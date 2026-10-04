# Statistics and Big Data Analysis

2026 秋冬统计与大数据分析。

## 作业

| 作业 | 内容 |
| --- | --- |
| [hw1.ipynb](hw1.ipynb) | 第一次作业：用 matplotlib 画一张有 x 轴和 y 轴的图，并用 Markdown 单元解释。共三张图：标准正态分布的概率密度曲线、大样本直方图与理论密度的对比、以及用三次 Bézier 曲线画的"奶龙"（整活图） |
| [hw2.ipynb](hw2.ipynb) | 第二次作业（L2）：条件概率与 Monte Carlo。解析计算 $P(A\mid B)=1/4$，用频率之比 $K_{AB}/K_B$ 做模拟估计，比较 $N=10^2\sim10^5$ 的收敛与波动（$\mathrm{sd}\approx1.299/\sqrt{N}$），并解释为什么增加 $N$ 不保证每次都更接近真值 |

## 环境

作业在 Jupyter Notebook 中完成，使用仓库根目录下的 `.venv`（Python 3.14，依赖统一用 uv 管理）。
`matplotlib`、`numpy` 已列在 `pyproject.toml` 中，Jupyter 相关包按需装进 `.venv`：

```bash
# 在仓库根目录执行
uv pip install --python .venv/Scripts/python.exe jupyter ipykernel

# 打开作业（可直接看到已保存的图形输出；想从头跑一遍用 Kernel → Restart & Run All）
.venv/Scripts/python.exe -m jupyter notebook statistics_big_data/hw1.ipynb
```
