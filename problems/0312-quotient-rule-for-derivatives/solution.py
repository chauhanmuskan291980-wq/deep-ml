import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # 1. Evaluate g(x) and h(x) at the given point
    g_val = evaluate_polynomial(g_coeffs, x)
    h_val = evaluate_polynomial(h_coeffs, x)

    # 2. Find the coefficients for g'(x) and h'(x)
    g_prime_coeffs = differentiate_polynomial(g_coeffs)
    h_prime_coeffs = differentiate_polynomial(h_coeffs)

    # 3. Evaluate g'(x) and h'(x) at the given point
    g_prime_val = evaluate_polynomial(g_prime_coeffs, x)
    h_prime_val = evaluate_polynomial(h_prime_coeffs, x)

    # 4. Apply the quotient Rule formula
    # FIXED: Changed h_prime_coeffs to h_prime_val
    numerator = (g_prime_val * h_val) - (g_val * h_prime_val) 
    denominator = h_val ** 2

    return numerator / denominator


def evaluate_polynomial(coeffs, x):
    """Evaluates a polynomial at a given point x using Horner's method."""
    # FIXED: Corrected indentation to 4 spaces
    result = 0
    for coeff in coeffs:
        result = result * x + coeff
    return result


def differentiate_polynomial(coeffs):
    """Computes the coefficients of the derivative of a polynomial."""
    n = len(coeffs) - 1
    derived_coeffs = []
    for i, coeff in enumerate(coeffs[:-1]):
        derived_coeffs.append(coeff * (n - i))
    return derived_coeffs if derived_coeffs else [0]
