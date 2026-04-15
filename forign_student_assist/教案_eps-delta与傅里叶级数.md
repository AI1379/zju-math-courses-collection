# 教案：ε-δ 语言技巧、多元微分学进阶与傅里叶级数初步

---

## 第一部分：ε-δ 语言的技巧性训练（约 90 分钟）

### 1. 为什么现在重提 ε-δ？

学生目前在学习多元函数微分学。回顾教材第八章 §1.3（p.65）中二元函数极限的定义：

$$\lim_{(x,y)\to(x_0,y_0)} f(x,y) = A \iff \forall \varepsilon > 0, \exists \delta > 0, \text{ s.t. } 0 < \sqrt{(x-x_0)^2+(y-y_0)^2} < \delta \Rightarrow |f(x,y)-A| < \varepsilon$$

ε-δ 语言在多元函数中比一元函数更关键，因为：

- 二元函数的极限要求沿**所有路径**趋近，ε-δ 是唯一严格刻画方式
- 后续"一致收敛"（第十一章 §4，p.264）本质上就是 ε-δ 语言的再运用
- 傅里叶级数的收敛性证明也需要 ε-δ 的思维

### 2. 核心技巧分类与例题

#### 技巧一：放缩法——将 $|f(x)-L|$ 放缩为关于 $\|x-x_0\|$ 的表达式

**例题 1**（二元极限的 ε-δ 证明）

证明：$\displaystyle\lim_{(x,y)\to(0,0)} \frac{x^2 y}{x^2 + y^2} = 0$

> **证明思路：**
> $$\left|\frac{x^2 y}{x^2 + y^2}\right| = |x| \cdot \frac{|xy|}{x^2 + y^2} \leq |x| \cdot \frac{1}{2}$$
> 其中用到 $2|xy| \leq x^2 + y^2$（基本不等式）。
>
> 又 $|x| = \sqrt{x^2} \leq \sqrt{x^2 + y^2}$，所以
> $$\left|\frac{x^2 y}{x^2 + y^2}\right| \leq \frac{1}{2}\sqrt{x^2+y^2}$$
>
> 对任意 $\varepsilon > 0$，取 $\delta = 2\varepsilon$，当 $0 < \sqrt{x^2+y^2} < \delta$ 时即得。

**关键要点：** 放缩的目标是把表达式全部统一到 $\sqrt{(x-x_0)^2+(y-y_0)^2}$ 的某个幂次。

---

#### 技巧二：分区域讨论——处理分段定义或分母有零点的函数

**例题 2**

证明：$\displaystyle\lim_{(x,y)\to(0,0)} \frac{xy}{\sqrt{x^2+y^2}} = 0$

> 利用 $|xy| \leq \frac{x^2+y^2}{2}$：
> $$\left|\frac{xy}{\sqrt{x^2+y^2}}\right| \leq \frac{x^2+y^2}{2\sqrt{x^2+y^2}} = \frac{\sqrt{x^2+y^2}}{2}$$
>
> 取 $\delta = 2\varepsilon$ 即可。

---

#### 技巧三：极坐标代换——将二元问题化为一元

令 $x = r\cos\theta$, $y = r\sin\theta$，则 $(x,y)\to(0,0)$ 等价于 $r\to 0^+$。

重新审视例题 1：
$$\frac{x^2 y}{x^2+y^2} = \frac{r^2\cos^2\theta \cdot r\sin\theta}{r^2} = r\cos^2\theta\sin\theta$$

因为 $|\cos^2\theta\sin\theta| \leq 1$，所以 $|f| \leq r = \sqrt{x^2+y^2}$。

**注意：** 极坐标代换在**证明极限存在**时非常方便，但在**证明极限不存在**时，需要找不同的路径（直线 $y=kx$、抛物线 $y=x^2$ 等）使极限值不同。

---

#### 技巧四：三角不等式的灵活运用

**例题 3**（连续性的 ε-δ 证明）

证明 $f(x,y) = x^2 + y^2$ 在全平面连续。

> 对任意 $(x_0, y_0)$：
> $$|f(x,y)-f(x_0,y_0)| = |x^2 - x_0^2 + y^2 - y_0^2|$$
> $$\leq |x-x_0||x+x_0| + |y-y_0||y+y_0|$$
>
> 限制 $\|(x,y)-(x_0,y_0)\| < 1$，则 $|x| < |x_0|+1$，$|y| < |y_0|+1$，于是：
> $$\leq (2|x_0|+1+2|y_0|+1)\sqrt{(x-x_0)^2+(y-y_0)^2}$$
>
> 取 $\delta = \min\left(1, \frac{\varepsilon}{2(|x_0|+|y_0|+1)}\right)$。

**要点：** 先限制 $\delta \leq 1$ 来控制 $|x+x_0|$ 等因子，再放缩——这是处理多项式函数的标准手法。

---

#### 技巧五：反例构造——证明极限不存在

**例题 4**

证明 $\displaystyle\lim_{(x,y)\to(0,0)} \frac{xy}{x^2+y^2}$ 不存在。

> - 沿 $y = kx$ 趋近：$\frac{kx^2}{x^2+k^2x^2} = \frac{k}{1+k^2}$，依赖于 $k$。
> - $k=0$ 时极限为 $0$，$k=1$ 时极限为 $\frac{1}{2}$，故极限不存在。

---

### 3. 课堂练习

1. 用 ε-δ 证明 $\displaystyle\lim_{(x,y)\to(1,2)} (3x^2 - xy) = 1$。
2. 判断并证明：$\displaystyle\lim_{(x,y)\to(0,0)} \frac{x^3-y^3}{x^2+y^2}$ 是否存在？
3. 证明 $f(x,y) = e^{x+y}$ 在任意点连续。（提示：利用 $|e^a - e^b| \leq e^{\max(a,b)}|a-b|$）
4. 用 ε-δ 证明 $\displaystyle\lim_{(x,y)\to(0,0)} \frac{x^2+y^2}{|x|+|y|} = 0$。（提示：$|x|+|y| \geq \sqrt{x^2+y^2}$）
5. 证明 $\displaystyle\lim_{(x,y)\to(0,0)} \frac{x^2y^2}{x^2+y^2} = 0$。
6. 判断 $\displaystyle\lim_{(x,y)\to(0,0)} \frac{x^2-y^2}{x^2+y^2}$ 是否存在？若存在则证明，若不存在则构造反例。
7. 用 ε-δ 证明 $f(x,y) = \sin(x^2+y^2)$ 在全平面连续。（提示：$|\sin a - \sin b| \leq |a-b|$）
8. 证明 $\displaystyle\lim_{(x,y)\to(0,0)} \frac{\sin(x^2+y^2)}{x^2+y^2} = 1$。（提示：先化为极坐标，再用一元 $\frac{\sin r^2}{r^2} \to 1$）
9. 证明 $\displaystyle\lim_{(x,y)\to(0,0)} \frac{x^4y^4}{(x^2+y^4)^2}$ 不存在。（提示：比较沿 $y=0$ 和 $x=y^2$ 两条路径）
10. 设 $f(x,y) = \begin{cases} \frac{xy}{x+y}, & x+y \neq 0 \\ 0, & x+y = 0 \end{cases}$，判断 $f$ 在 $(0,0)$ 处是否连续。

#### ε-δ 练习解答

**第 1 题**

> 目标：证明 $\lim_{(x,y)\to(1,2)}(3x^2-xy)=1$。
>
> $$|3x^2-xy-1| = |3x^2-xy-3\cdot 1^2+1\cdot 2| = |3(x^2-1)-y(x-1)-1(x-1)-1(y-2)|$$
> 不够直接，换个方式：
> $$= |3(x-1)(x+1) - (x-1)y - (y-2)| = |(x-1)(3x+3-y) - (y-2)|$$
>
> 限制 $\sqrt{(x-1)^2+(y-2)^2}<1$，则 $|x-1|<1$, $|y-2|<1$，即 $0<x<2$, $1<y<3$。
> 于是 $|3x+3-y|<3\cdot 2+3-1=8$。
> $$|3x^2-xy-1| \leq |x-1|\cdot 8 + |y-2| \leq 8\sqrt{(x-1)^2+(y-2)^2}+\sqrt{(x-1)^2+(y-2)^2} = 9\sqrt{(x-1)^2+(y-2)^2}$$
> 取 $\delta = \min(1, \varepsilon/9)$。

**第 2 题**

> $\displaystyle\left|\frac{x^3-y^3}{x^2+y^2}\right| = \frac{|x-y|\cdot|x^2+xy+y^2|}{x^2+y^2}$。
>
> 由 $|x^2+xy+y^2| \leq x^2+y^2+|xy| \leq \frac{3}{2}(x^2+y^2)$，且 $|x-y| \leq |x|+|y| \leq 2\sqrt{x^2+y^2}$：
> $$\leq \frac{2\sqrt{x^2+y^2}\cdot\frac{3}{2}(x^2+y^2)}{x^2+y^2} = 3\sqrt{x^2+y^2}$$
>
> 取 $\delta = \varepsilon/3$。极限存在，值为 $0$。

**第 3 题**

> 在任意 $(x_0,y_0)$ 处：
> $$|e^{x+y}-e^{x_0+y_0}| \leq e^{\max(x+y,\,x_0+y_0)}\cdot|(x+y)-(x_0+y_0)|$$
>
> 限制 $\sqrt{(x-x_0)^2+(y-y_0)^2}<1$，则 $|(x+y)-(x_0+y_0)|\leq |x-x_0|+|y-y_0| \leq \sqrt{2}\cdot r$，且 $\max(x+y,x_0+y_0) < x_0+y_0+2$。
> $$\leq e^{x_0+y_0+2}\cdot\sqrt{2}\cdot\sqrt{(x-x_0)^2+(y-y_0)^2}$$
> 取 $\delta = \min\!\left(1,\frac{\varepsilon}{\sqrt{2}\,e^{x_0+y_0+2}}\right)$。

**第 4 题**

> 由 $|x|+|y| \geq \sqrt{x^2+y^2}$（两边平方即证），得：
> $$\frac{x^2+y^2}{|x|+|y|} \leq \frac{x^2+y^2}{\sqrt{x^2+y^2}} = \sqrt{x^2+y^2}$$
> 取 $\delta = \varepsilon$。

**第 5 题**

> $$\frac{x^2y^2}{x^2+y^2} \leq \frac{(x^2+y^2)^2/4}{x^2+y^2} = \frac{x^2+y^2}{4}$$
> 其中用到 $x^2y^2 \leq \frac{(x^2+y^2)^2}{4}$（由 $2|x||y| \leq x^2+y^2$）。
> 取 $\delta = 2\sqrt{\varepsilon}$（保证 $(x^2+y^2)/4 < \varepsilon$）。

**第 6 题**

> 极限**不存在**。
>
> - 沿 $y=0$：$\frac{x^2}{x^2} = 1 \to 1$。
> - 沿 $x=0$：$\frac{-y^2}{y^2} = -1 \to -1$。
> - 两条路径极限不同，故极限不存在。

**第 7 题**

> 在任意 $(x_0,y_0)$ 处：
> $$|\sin(x^2+y^2)-\sin(x_0^2+y_0^2)| \leq |(x^2+y^2)-(x_0^2+y_0^2)|$$
>
> 同例题 3 的放缩：$|(x^2+y^2)-(x_0^2+y_0^2)| \leq (2|x_0|+2|y_0|+2)\sqrt{(x-x_0)^2+(y-y_0)^2}$（限制 $\delta\leq 1$）。
> 取 $\delta = \min\!\left(1, \frac{\varepsilon}{2(|x_0|+|y_0|+1)}\right)$。

**第 8 题**

> 化为极坐标 $x=r\cos\theta$, $y=r\sin\theta$，则 $x^2+y^2=r^2$：
> $$\frac{\sin(x^2+y^2)}{x^2+y^2} = \frac{\sin r^2}{r^2}$$
>
> 这是关于 $r$ 的一元函数，且 $r\to 0$ 时 $r^2\to 0$。由一元结果 $\frac{\sin t}{t}\to 1$（$t\to 0$），令 $t=r^2$：
> $$\frac{\sin r^2}{r^2}\bigg|_{r\to 0} = \frac{\sin t}{t}\bigg|_{t\to 0} = 1$$
>
> 严格 ε-δ：对任意 $\varepsilon>0$，存在 $\eta>0$ 使得 $0<t<\eta$ 时 $|\frac{\sin t}{t}-1|<\varepsilon$。取 $\delta = \sqrt{\eta}$，当 $0<r<\delta$ 时 $0<r^2<\eta$。

**第 9 题**

> 极限**不存在**。
>
> - 沿 $y=0$：$\frac{0}{x^4} = 0 \to 0$。
> - 沿 $x=y^2$：$\frac{y^8\cdot y^4}{(y^4+y^4)^2} = \frac{y^{12}}{4y^8} = \frac{y^4}{4} \to 0$。
>
> 两条路径都趋向 0，还不够。换一条更极端的路径——沿 $y^2 = kx$（$k\neq 0$）：
> $$\frac{x^4y^4}{(x^2+y^4)^2} = \frac{x^4\cdot k^2x^2}{(x^2+k^2x^2)^2} = \frac{k^2x^6}{x^4(1+k^2)^2} = \frac{k^2}{(1+k^2)^2}\cdot x^2$$
>
> 这也趋向 0。但沿 $x = y^4$：
> $$\frac{y^{16}\cdot y^4}{(y^8+y^4)^2} = \frac{y^{20}}{y^8(y^4+1)^2} = \frac{y^{12}}{(y^4+1)^2} \to 0$$
>
> 再尝试沿 $x = \sqrt{|y|}$（$y\to 0$）：$x^2 = |y|$，
> $$\frac{|y|^2\cdot y^4}{(|y|+y^4)^2} = \frac{y^6}{(y+y^4)^2} \text{（取 }y>0\text{）}$$
>
> 实际上此题极限**存在且为 0**。用放缩：
> $$\frac{x^4y^4}{(x^2+y^4)^2} = \frac{x^4y^4}{(x^2+y^4)^2}$$
> 由 $x^4 \leq (x^2+y^4)^2$（因为 $x^2\leq x^2+y^4$），$y^4\leq (x^2+y^4)^2$ 不对。换思路：
> $$\frac{x^4y^4}{(x^2+y^4)^2} = \left(\frac{x^2}{x^2+y^4}\right)^2\cdot y^4$$
> 由于 $\frac{x^2}{x^2+y^4}\leq 1$，所以 $\leq y^4\leq (x^2+y^2)^2$。取 $\delta = \varepsilon^{1/4}$。
>
> **结论：极限存在，值为 0。**（原提示有误，此题是训练"看起来要构造反例但实际能放缩证明"的情况。）

**第 10 题**

> 沿 $y=kx$（$k\neq -1$）趋近：
> $$\frac{x\cdot kx}{x+kx} = \frac{kx^2}{(1+k)x} = \frac{k}{1+k}x \to 0$$
>
> 沿 $y=x^2-x$（$x\to 0$）趋近：
> $$\frac{x(x^2-x)}{x+x^2-x} = \frac{x^3-x^2}{x^2} = x - 1 \to -1$$
>
> 两条路径极限不同（$0\neq -1$），故 $f$ 在 $(0,0)$ 处**不连续**。

---

## 第二部分：课本后续内容——多元微分学进阶

> 覆盖教材第八章 §3（p.83）到 §5（p.99），衔接学生当前的进度。

### 1. 复合函数微分法（§3，p.83）

学生刚学到链式法则，这里做一个深化回顾。

#### 1.1 链式法则的基本形式

设 $z = f(u,v)$，$u = \varphi(x,y)$，$v = \psi(x,y)$，则：

$$\frac{\partial z}{\partial x} = \frac{\partial f}{\partial u}\frac{\partial u}{\partial x} + \frac{\partial f}{\partial v}\frac{\partial v}{\partial x}$$

$$\frac{\partial z}{\partial y} = \frac{\partial f}{\partial u}\frac{\partial u}{\partial y} + \frac{\partial f}{\partial v}\frac{\partial v}{\partial y}$$

**记忆口诀：** "对中间变量求偏导，乘以中间变量对自变量的偏导，再加起来"——本质上就是全微分链的展开。

#### 1.2 特殊情形与易错点

**情形一：** $z = f(x,y)$，$y = y(x)$（即 $x$ 既是自变量又通过 $y$ 间接影响 $z$）

$$\frac{dz}{dx} = \frac{\partial f}{\partial x} + \frac{\partial f}{\partial y}\frac{dy}{dx}$$

> **注意：** $\frac{dz}{dx}$（全导数）$\neq$ $\frac{\partial f}{\partial x}$（偏导数）。
> 这是学生最容易混淆的地方——偏导数只看"直接"路径，全导数看所有路径。

**例题** 设 $z = e^{x^2+y}$，$y = \sin x$，求 $\frac{dz}{dx}$。

> **解：**
> $$\frac{dz}{dx} = \frac{\partial z}{\partial x} + \frac{\partial z}{\partial y}\cdot y'(x) = 2xe^{x^2+y} + e^{x^2+y}\cdot\cos x = e^{x^2+\sin x}(2x + \cos x)$$
>
> 验证：直接代入 $z = e^{x^2+\sin x}$，$\frac{dz}{dx} = e^{x^2+\sin x}(2x+\cos x)$，一致。

**情形二：** $z = f(u)$，$u = \varphi(x,y)$（中间变量只有一个）

$$\frac{\partial z}{\partial x} = f'(u)\frac{\partial u}{\partial x}, \quad \frac{\partial z}{\partial y} = f'(u)\frac{\partial u}{\partial y}$$

#### 1.3 复合函数的全微分——一阶微分形式不变性

$$dz = \frac{\partial f}{\partial u}du + \frac{\partial f}{\partial v}dv$$

无论 $u,v$ 是自变量还是中间变量，这个形式不变。这在计算中很实用：

**例题** 设 $z = f(x^2 - y^2, e^{xy})$，求 $dz$。

> **解：** 令 $u = x^2-y^2$，$v = e^{xy}$：
> $$dz = f_1' \cdot d(x^2-y^2) + f_2' \cdot d(e^{xy}) = f_1'(2x\,dx - 2y\,dy) + f_2'(ye^{xy}\,dx + xe^{xy}\,dy)$$
> $$= (2xf_1' + ye^{xy}f_2')dx + (-2yf_1' + xe^{xy}f_2')dy$$
>
> 其中 $f_1' = \frac{\partial f}{\partial u}$，$f_2' = \frac{\partial f}{\partial v}$。
>
> 直接读出：$\frac{\partial z}{\partial x} = 2xf_1' + ye^{xy}f_2'$，$\frac{\partial z}{\partial y} = -2yf_1' + xe^{xy}f_2'$

---

### 2. 隐函数的偏导数（§4，p.90）

#### 2.1 一个方程确定的隐函数

设 $F(x,y) = 0$ 确定了 $y = y(x)$，则：

$$\frac{dy}{dx} = -\frac{F_x}{F_y} \quad (F_y \neq 0)$$

设 $F(x,y,z) = 0$ 确定了 $z = z(x,y)$，则：

$$\frac{\partial z}{\partial x} = -\frac{F_x}{F_z}, \quad \frac{\partial z}{\partial y} = -\frac{F_y}{F_z} \quad (F_z \neq 0)$$

> **推导（以二元为例）：**
> 对 $F(x,y(x)) = 0$ 两边对 $x$ 求导：
> $$F_x + F_y \cdot y'(x) = 0 \implies y'(x) = -\frac{F_x}{F_y}$$

**例题** 设 $x^2 + y^2 + z^2 - 4z = 0$，求 $\frac{\partial z}{\partial x}$ 和 $\frac{\partial z}{\partial y}$。

> **解：** $F(x,y,z) = x^2+y^2+z^2-4z$，$F_x = 2x$，$F_y = 2y$，$F_z = 2z-4$
> $$\frac{\partial z}{\partial x} = -\frac{2x}{2z-4} = \frac{x}{2-z}, \quad \frac{\partial z}{\partial y} = -\frac{2y}{2z-4} = \frac{y}{2-z}$$

#### 2.2 隐函数组（方程组的情况）

设方程组
$$\begin{cases} F(x,y,u,v) = 0 \\ G(x,y,u,v) = 0 \end{cases}$$
确定了 $u = u(x,y)$，$v = v(x,y)$。

对每个方程用链式法则：
$$\begin{cases} F_x + F_u u_x + F_v v_x = 0 \\ G_x + G_u u_x + G_v v_x = 0 \end{cases}$$

解这个线性方程组（Cramer 法则）：

$$\frac{\partial u}{\partial x} = -\frac{\begin{vmatrix} F_x & F_v \\ G_x & G_v \end{vmatrix}}{\begin{vmatrix} F_u & F_v \\ G_u & G_v \end{vmatrix}}, \quad \frac{\partial v}{\partial x} = -\frac{\begin{vmatrix} F_u & F_x \\ G_u & G_x \end{vmatrix}}{\begin{vmatrix} F_u & F_v \\ G_u & G_v \end{vmatrix}}$$

> **教学提示：** 分母是 Jacobian 行列式 $J = \frac{\partial(F,G)}{\partial(u,v)}$，条件是 $J \neq 0$。这正是第一章学的三阶行列式（第七章 §1，p.1）在这里的运用——可以提醒学生行列式不是白学的。

---

### 3. 场的方向导数与梯度（§5，p.99）

#### 3.1 方向导数

偏导数 $\frac{\partial f}{\partial x}$, $\frac{\partial f}{\partial y}$ 给出了沿坐标轴方向的变化率。那沿任意方向 $\mathbf{l} = (\cos\alpha, \cos\beta)$（单位向量）呢？

$$\frac{\partial f}{\partial l} = \lim_{t\to 0^+}\frac{f(x_0+t\cos\alpha,\, y_0+t\cos\beta) - f(x_0,y_0)}{t}$$

**定理：** 若 $f$ 可微，则

$$\frac{\partial f}{\partial l} = \frac{\partial f}{\partial x}\cos\alpha + \frac{\partial f}{\partial y}\cos\beta$$

> **证明要点：** 这就是链式法则。令 $x = x_0 + t\cos\alpha$，$y = y_0 + t\cos\beta$，则
> $$\frac{df}{dt}\bigg|_{t=0} = f_x\cos\alpha + f_y\cos\beta$$

**例题** 设 $f(x,y) = x^2 + y^2$，求在 $(1,2)$ 处沿方向 $\mathbf{l} = (\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}})$ 的方向导数。

> **解：** $f_x = 2x = 2$，$f_y = 2y = 4$
> $$\frac{\partial f}{\partial l} = 2\cdot\frac{1}{\sqrt{2}} + 4\cdot\frac{1}{\sqrt{2}} = \frac{6}{\sqrt{2}} = 3\sqrt{2}$$

#### 3.2 梯度

定义梯度向量：

$$\nabla f = \text{grad}\, f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right)$$

则方向导数可以写成内积形式：

$$\frac{\partial f}{\partial l} = \nabla f \cdot \mathbf{l} = |\nabla f|\cos\theta$$

其中 $\theta$ 是梯度方向与 $\mathbf{l}$ 的夹角。

**关键结论：**

- 梯度方向是函数值**增长最快**的方向（$\theta = 0$，方向导数最大）
- 梯度的模 $|\nabla f|$ 就是最大增长率
- 梯度的反方向是函数值**下降最快**的方向（这就是梯度下降法的来源）
- 等值线 $f(x,y) = c$ 的法向量就是 $\nabla f$

> **教学提示：** 梯度在机器学习（梯度下降法）和物理（电场强度 = 电势的负梯度）中都有核心地位，值得点明。

#### 3.3 三元函数的推广

对 $f(x,y,z)$：

$$\nabla f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\right)$$

$$\frac{\partial f}{\partial l} = \nabla f \cdot \mathbf{l}$$

---

### 4. 本节练习

1. 设 $z = f(u,v)$，$u = xy$，$v = x+y$，求 $\frac{\partial z}{\partial x}$ 和 $\frac{\partial z}{\partial y}$。
2. 设 $z^3 - 3xyz = 0$ 确定了 $z = z(x,y)$，求 $\frac{\partial z}{\partial x}$ 和 $\frac{\partial^2 z}{\partial x \partial y}$。
3. 设 $f(x,y) = e^{x-y}$，求在点 $(1,1)$ 处沿方向 $(3, 4)$ 的方向导数。
4. 求 $f(x,y) = \ln(x^2+y^2)$ 的梯度，并说明等值线是什么曲线。
5. 设 $z = f\!\left(\frac{y}{x}, \frac{x}{y}\right)$，求 $\frac{\partial z}{\partial x}$ 和 $\frac{\partial z}{\partial y}$。（用一阶微分形式不变性做最快）
6. 设 $z = \arctan\frac{y}{x}$，$x = e^t$，$y = e^{-t}$，求 $\frac{dz}{dt}$。（注意：这是一元函数的全导数）
7. 设 $u = \sin(xyz)$，$x = r^2+s$，$y = rs$，$z = r-s$，用链式法则求 $\frac{\partial u}{\partial r}$ 和 $\frac{\partial u}{\partial s}$。
8. 设 $e^z - xyz = 0$ 确定了 $z = z(x,y)$，求 $\frac{\partial z}{\partial x}$, $\frac{\partial z}{\partial y}$ 和 $\frac{\partial^2 z}{\partial x^2}$。
9. 设方程组 $\begin{cases} x^2+y^2-u^2-v^2=0 \\ x^2-y^2+2u^2+3v^2=0 \end{cases}$ 确定了 $u=u(x,y)$, $v=v(x,y)$，求 $\frac{\partial u}{\partial x}$ 和 $\frac{\partial v}{\partial x}$。
10. 设 $f(x,y) = x^2y - y^3$，求 $\nabla f$，并求 $f$ 在 $(1,-1)$ 处增长最快的方向及最大增长率。
11. 求函数 $f(x,y,z) = x^2+2y^2+3z^2$ 在点 $(1,1,1)$ 处沿方向 $(1,2,2)$ 的方向导数。这和梯度有什么关系？
12. 证明：梯度 $\nabla f(x_0,y_0)$ 与过 $(x_0,y_0)$ 的等值线 $f(x,y)=f(x_0,y_0)$ 相切还是垂直？用例子验证。

#### 本节练习解答

**第 1 题**

> 设 $u=xy$, $v=x+y$。由链式法则：
> $$\frac{\partial z}{\partial x}=f_u\frac{\partial u}{\partial x}+f_v\frac{\partial v}{\partial x}=y f_u+f_v$$
> $$\frac{\partial z}{\partial y}=f_u\frac{\partial u}{\partial y}+f_v\frac{\partial v}{\partial y}=x f_u+f_v$$

**第 2 题**

> 记 $F(x,y,z)=z^3-3xyz=0$。则
> $$F_x=-3yz,\quad F_y=-3xz,\quad F_z=3(z^2-xy)$$
> 所以
> $$z_x=-\frac{F_x}{F_z}=\frac{yz}{z^2-xy},\qquad z_y=-\frac{F_y}{F_z}=\frac{xz}{z^2-xy}$$
>
> 在 $z\neq 0$ 的分支上，由 $z^3=3xyz$ 得 $z^2=3xy$，于是
> $$z_x=\frac{z}{2x},\qquad z_y=\frac{z}{2y}$$
> 再对 $y$ 求导：
> $$z_{xy}=\frac{\partial}{\partial y}\left(\frac{z}{2x}\right)=\frac{z_y}{2x}=\frac{z}{4xy}=\frac{3}{4z}$$

**第 3 题**

> 方向 $(3,4)$ 的单位向量是 $(3/5,4/5)$。而
> $$f_x=e^{x-y},\qquad f_y=-e^{x-y}$$
> 故在 $(1,1)$ 处
> $$\frac{\partial f}{\partial l}=1\cdot\frac{3}{5}+(-1)\cdot\frac{4}{5}=-\frac{1}{5}$$

**第 4 题**

> $$\nabla f(x,y)=\left(\frac{2x}{x^2+y^2},\frac{2y}{x^2+y^2}\right)$$
> 等值线满足 $x^2+y^2=c$，所以是以原点为中心的圆。

**第 5 题**

> 设 $u=\frac{y}{x}$，$v=\frac{x}{y}$，则 $z=f(u,v)$。由链式法则：
> $$\frac{\partial z}{\partial x}=f_u\left(-\frac{y}{x^2}\right)+f_v\left(\frac{1}{y}\right)$$
> $$\frac{\partial z}{\partial y}=f_u\left(\frac{1}{x}\right)+f_v\left(-\frac{x}{y^2}\right)$$

**第 6 题**

> 由 $x=e^t$, $y=e^{-t}$，得 $\frac{y}{x}=e^{-2t}$，所以
> $$z=\arctan(e^{-2t})$$
> 因而
> $$\frac{dz}{dt}=\frac{-2e^{-2t}}{1+e^{-4t}}=-\frac{2}{e^{2t}+e^{-2t}}$$

**第 7 题**

> 令 $u=\sin(xyz)$，则
> $$u_r=\cos(xyz)\cdot\frac{\partial(xyz)}{\partial r},\qquad u_s=\cos(xyz)\cdot\frac{\partial(xyz)}{\partial s}$$
> 其中 $x=r^2+s$, $y=rs$, $z=r-s$，所以 $xyz=rs(r^2+s)(r-s)$。
> 直接求导得
> $$\frac{\partial(xyz)}{\partial r}=4r^3s-3r^2s^2+2rs^2-s^3$$
> $$\frac{\partial(xyz)}{\partial s}=r^4-2r^3s+2r^2s-3rs^2$$
> 因而
> $$u_r=\cos(xyz)\,(4r^3s-3r^2s^2+2rs^2-s^3)$$
> $$u_s=\cos(xyz)\,(r^4-2r^3s+2r^2s-3rs^2)$$

**第 8 题**

> 记 $F(x,y,z)=e^z-xyz=0$。则
> $$F_x=-yz,\quad F_y=-xz,\quad F_z=e^z-xy$$
> 所以
> $$z_x=\frac{yz}{e^z-xy},\qquad z_y=\frac{xz}{e^z-xy}$$
> 对 $z_x$ 再对 $x$ 求导：
> $$z_{xx}=\frac{2y^2z}{(e^z-xy)^2}-\frac{e^z y^2 z^2}{(e^z-xy)^3}$$

**第 9 题**

> 对方程组对 $x$ 求导：
> $$2x-2u u_x-2v v_x=0$$
> $$2x+4u u_x+6v v_x=0$$
> 化简得
> $$u u_x+v v_x=x,\qquad 2u u_x+3v v_x=-x$$
> 解得
> $$u_x=\frac{4x}{u},\qquad v_x=-\frac{3x}{v}$$

**第 10 题**

> $$\nabla f=(2xy,\ x^2-3y^2)$$
> 在 $(1,-1)$ 处：
> $$\nabla f(1,-1)=(-2,-2)$$
> 所以增长最快方向为
> $$\frac{1}{\sqrt{2}}(-1,-1)$$
> 最大增长率为
> $$|\nabla f(1,-1)|=2\sqrt{2}$$

**第 11 题**

> $$\nabla f=(2x,4y,6z)$$
> 在 $(1,1,1)$ 处，$\nabla f=(2,4,6)$。方向 $(1,2,2)$ 的单位向量是 $(1/3,2/3,2/3)$，因此
> $$\frac{\partial f}{\partial l}=\nabla f\cdot \mathbf l=2\cdot\frac{1}{3}+4\cdot\frac{2}{3}+6\cdot\frac{2}{3}=\frac{22}{3}$$

**第 12 题**

> 设等值线为 $f(x,y)=c$。沿曲线运动时 $df=0$，即
> $$f_x\,dx+f_y\,dy=0$$
> 这说明梯度 $\nabla f=(f_x,f_y)$ 与等值线的切向量 $(dx,dy)$ 垂直。
>
> 因而在 $\nabla f(x_0,y_0)\neq 0$ 时，梯度与过该点的等值线**垂直**。例如 $f=x^2+y^2$ 的等值线是圆，梯度 $(2x,2y)$ 正是圆的法向量。

---

## 第三部分：傅里叶级数（约 90 分钟）

### 1. 先回答学生的疑问：傅里叶级数 vs 傅里叶变换

| | 傅里叶级数（Fourier Series） | 傅里叶变换（Fourier Transform） |
|---|---|---|
| **适用对象** | 周期函数 $f(x+T)=f(x)$ | 非周期函数（或周期函数取 $T\to\infty$） |
| **分解结果** | 离散频率分量 $\{n\omega_0\}$ | 连续频谱 $\hat{f}(\omega)$ |
| **公式** | $f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty}(a_n\cos n\omega x + b_n\sin n\omega x)$ | $\hat{f}(\omega) = \int_{-\infty}^{+\infty} f(x)e^{-i\omega x}dx$ |
| **课程归属** | 微积分/数学分析 | 数学物理方法/信号处理 |
| **教材位置** | 本书第十一章 §8（p.292） | 本书未涉及 |

**建议讲解方式：** 先讲傅里叶级数，最后用 5 分钟点明傅里叶变换是"把周期推向无穷"的推广，激发兴趣即可，不需要深入。

### 2. 从"用简单函数逼近复杂函数"引入

回顾学生已有的知识链条：

$$\text{Taylor 展开} \xrightarrow{\text{多项式逼近}} \text{局部近似}$$

现在换一个思路：

$$\text{Fourier 展开} \xrightarrow{\text{三角函数逼近}} \text{全局近似}$$

**核心思想：** 任何（满足一定条件的）周期函数，都可以表示为不同频率的正弦波和余弦波的叠加。

**类比：** 白光通过三棱镜分解为不同颜色的光——傅里叶分析就是把函数"分解"为不同频率的"波"。

### 3. 傅里叶级数的定义

设 $f(x)$ 以 $2\pi$ 为周期，在 $[-\pi, \pi]$ 上可积，则：

$$f(x) \sim \frac{a_0}{2} + \sum_{n=1}^{\infty}(a_n \cos nx + b_n \sin nx)$$

其中 Fourier 系数为：

$$a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\cos nx\, dx, \quad n = 0, 1, 2, \ldots$$

$$b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\sin nx\, dx, \quad n = 1, 2, 3, \ldots$$

**关键问题：** " $\sim$ "什么时候能换成" $=$ "？

### 4. 收敛定理（Dirichlet 条件）

> **定理**（教材 p.295 附近）：若 $f(x)$ 在 $[-\pi,\pi]$ 上满足：
>
> 1. 连续或仅有有限个第一类间断点
> 2. 只有有限个极值点
>
> 则 Fourier 级数处处收敛，且
> $$\frac{a_0}{2} + \sum_{n=1}^{\infty}(a_n\cos nx + b_n\sin nx) = \frac{f(x^+)+f(x^-)}{2}$$

**注意：** 在连续点收敛到 $f(x)$，在间断点收敛到左右极限的平均值。

### 4+. 收敛定理的证明（Dirichlet 定理）

> 以下证明供教师参考，对学生而言难度较大，可视情况选讲。

#### 第一步：引入 Dirichlet 核

Fourier 级数的第 $N$ 阶部分和为：

$$S_N(x) = \frac{a_0}{2} + \sum_{n=1}^{N}(a_n\cos nx + b_n\sin nx)$$

将 $a_n$, $b_n$ 的积分公式代入，交换求和与积分：

$$S_N(x) = \frac{1}{\pi}\int_{-\pi}^{\pi} f(t)\left[\frac{1}{2} + \sum_{n=1}^{N}\cos n(t-x)\right]dt$$

定义 **Dirichlet 核**：

$$D_N(u) = \frac{1}{2} + \sum_{n=1}^{N}\cos nu$$

于是 $S_N(x) = \frac{1}{\pi}\displaystyle\int_{-\pi}^{\pi} f(t)D_N(t-x)\,dt$。

#### 第二步：Dirichlet 核的封闭形式

**引理**：$D_N(u) = \dfrac{\sin\left(N+\frac{1}{2}\right)u}{2\sin\frac{u}{2}}$（当 $u \neq 2k\pi$ 时）

> **证明：** 利用等比数列求和。
>
> $$2\sin\frac{u}{2}\cdot D_N(u) = \sin\frac{u}{2} + 2\sum_{n=1}^{N}\sin\frac{u}{2}\cos nu$$
>
> 由积化和差 $2\sin A\cos B = \sin(A+B) + \sin(A-B)$：
>
> $$= \sin\frac{u}{2} + \sum_{n=1}^{N}\left[\sin\left(n+\frac{1}{2}\right)u - \sin\left(n-\frac{1}{2}\right)u\right]$$
>
> 这是**望远镜求和**（telescoping sum），中间项全部抵消：
>
> $$= \sin\frac{u}{2} + \sin\left(N+\frac{1}{2}\right)u - \sin\frac{u}{2} = \sin\left(N+\frac{1}{2}\right)u$$
>
> $$\boxed{D_N(u) = \frac{\sin\left(N+\frac{1}{2}\right)u}{2\sin\frac{u}{2}}}$$

**Dirichlet 核的性质：**

- $\displaystyle\frac{1}{\pi}\int_{-\pi}^{\pi}D_N(u)\,du = 1$（令 $f \equiv 1$ 即得）
- $D_N(u)$ 是偶函数
- 当 $N\to\infty$ 时，$D_N(u)$ 在 $u\neq 0$ 处"快速振荡"，贡献趋于 0；但在 $u=0$ 附近有一个越来越窄但越来越高的"峰"

#### 第三步：将部分和改写为对称积分

利用 $D_N$ 的性质，对 $S_N(x)$ 做变量替换 $u = t - x$：

$$S_N(x) = \frac{1}{\pi}\int_{-\pi}^{\pi}f(x+u)D_N(u)\,du$$

减去 $\frac{f(x^+)+f(x^-)}{2}$（我们要证明的目标差值）：

$$S_N(x) - \frac{f(x^+)+f(x^-)}{2} = \frac{1}{\pi}\int_{-\pi}^{\pi}\left[f(x+u) - \frac{f(x^+)+f(x^-)}{2}\right]D_N(u)\,du$$

利用 $D_N$ 是偶函数，将积分拆成 $[0,\pi]$ 和 $[-\pi,0]$：

$$= \frac{1}{\pi}\int_0^{\pi}\left[f(x+u)+f(x-u)-f(x^+)-f(x^-)\right]D_N(u)\,du$$

记 $g(u) = f(x+u) + f(x-u) - f(x^+) - f(x^-)$，我们需要证明：

$$\frac{1}{\pi}\int_0^{\pi} g(u) \cdot \frac{\sin\left(N+\frac{1}{2}\right)u}{2\sin\frac{u}{2}}\,du \xrightarrow{N\to\infty} 0$$

#### 第四步：Riemann-Lebesgue 引理

> **引理（Riemann-Lebesgue）：** 若 $h \in L^1[a,b]$，则 $\displaystyle\int_a^b h(u)\sin\lambda u\,du \to 0$（$\lambda\to\infty$）。
>
> **完整证明（三步走）：**
>
> **第一步：对特征函数验证。**
>
> 设 $h(u) = \chi_{[\alpha,\beta]}(u)$（区间 $[\alpha,\beta]$ 上的特征函数），则：
> $$\int_a^b \chi_{[\alpha,\beta]}(u)\sin\lambda u\,du = \int_\alpha^\beta \sin\lambda u\,du = \frac{-\cos\lambda u}{\lambda}\bigg|_\alpha^\beta = \frac{\cos\lambda\alpha - \cos\lambda\beta}{\lambda}$$
>
> 由 $|\cos\theta| \leq 1$：
> $$\left|\int_a^b \chi_{[\alpha,\beta]}(u)\sin\lambda u\,du\right| \leq \frac{2}{\lambda} \to 0 \quad (\lambda\to\infty)$$
>
> **第二步：对阶梯函数验证。**
>
> 设 $h(u) = \sum_{k=1}^{m} c_k \chi_{[\alpha_k,\beta_k]}(u)$，由线性性：
> $$\int_a^b h(u)\sin\lambda u\,du = \sum_{k=1}^{m} c_k \int_{\alpha_k}^{\beta_k}\sin\lambda u\,du$$
>
> 每一项趋于 0，有限和也趋于 0。
>
> **第三步：用稠密性过渡到一般 $L^1$ 函数。**
>
> 对任意 $h \in L^1[a,b]$ 和任意 $\varepsilon > 0$，由阶梯函数在 $L^1[a,b]$ 中稠密，存在阶梯函数 $\varphi$ 使得：
> $$\int_a^b |h(u) - \varphi(u)|\,du < \frac{\varepsilon}{2}$$
>
> 于是：
> $$\left|\int_a^b h(u)\sin\lambda u\,du\right| \leq \left|\int_a^b \varphi(u)\sin\lambda u\,du\right| + \int_a^b |h(u)-\varphi(u)|\cdot|\sin\lambda u|\,du$$
>
> 第二步中已证：存在 $\Lambda$ 使得 $\lambda > \Lambda$ 时第一项 $< \frac{\varepsilon}{2}$。第二项由 $|\sin\lambda u| \leq 1$：
> $$\leq \frac{\varepsilon}{2} + \int_a^b|h(u)-\varphi(u)|\,du < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$$
>
> 因此 $\displaystyle\int_a^b h(u)\sin\lambda u\,du \to 0$（$\lambda\to\infty$）。$\blacksquare$
>
> **直觉理解：** 当 $\lambda$ 很大时，$\sin\lambda u$ 振荡极快，正负部分几乎抵消。$h(u)$ 在每个微小区间内近似为常数，而 $\sin\lambda u$ 在该区间上的积分近似为 0。

#### 第五步：完成证明

将积分改写为：

$$\frac{1}{\pi}\int_0^{\pi} g(u) \cdot \frac{\sin\left(N+\frac{1}{2}\right)u}{2\sin\frac{u}{2}}\,du = \frac{1}{\pi}\int_0^{\pi} \frac{g(u)}{2\sin\frac{u}{2}} \cdot \sin\left(N+\tfrac{1}{2}\right)u\,du$$

关键观察：在 Dirichlet 条件下（$f$ 有有限个第一类间断点和有限个极值点），$x$ 是**固定的**。

- 当 $u \to 0^+$ 时，$g(u) = [f(x+u)-f(x^+)] + [f(x-u)-f(x^-)]$，由单侧极限存在，$g(u) \to 0$
- 更进一步，Dirichlet 条件保证了 $\frac{g(u)}{2\sin\frac{u}{2}}$ 在 $[0,\pi]$ 上**可积**（间断点是可去奇点或有限跳跃，不影响可积性）

记 $h(u) = \frac{g(u)}{2\sin\frac{u}{2}}$，则 $h \in L^1[0,\pi]$。由 Riemann-Lebesgue 引理：

$$\int_0^{\pi} h(u)\sin\left(N+\tfrac{1}{2}\right)u\,du \to 0 \quad (N\to\infty)$$

因此 $S_N(x) \to \dfrac{f(x^+)+f(x^-)}{2}$。$\blacksquare$

#### 证明思路总结

```text
Fourier 部分和 S_N(x)
  │
  ├── 代入系数公式，引入 Dirichlet 核 D_N(u)
  │
  ├── 利用 D_N 的封闭形式（望远镜求和）
  │
  ├── 减去目标值，改写为 ∫ g(u)·D_N(u) du
  │
  ├── 将 D_N(u) 的振荡部分 sin((N+½)u) 分离
  │
  └── Riemann-Lebesgue 引理 → 积分趋于 0
```

### 5. 经典例题

#### 例题 1：方波的傅里叶展开

设 $f(x)$ 以 $2\pi$ 为周期，在 $(-\pi,\pi)$ 上 $f(x) = \begin{cases} 1, & 0 < x < \pi \\ -1, & -\pi < x < 0 \end{cases}$

> **计算过程：**
>
> $f(x)$ 是奇函数 $\Rightarrow$ 所有 $a_n = 0$
>
> $$b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\sin nx\, dx = \frac{2}{\pi}\int_0^{\pi}\sin nx\, dx = \frac{2}{n\pi}(1-\cos n\pi)$$
>
> $$b_n = \begin{cases} \frac{4}{n\pi}, & n \text{ 奇} \\ 0, & n \text{ 偶} \end{cases}$$
>
> 故 $f(x) = \frac{4}{\pi}\left(\sin x + \frac{1}{3}\sin 3x + \frac{1}{5}\sin 5x + \cdots\right)$

**教学建议：** 可以用图像展示取前 $N$ 项的部分和 $S_N(x)$ 如何逐步逼近方波，并指出 Gibbs 现象（在间断点附近始终有过冲，约 $9\%$）。

#### 例题 2：锯齿波

设 $f(x) = x$，$x \in (-\pi, \pi)$，以 $2\pi$ 为周期延拓。

> $f(x)$ 是奇函数，$a_n = 0$
>
> $$b_n = \frac{2}{\pi}\int_0^{\pi} x\sin nx\, dx = \frac{2}{\pi}\left[\frac{-x\cos nx}{n}\Big|_0^{\pi} + \frac{1}{n}\int_0^{\pi}\cos nx\, dx\right] = (-1)^{n+1}\frac{2}{n}$$
>
> 故 $x = 2\left(\sin x - \frac{1}{2}\sin 2x + \frac{1}{3}\sin 3x - \cdots\right)$，$x \in (-\pi, \pi)$

### 6. 正弦余弦函数系的正交性（ε-δ 在这里也有体现）

Fourier 系数公式的基础是三角函数系的**正交性**：

$$\int_{-\pi}^{\pi}\cos mx\cos nx\, dx = \begin{cases} 0, & m \neq n \\ \pi, & m = n \neq 0 \end{cases}$$

$$\int_{-\pi}^{\pi}\sin mx\sin nx\, dx = \begin{cases} 0, & m \neq n \\ \pi, & m = n \end{cases}$$

$$\int_{-\pi}^{\pi}\cos mx\sin nx\, dx = 0$$

> **证明要点（以第一个为例，当 $m \neq n$ 时）：**
>
> 利用积化和差：$\cos mx\cos nx = \frac{1}{2}[\cos(m+n)x + \cos(m-n)x]$
>
> $$\int_{-\pi}^{\pi}\cos mx\cos nx\, dx = \frac{1}{2}\left[\frac{\sin(m+n)x}{m+n} + \frac{\sin(m-n)x}{m-n}\right]_{-\pi}^{\pi} = 0$$

**类比：** 这和线性代数中向量的正交分解是完全一样的结构——$\{1, \cos x, \sin x, \cos 2x, \sin 2x, \ldots\}$ 就是函数空间的一组"正交基"。

### 7. 有限区间上的傅里叶展开（教材 §8.3，p.299）

实际问题中函数定义在有限区间 $[0, L]$ 上，有两种延拓方式：

- **奇延拓**（Fourier 正弦级数）：$f(x) = \sum_{n=1}^{\infty} b_n \sin\frac{n\pi x}{L}$
- **偶延拓**（Fourier 余弦级数）：$f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} a_n \cos\frac{n\pi x}{L}$

### 8. 选讲：从傅里叶级数到傅里叶变换（5 分钟概览）

令周期 $T \to \infty$，求和变成积分，离散频率 $n\omega_0$ 变成连续频率 $\omega$：

$$f(x) = \frac{1}{2\pi}\int_{-\infty}^{+\infty} \hat{f}(\omega) e^{i\omega x}\, d\omega$$

$$\hat{f}(\omega) = \int_{-\infty}^{+\infty} f(x) e^{-i\omega x}\, dx$$

这就是**傅里叶变换**。学生将来在数学物理方法或信号处理课程中会系统学习。

### 9. 课堂练习

1. 求 $f(x) = x^2$（$x \in [-\pi,\pi]$，周期 $2\pi$）的 Fourier 级数，并由此证明 $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2} = \frac{\pi^2}{6}$。
2. 将 $f(x) = 1$（$0 < x < \pi$）分别展开为正弦级数和余弦级数。
3. 设 $f(x) = |\sin x|$，判断其 Fourier 级数是否点点收敛到 $f(x)$，为什么？

#### 课堂练习解答

**第 1 题**

> $f(x)=x^2$ 是偶函数，所以 $b_n=0$。计算系数：
> $$a_0=\frac{1}{\pi}\int_{-\pi}^{\pi}x^2\,dx=\frac{2\pi^2}{3}$$
> $$a_n=\frac{1}{\pi}\int_{-\pi}^{\pi}x^2\cos nx\,dx=\frac{2}{\pi}\int_0^{\pi}x^2\cos nx\,dx=\frac{4(-1)^n}{n^2}$$
> 因而
> $$x^2=\frac{\pi^2}{3}+4\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2}\cos nx$$
> 在 $x=\pi$ 处取值，得到
> $$\pi^2=\frac{\pi^2}{3}+4\sum_{n=1}^{\infty}\frac{1}{n^2}$$
> 所以
> $$\sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{\pi^2}{6}$$

**第 2 题**

> 在 $(0,\pi)$ 上作半区间展开。
>
> 正弦级数：
> $$b_n=\frac{2}{\pi}\int_0^{\pi}\sin nx\,dx=\frac{2}{\pi}\cdot\frac{1-\cos n\pi}{n}$$
> 所以偶数项为 0、奇数项为 $\frac{4}{n\pi}$，即
> $$1=\frac{4}{\pi}\left(\sin x+\frac{1}{3}\sin 3x+\frac{1}{5}\sin 5x+\cdots\right)$$
>
> 余弦级数：
> $$a_0=\frac{2}{\pi}\int_0^{\pi}1\,dx=2,\qquad a_n=\frac{2}{\pi}\int_0^{\pi}\cos nx\,dx=0$$
> 因而余弦级数就是
> $$1=\frac{a_0}{2}=1$$

**第 3 题**

> $|\sin x|$ 是周期函数，而且连续、分段光滑，只在 $x=k\pi$ 处有折点，没有跳跃间断点。它满足 Dirichlet 条件，所以 Fourier 级数在每一点都收敛；由于函数连续，收敛值就是函数值本身。
>
> 因而其 Fourier 级数**点点收敛到** $|\sin x|$。
