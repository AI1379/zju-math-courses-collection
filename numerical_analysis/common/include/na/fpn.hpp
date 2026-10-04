#pragma once

#include <string>
#include <vector>

namespace na {

/// A floating-point number system F(beta, p, L, U) of Definition 1.12. Elements are
/// +-M beta^E with beta^(p-1) <= M < beta^p, kept as integer mantissas so that
/// enumeration and membership tests stay exact.
struct FpnSystem {
    int beta = 2;
    int p = 3;
    int L = -1;
    int U = 1;

    double power(int e) const;

    double ufl() const;               // beta^L, Definition 1.19
    double ofl() const;               // beta^U (beta - beta^(1-p)), Definition 1.19
    double machine_precision() const; // beta^(1-p), Definition 1.18
    double unit_roundoff() const;     // half the machine precision, Definition 1.28

    long long nonzero_count() const;
    long long cardinality() const; // #F, Corollary 1.21

    std::string describe() const;
};

/// One element of a system.
struct Fpn {
    int sign = 1;
    long long mantissa = 0;
    int exponent = 0;
    bool subnormal = false; // added by Definition 1.15

    double value(const FpnSystem& sys) const;
    std::string str(const FpnSystem& sys) const;   // "1.01 x 2^0"
    std::string latex(const FpnSystem& sys) const; // "$1.01 \times 2^{0}$"
};

/// The elements with a positive sign, ordered by exponent then mantissa.
std::vector<Fpn> normalized(const FpnSystem& sys);
/// The subnormal numbers of Definition 1.15: e = L with mantissa m in (0, 1).
std::vector<Fpn> subnormals(const FpnSystem& sys);
/// The extended system: subnormals followed by the normalized elements.
std::vector<Fpn> extended(const FpnSystem& sys);

} // namespace na
