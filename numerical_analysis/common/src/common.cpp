#include "na/common.hpp"

#include <algorithm>
#include <iomanip>
#include <iostream>
#include <sstream>

namespace na {
namespace {

std::string render(Real value, int precision) {
    std::ostringstream text;
    text << std::setprecision(precision) << value;
    return text.str();
}

// Each column is as wide as its widest cell plus two spaces, and at least `width`.
std::vector<std::size_t> column_widths(const std::vector<std::string>& header,
                                       const std::vector<Row>& rows, int width) {
    std::vector<std::size_t> widths(header.size(), static_cast<std::size_t>(width));
    for (std::size_t i = 0; i < header.size(); ++i) {
        widths[i] = std::max(widths[i], header[i].size() + 2);
    }
    for (const Row& row : rows) {
        for (std::size_t i = 0; i < row.size() && i < widths.size(); ++i) {
            widths[i] = std::max(widths[i], row[i].size() + 2);
        }
    }
    return widths;
}

void write_plain(std::ostream& out, const std::vector<std::string>& header,
                 const std::vector<Row>& rows, const std::vector<std::size_t>& widths) {
    const auto write_row = [&out, &widths](const Row& row) {
        for (std::size_t i = 0; i < row.size() && i < widths.size(); ++i) {
            out << std::string(row[i].size() < widths[i] ? widths[i] - row[i].size() : 0, ' ')
                << row[i];
        }
        out << '\n';
    };

    write_row(header);
    for (std::size_t column : widths) {
        out << std::string(column, '-');
    }
    out << '\n';
    for (const Row& row : rows) {
        write_row(row);
    }
}

void write_latex(std::ostream& out, const std::vector<Row>& rows) {
    for (const Row& row : rows) {
        for (std::size_t i = 0; i < row.size(); ++i) {
            out << (i == 0 ? "" : " & ") << row[i];
        }
        out << " \\\\\n";
    }
}

} // namespace

void print_table(std::ostream& out, const std::vector<std::string>& header,
                 const std::vector<Row>& rows, TableStyle style, int width) {
    if (style == TableStyle::LaTeX) {
        write_latex(out, rows);
        return;
    }
    write_plain(out, header, rows, column_widths(header, rows, width));
}

void print_table(std::ostream& out, const std::vector<std::string>& header,
                 const std::vector<Vec>& rows, TableStyle style, int precision, int width) {
    std::vector<Row> text;
    text.reserve(rows.size());
    for (const Vec& row : rows) {
        Row cells;
        cells.reserve(row.size());
        for (Real value : row) {
            cells.push_back(render(value, precision));
        }
        text.push_back(std::move(cells));
    }
    print_table(out, header, text, style, width);
}

void print_table(const std::vector<std::string>& header, const std::vector<Row>& rows,
                 TableStyle style, int width) {
    print_table(std::cout, header, rows, style, width);
}

void print_table(const std::vector<std::string>& header, const std::vector<Vec>& rows,
                 TableStyle style, int precision, int width) {
    print_table(std::cout, header, rows, style, precision, width);
}

} // namespace na
