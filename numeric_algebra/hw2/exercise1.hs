{- cabal:
build-depends: base, array, vector, hmatrix
-}

import Data.Foldable
import qualified Data.Vector as V
import qualified Data.Vector.Unboxed as UV

data Matrix = Matrix {rows :: Int, cols :: Int, entries :: UV.Vector Double}

{-# INLINE at #-}
at :: Matrix -> Int -> Int -> Double
at (Matrix _ cols es) i j = es UV.! (i * cols + j)

{-# INLINE mkMatrix #-}
mkMatrix :: Int -> Int -> (Int -> Int -> Double) -> Matrix
mkMatrix r c f =
  Matrix
    { rows = r,
      cols = c,
      entries = UV.generate (r * c) (\k -> f (k `div` c) (k `mod` c))
    }

{-# INLINE eps #-}
eps :: Double
eps = 1e-10

{-# INLINE isZero #-}
isZero :: Double -> Bool
isZero x = x <= eps && x >= -eps

-- ============================================================================
-- 打印矩阵辅助函数
-- ============================================================================
printMatrix :: Matrix -> IO ()
printMatrix m = mapM_ putStrLn [unwords [show (at m i j) | j <- [0 .. cols m - 1]] | i <- [0 .. rows m - 1]]

-- ============================================================================
-- 不选主元的高斯消元法（Gaussian Elimination Without Pivoting）
-- 使用向量优化性能
-- ============================================================================

-- 将矩阵转换为向量行表示（V.Vector of UV.Vector）
matrixToRowVectors :: Matrix -> V.Vector (UV.Vector Double)
matrixToRowVectors m =
  V.generate
    (rows m)
    (UV.generate (cols m) . at m)

-- 从向量行转换回矩阵
rowVectorsToMatrix :: Int -> Int -> V.Vector (UV.Vector Double) -> Matrix
rowVectorsToMatrix r c rowVecs =
  mkMatrix r c (\i j -> (rowVecs V.! i) UV.! j)

-- 消元一行：对第 i 行在第 k 列进行消元
-- 参数：row(待消元行), rowIndex(i), colIndex(k), pivot, allRows(所有行向量)
{-# INLINE eliminateRowVectorNoPivot #-}
eliminateRowVectorNoPivot :: UV.Vector Double -> Int -> Int -> Double -> V.Vector (UV.Vector Double) -> UV.Vector Double
eliminateRowVectorNoPivot row i k pivot allRows
  | i <= k = row -- 保留第 k 行及其上面的所有行
  | otherwise =
      let kRow = allRows V.! k
          factor = (row UV.! k) / pivot
       in -- 使用 UV.zipWith 高效计算：row[j] -= factor * kRow[j]
          UV.zipWith (\x y -> x - factor * y) row kRow

-- 不选主元的高斯消元法：将矩阵化为上三角矩阵
-- 对于第 k 列，使用对角线元素 A[k,k] 作为主元，消除下面的所有元素
gaussEliminationNoPivot :: Matrix -> Matrix
gaussEliminationNoPivot mat =
  let rowVecs = matrixToRowVectors mat
      numRows = rows mat
      numCols = cols mat
      -- 消元的步数：min(行数-1, 列数-1)
      maxStep = min (numRows - 1) (numCols - 1)
      -- 对每一列进行消元，使用 foldl' 保证严格求值
      resultRows = foldl' elimColumn rowVecs [0 .. maxStep]
   in rowVectorsToMatrix numRows numCols resultRows
  where
    -- 对第 k 列进行高斯消元
    elimColumn :: V.Vector (UV.Vector Double) -> Int -> V.Vector (UV.Vector Double)
    elimColumn rows k =
      let kRow = rows V.! k
          pivot = kRow UV.! k
       in -- 如果主元为 0，则无法进行消元，返回原向量组
          -- （这正是无主元法的缺点）
          if isZero pivot
            then rows
            else
              -- 优化：只处理 k+1 到最后的行，避免对 k 行及其以上的行做无谓检查
              V.generate (V.length rows) $ \i ->
                if i <= k then rows V.! i else eliminateRowVectorNoPivot (rows V.! i) i k pivot rows

-- 高斯-约当消元法（可选）：完全消元得到行简化阶梯形
-- 这个版本消除上下的所有元素，而不仅仅是下面的元素
gaussJordanEliminationNoPivot :: Matrix -> Matrix
gaussJordanEliminationNoPivot mat =
  let rowVecs = matrixToRowVectors mat
      numRows = rows mat
      numCols = cols mat
      maxStep = min (numRows - 1) (numCols - 1)
      resultRows = foldl' elimColumn rowVecs [0 .. maxStep]
   in rowVectorsToMatrix numRows numCols resultRows
  where
    elimColumn :: V.Vector (UV.Vector Double) -> Int -> V.Vector (UV.Vector Double)
    elimColumn rows k =
      let kRow = rows V.! k
          pivot = kRow UV.! k
       in if isZero pivot
            then rows
            else
              -- 优化：只处理非主元行，主元行直接保留
              V.generate (V.length rows) $ \i ->
                if i == k
                  then rows V.! i
                  else eliminateRowVectorGJNoPivot (rows V.! i) i k pivot rows

    -- 高斯-约当消元：消除上下两个方向的元素
    eliminateRowVectorGJNoPivot :: UV.Vector Double -> Int -> Int -> Double -> V.Vector (UV.Vector Double) -> UV.Vector Double
    eliminateRowVectorGJNoPivot row i k pivot allRows =
      let kRow = allRows V.! k
          factor = (row UV.! k) / pivot
       in UV.zipWith (\x y -> x - factor * y) row kRow

-- ============================================================================
-- LU分解（不选主元）- 返回下三角矩阵L和上三角矩阵U
-- 其中A = LU，L的对角线为1，U是上三角矩阵
-- 使用纯函数式方法：逐步构建L和U
-- ============================================================================

-- 数据结构存储LU分解结果
data LUDecomposition = LUDecomposition
  { luL :: Matrix, -- 下三角矩阵L
    luU :: Matrix -- 上三角矩阵U
  }

-- LU 分解的纯函数式实现
-- 基本思想：逐列执行高斯消元，同时记录消元因子构造L矩阵
luDecompositionNoPivot :: Matrix -> LUDecomposition
luDecompositionNoPivot mat =
  let n = rows mat
      m = cols mat
      -- 初始化 U = A，L = I
      u = mkMatrix n m (at mat)
      l = mkMatrix n n (\i j -> if i == j then 1.0 else 0.0)
      -- 逐列执行 Doolittle 方法
      (finalU, finalL) = decompose u l 0
   in LUDecomposition {luU = finalU, luL = finalL}
  where
    n = rows mat
    m = cols mat

    -- 递归分解第 k 列及之后的所有列
    decompose :: Matrix -> Matrix -> Int -> (Matrix, Matrix)
    decompose u l k
      | k >= min (n - 1) (m - 1) = (u, l)
      | isZero (at u k k) = (u, l) -- 主元为 0，无法继续
      | otherwise =
          let pivot = at u k k
              -- 对所有 i > k 的行计算消元因子并消元
              processRows :: Matrix -> Matrix -> Int -> (Matrix, Matrix)
              processRows u' l' i
                | i >= n = (u', l')
                | i <= k = processRows u' l' (i + 1)
                | otherwise =
                    let factor = at u' i k / pivot
                        -- 更新 U: U[i,j] -= factor * U[k,j] for all j >= k
                        newU =
                          mkMatrix
                            n
                            m
                            ( \r c ->
                                if r == i && c >= k
                                  then at u' r c - factor * at u' k c
                                  else at u' r c
                            )
                        -- 更新 L: L[i,k] = factor
                        newL =
                          mkMatrix
                            n
                            n
                            ( \r c ->
                                if r == i && c == k
                                  then factor
                                  else at l' r c
                            )
                     in processRows newU newL (i + 1)
           in uncurry decompose (processRows u l k) (k + 1)

-- ============================================================================
-- 前代法（Forward Substitution）- 求解 Ly = b
-- L是下三角矩阵，对角线元素为1
-- 使用分步计算避免循环依赖
-- ============================================================================
forwardSubstitutionNoPivot :: Matrix -> UV.Vector Double -> UV.Vector Double
forwardSubstitutionNoPivot lMat b =
  let n = rows lMat
      -- 从上到下逐行计算 y[i]
      solve i yPrev =
        if i >= n
          then yPrev
          else
            let -- 只计算 L[i, 0:i]，L[i,i] = 1
                sumVal =
                  if i == 0
                    then 0.0
                    else
                      UV.sum $
                        UV.zipWith
                          (*)
                          (UV.slice 0 i (UV.generate i (at lMat i)))
                          (UV.slice 0 i yPrev)
                yi = b UV.! i - sumVal
                newY = yPrev UV.++ UV.singleton yi
             in solve (i + 1) newY
   in solve 0 UV.empty

-- ============================================================================
-- 回代法（Back Substitution）- 求解 Ux = y
-- U是上三角矩阵
-- 使用分步计算从下到上逐行求解
-- ============================================================================
backSubstitutionNoPivot :: Matrix -> UV.Vector Double -> UV.Vector Double
backSubstitutionNoPivot uMat y =
  let n = rows uMat
      m = cols uMat
      -- 从下到上逐行计算 x[i]
      solve i xNext =
        if i < 0
          then xNext
          else
            let diag = at uMat i i
                -- 只计算 U[i, i+1:n] 的部分
                restStart = i + 1
                restLen = max 0 (n - restStart)
                sumVal =
                  if restLen == 0
                    then 0.0
                    else
                      UV.sum $
                        UV.zipWith
                          (*)
                          (UV.slice restStart restLen (UV.generate m (at uMat i)))
                          (UV.slice 0 restLen xNext)
                xi =
                  if not (isZero diag)
                    then (y UV.! i - sumVal) / diag
                    else 0.0
                newX = UV.cons xi xNext
             in solve (i - 1) newX
   in solve (n - 1) UV.empty

-- ============================================================================
-- 求解线性方程 Ax = b 通过LU分解
-- ============================================================================
solveLUNoPivot :: Matrix -> UV.Vector Double -> UV.Vector Double
solveLUNoPivot aMat b =
  let luDec = luDecompositionNoPivot aMat
      -- 第一步：求解 Ly = b
      y = forwardSubstitutionNoPivot (luL luDec) b
      -- 第二步：求解 Ux = y
      x = backSubstitutionNoPivot (luU luDec) y
   in x

-- 获取向量的字符串表示用于打印
printVector :: UV.Vector Double -> String
printVector v = "[" ++ unwords (map show (UV.toList v)) ++ "]"

-- 测试函数
main :: IO ()
main = do
  putStrLn "============================================================"
  putStrLn "示例 1: 演示高斯消元和高斯-约当消元"
  putStrLn "============================================================"
  putStrLn "原始矩阵 A (3x4):"
  let a =
        mkMatrix
          3
          4
          ( \i j ->
              if i == 0 && j == 0
                then 2
                else
                  if i == 0 && j == 1
                    then 1
                    else
                      if i == 0 && j == 2
                        then -1
                        else
                          if i == 0 && j == 3
                            then 8
                            else
                              if i == 1 && j == 0
                                then -3
                                else
                                  if i == 1 && j == 1
                                    then -1
                                    else
                                      if i == 1 && j == 2
                                        then 2
                                        else
                                          if i == 1 && j == 3
                                            then -11
                                            else
                                              if i == 2 && j == 0
                                                then -2
                                                else
                                                  if i == 2 && j == 1
                                                    then 1
                                                    else
                                                      if i == 2 && j == 2
                                                        then 2
                                                        else 3
          )
  printMatrix a
  putStrLn "\n不选主元的高斯消元后（上三角矩阵）:"
  let u = gaussEliminationNoPivot a
  printMatrix u
  putStrLn "\n高斯-约当消元后（行简化阶梯形）:"
  let rref = gaussJordanEliminationNoPivot a
  printMatrix rref

  putStrLn "\n============================================================"
  putStrLn "示例 2: LU 分解和求解线性方程 Ax = b"
  putStrLn "============================================================"
  -- 定义一个 3x3 系统矩阵
  let systemA =
        mkMatrix
          3
          3
          ( \i j ->
              if i == 0 && j == 0
                then 2
                else
                  if i == 0 && j == 1
                    then 1
                    else
                      if i == 0 && j == 2
                        then -1
                        else
                          if i == 1 && j == 0
                            then -3
                            else
                              if i == 1 && j == 1
                                then -1
                                else
                                  if i == 1 && j == 2
                                    then 2
                                    else
                                      if i == 2 && j == 0
                                        then -2
                                        else if i == 2 && j == 1 then 1 else 2
          )
  putStrLn "系统矩阵 A:"
  printMatrix systemA

  -- 定义右边向量 b = [8, -11, 3]^T
  let b = UV.fromList [8, -11, 3]
  putStrLn "\n右边向量 b:"
  putStrLn $ printVector b

  -- 执行 LU 分解
  let luDec = luDecompositionNoPivot systemA
  putStrLn "\nLU 分解结果："
  putStrLn "下三角矩阵 L (对角线为1):"
  printMatrix (luL luDec)
  putStrLn "\n上三角矩阵 U:"
  printMatrix (luU luDec)

  -- 求解线性方程
  let x = solveLUNoPivot systemA b
  putStrLn "\n求解 Ax = b 的结果 x:"
  putStrLn $ printVector x

  -- 验证解：计算 Ax 并与 b 比较
  putStrLn "\n验证：计算 Ax ="
  let ax =
        UV.generate
          (rows systemA)
          ( \i ->
              UV.sum $ UV.zipWith (*) (UV.generate (cols systemA) (at systemA i)) x
          )
  putStrLn $ printVector ax
  putStrLn "原始 b ="
  putStrLn $ printVector b
  putStrLn "误差 ||Ax - b|| (应该接近0):"
  let err = sqrt $ UV.sum $ UV.map (\v -> v * v) (UV.zipWith (-) ax b)
  print err
