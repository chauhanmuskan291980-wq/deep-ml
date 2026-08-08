def poly_term_derivative(c: float, x: float, n: float) -> float:
    equction = c*x**n 
    derivative = float(c*(n)*x**(n-1))
    return derivative