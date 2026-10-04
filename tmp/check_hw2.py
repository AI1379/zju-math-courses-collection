# -*- coding: utf-8 -*-
"""校验 hw2.ipynb：格式、数学公式 $ 配对、所有代码单元均已执行。"""
import nbformat

nb = nbformat.read("statistics_big_data/hw2.ipynb", as_version=4)
nbformat.validate(nb)
print("nbformat validate: OK")

n_md = n_code = 0
for i, c in enumerate(nb.cells):
    src = c.source
    if c.cell_type == "markdown":
        n_md += 1
        # 统计未转义的 $ 个数，应为偶数
        cnt, j = 0, 0
        while j < len(src):
            if src[j] == "\\":
                j += 2
                continue
            if src[j] == "$":
                cnt += 1
            j += 1
        if cnt % 2:
            print("WARN odd dollar count in markdown cell", i)
        if "待填" in src:
            print("WARN placeholder remains in cell", i)
    else:
        n_code += 1
        assert c.get("execution_count") is not None, f"code cell {i} not executed"

print(f"cells: {n_md} markdown + {n_code} code; all code cells executed")
print("total cells:", len(nb.cells))
