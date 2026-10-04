# Numerical Analysis

2026 秋冬数值分析。作业要求用 C++ 实现，所以这里是仓库里唯一带构建系统的课程目录。

## 环境

本机已就绪（都是 scoop / winget 装的，装在 PATH 上）：

| 工具 | 用途 |
| --- | --- |
| `clang++` (LLVM 21) | 编译器。自动探测 MSVC 头文件和 Windows SDK，无需 `vcvarsall` |
| `cmake` + `ninja` | 构建。Ninja 是必需的，本机没有 `make` |
| `clangd` | 编辑器补全、跳转、诊断 |
| `clang-format` | 代码格式化 |
| `lualatex` + `latexmk` | 编译 `report.tex`（依赖 `common/macros.tex` 里的 Lua） |

## 构建

首次配置一次即可，之后只要 build：

```bash
cd numerical_analysis
cmake --preset default        # 配置，生成 build/ 和 compile_commands.json
cmake --build --preset default
./build/hw1/hw1.exe
```

`CMakePresets.json` 已经把工具链固定成 clang++ + Ninja，并打开了
`CMAKE_EXPORT_COMPILE_COMMANDS`。

不指定生成器时 CMake 会默认选用 Visual Studio 生成器（走 MSVC，不是 clang++），
编译数据库的内容也会随之不同，所以请走 preset，别手敲 `cmake -S . -B build`。

## clangd

`numerical_analysis/.clangd` 把 clangd 指向 `build/compile_commands.json`，
头文件路径、C++ 标准、宏定义都由 CMake 导出，不需要在编辑器里另配。

**先配置一次再进行编辑**，否则 clangd 找不到编译数据库，会退化成
「找不到 `na/common.hpp`」之类的报错。改了 `CMakeLists.txt` 或新增源文件后重新
`cmake --preset default` 即可刷新。

注意 `.vscode/settings.json` 里设了 `cmake.sourceDirectory` 指向本目录，
那是给 VSCode 的 CMake Tools 用的；clangd 不依赖它，靠 `.clangd` 里的
`CompilationDatabase: build` 找编译数据库。

如果同时装了 Microsoft C/C++ 扩展，建议关掉它的 IntelliSense，
不然两套引擎会重复报错。仓库根目录的 `.vscode/settings.json` 里已经设好了
`"C_Cpp.intelliSenseEngine": "disabled"`（该文件被 gitignore，只对本地生效）。

## 目录结构

```
numerical_analysis/
├── CMakeLists.txt          # 顶层：自动收录所有 hw*/ 子目录
├── CMakePresets.json       # clang++ + Ninja 预设
├── .clangd                 # clangd 配置（编译数据库路径）
├── .clang-format           # 格式化规则（4 空格缩进，100 列）
├── common/                 # 跨作业复用的库，对应 na_common
│   ├── include/na/common.hpp   # 表格打印 (print_table)
│   ├── include/na/fpn.hpp      # 浮点数系统 F(beta, p, L, U) 的枚举与刻画量
│   └── src/
└── hw1/
    ├── CMakeLists.txt
    ├── main.cpp            # 作业程序
    ├── out/                # 程序生成的 LaTeX 片段，由 report.tex \input
    └── report.tex          # 作业报告
```

`common/` 的角色和 `numeric_algebra/common/` 一样，放复用的数值算法；
新算法加进 `common/src/`，在 `common/include/na/` 里声明。

## 新增一次作业

建 `hwN/`，放三个文件就够：

`hwN/CMakeLists.txt`

```cmake
add_executable(hw2 main.cpp)
target_link_libraries(hw2 PRIVATE na_common)
```

`hwN/main.cpp` 和 `hwN/report.tex`（`report.tex` 直接抄上一次的，
改掉 `\newcommand{\hwNum}{2}`）。

顶层 `CMakeLists.txt` 用 `CONFIGURE_DEPENDS` 自动收录 `hw*` 目录，
新目录不用手动注册，下次构建时自动生效。

## 报告

`report.tex` 沿用仓库其他课程的模板（LuaLaTeX + `\input{../../common/macros.tex}`）。
hw1 的做法是让程序把 LaTeX 片段写进 `hw1/out/`，报告直接 `\input` 它们，
这样报告里的表格和插图始终是程序真实算出来的，不用手工誊抄：

```cpp
// 生成一个完整的 tabular 环境
write_tabular(out_path("elements.tex"), {"值", "规格化形式"}, rows);
```

```latex
% report.tex 里这样引用
\begin{center}
  \input{out/elements.tex}
\end{center}
```

注意 `\input` 的文件末尾不要以 `\\` 结尾，否则后面的 `\hline` 会报
`Misplaced \noalign`；生成完整的 `tabular`（如上面的 `write_tabular`）
就不会有这个问题。

`na::print_table` 传 `na::TableStyle::LaTeX` 输出 `a & b \\` 形式的数据行，
传 `na::TableStyle::Plain` 输出对齐的纯文本，方便在终端里看。

### 把源码挂进报告

和 `numeric_algebra` 那边一样，用 `listings` 宏包把 C++ 源码直接列入报告，
不用手抄：

```latex
\usepackage{listings}
\usepackage{xcolor}

\lstset{
  language=C++,
  basicstyle=\ttfamily\small,
  keywordstyle=\bfseries\color{blue},
  commentstyle=\color{gray},
  stringstyle=\color{red},
  breaklines=true,
  showstringspaces=false,
  tabsize=4,
  frame=single,
  framesep=5pt,
  rulecolor=\color{gray},
  captionpos=b,
  numberstyle=\tiny\color{gray},
  numbers=left,
}
```

引用时路径相对 `report.tex` 所在目录：

```latex
\lstinputlisting[language=C++, caption={作业程序 main.cpp}]{main.cpp}
\lstinputlisting[language=C++, caption={FPN 系统 fpn.hpp}]{../common/include/na/fpn.hpp}
```

`breaklines=true` 让长行自动折行。中文出现在字符串字面量里也能正常渲染
（ctex 已加载），无需额外处理。

编译（先跑程序生成 `out/`）：

```bash
./build/hw1/hw1.exe && cd hw1 && latexmk -lualatex report.tex
```

### 页眉的姓名和学号

模板用 `\getEnv{NAME}{NAME}` 从环境变量取姓名和学号（见 `common/macros.tex`），
这样个人信息不进版本库。若变量没设置，页眉会渲染成字面量 `NAME(UID)`。

命令行构建靠用户级 `~/.latexmkrc` 注入这两个值（VSCode 全局设置里那对只对
它的 `lualatexmk` 这一个 tool 生效，命令行拿不到）：

```perl
use Encode qw(encode);
$ENV{NAME} = encode('cp936', '林江涛') unless defined $ENV{NAME};
$ENV{UID}  = '3240103365' unless defined $ENV{UID};
```

注意中文必须显式 `encode('cp936', ...)`：lualatex 按系统 ANSI 代码页（本机
CP936）解读环境变量的字节，直接写 UTF-8 会在 PDF 里渲染成乱码。
临时覆盖用 `env NAME=... UID=... latexmk ...`；注意 Git Bash 里 `UID` 是只读的，
不能写成 `UID=... latexmk` 的前缀形式。
