#pragma once

#include <cstddef>
#include <iosfwd>
#include <string>
#include <vector>

namespace na {

using Real = double;
using Vec = std::vector<Real>;
using Mat = std::vector<Vec>;
using Row = std::vector<std::string>; // a table row whose cells are already formatted

enum class TableStyle {
    Plain, // column-aligned text
    LaTeX, // body rows only, "a & b \\"
};

/// Print `rows` as a table. Plain output pads each column to its widest cell, at
/// least `width` characters; LaTeX output leaves the tabular environment to the
/// caller.
void print_table(std::ostream& out, const std::vector<std::string>& header,
                 const std::vector<Row>& rows, TableStyle style = TableStyle::Plain,
                 int width = 12);

/// Same, formatting each numeric cell with `precision` significant digits.
void print_table(std::ostream& out, const std::vector<std::string>& header,
                 const std::vector<Vec>& rows, TableStyle style = TableStyle::Plain,
                 int precision = 6, int width = 12);

/// Same, writing to stdout.
void print_table(const std::vector<std::string>& header, const std::vector<Row>& rows,
                 TableStyle style = TableStyle::Plain, int width = 12);
void print_table(const std::vector<std::string>& header, const std::vector<Vec>& rows,
                 TableStyle style = TableStyle::Plain, int precision = 6, int width = 12);

} // namespace na
