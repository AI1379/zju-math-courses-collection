# ZJU Math Courses Collections

数院的一些课程的讲义和作业合集。

## Common

常见 LaTeX 模板。包含 [common/macros.tex](common/macros.tex)，定义了常用的数学算子、矩阵缩写和作业环境。

在作业中可以通过 `\input{../../common/macros.tex}` 引用。注意这里依赖了 LuaLaTeX 读取环境变量。

## Scripts

- `flatten_tex.py`: 用于将 .tex 文件中的 `\input` 特性展开，生成独立的 .tex 文件。

    ```bash
    python flatten_tex.py <input.tex> [output.tex]
    ```

## Numeric Algebra

2026 春夏数值代数

## Numerical Analysis

2026 秋冬数值分析。作业用 C++ 实现，目录下带 CMake 构建和 clangd 配置，
详见 [numerical_analysis/README.md](numerical_analysis/README.md)。

## Complex Analysis

2026 春夏复变函数

## Probability

2026 秋冬概率论。第一章作业见 [probability/chapter1.tex](probability/chapter1.tex)。

## Statistics and Big Data Analysis

2026 秋冬统计与大数据分析。第一次作业（Jupyter + matplotlib 绘图）见
[statistics_big_data/hw1.ipynb](statistics_big_data/hw1.ipynb)，
第二次作业（条件概率与 Monte Carlo）见 [statistics_big_data/hw2.ipynb](statistics_big_data/hw2.ipynb)。
