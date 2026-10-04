#include "na/fpn.hpp"

#include <cmath>
#include <sstream>

namespace na {
namespace {

long long int_power(int beta, int k) {
    long long result = 1;
    for (int i = 0; i < k; ++i) {
        result *= beta;
    }
    return result;
}

// The p digits of M as "d0.d1d2...", left-padded with zeros.
std::string format_digits(long long M, int beta, int p) {
    std::string digits(static_cast<std::size_t>(p), '0');
    for (int i = p - 1; i >= 0; --i) {
        digits[static_cast<std::size_t>(i)] = static_cast<char>('0' + M % beta);
        M /= beta;
    }
    return digits.substr(0, 1) + "." + digits.substr(1);
}

} // namespace

double FpnSystem::power(int e) const { return std::pow(static_cast<double>(beta), e); }

double FpnSystem::ufl() const { return power(L); }

double FpnSystem::ofl() const {
    return power(U) * (static_cast<double>(beta) - machine_precision());
}

double FpnSystem::machine_precision() const { return std::pow(static_cast<double>(beta), 1 - p); }

double FpnSystem::unit_roundoff() const { return 0.5 * machine_precision(); }

long long FpnSystem::nonzero_count() const {
    const long long mantissas = int_power(beta, p - 1) * (beta - 1);
    return 2 * mantissas * (U - L + 1);
}

long long FpnSystem::cardinality() const { return nonzero_count() + 1; }

std::string FpnSystem::describe() const {
    std::ostringstream out;
    out << "F(beta = " << beta << ", p = " << p << ", L = " << L << ", U = " << U << ")";
    return out.str();
}

double Fpn::value(const FpnSystem& sys) const {
    return sign * static_cast<double>(mantissa) * sys.power(exponent - sys.p + 1);
}

std::string Fpn::str(const FpnSystem& sys) const {
    std::ostringstream out;
    if (sign < 0) {
        out << '-';
    }
    if (subnormal) {
        // Definition 1.15: the mantissa is m in (0, 1), written "0.d1d2...".
        std::string digits(static_cast<std::size_t>(sys.p) - 1, '0');
        long long M = mantissa;
        for (int i = sys.p - 2; i >= 0; --i) {
            digits[static_cast<std::size_t>(i)] = static_cast<char>('0' + M % sys.beta);
            M /= sys.beta;
        }
        out << "0." << digits << " x " << sys.beta << "^" << exponent;
    } else {
        out << format_digits(mantissa, sys.beta, sys.p) << " x " << sys.beta << "^" << exponent;
    }
    return out.str();
}

std::string Fpn::latex(const FpnSystem& sys) const {
    const std::string plain = str(sys);
    const std::string marker = " x " + std::to_string(sys.beta) + "^";
    const std::size_t at = plain.find(marker);
    const std::string significand = at == std::string::npos ? plain : plain.substr(0, at);
    const std::string exponent = at == std::string::npos ? "0" : plain.substr(at + marker.size());
    return "$" + significand + " \\times " + std::to_string(sys.beta) + "^{" + exponent + "}$";
}

std::vector<Fpn> normalized(const FpnSystem& sys) {
    std::vector<Fpn> result;
    const long long low = int_power(sys.beta, sys.p - 1);
    const long long high = int_power(sys.beta, sys.p);
    for (int e = sys.L; e <= sys.U; ++e) {
        for (long long M = low; M < high; ++M) {
            result.push_back(Fpn{1, M, e, false});
        }
    }
    return result;
}

std::vector<Fpn> subnormals(const FpnSystem& sys) {
    std::vector<Fpn> result;
    const long long high = int_power(sys.beta, sys.p - 1);
    for (long long M = 1; M < high; ++M) {
        result.push_back(Fpn{1, M, sys.L, true});
    }
    return result;
}

std::vector<Fpn> extended(const FpnSystem& sys) {
    std::vector<Fpn> result = subnormals(sys);
    for (const Fpn& x : normalized(sys)) {
        result.push_back(x);
    }
    return result;
}

} // namespace na
