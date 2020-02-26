def NewtonRaphson(fpoly, a, tolerance=.00001):
    """Given a set of polynomial coefficients fpoly
    for a univariate polynomial function,
    e.g. (3, 6, 0, -24) for 3x^3 + 6x^2 +0x^1 -24x^0,
    find the real roots of the polynomial (if any)
    using the Newton-Raphson method.

    a is the initial estimate of the root and
    starting state of the search.

    This is an iterative method that stops when the
    change in estimators is less than tolerance.
"""
    # Calculate b (x-intercept) of line tangent to fpoly
    # Using approximate value a
    b = a - polyval(fpoly, a) / polyval(derivative(fpoly), a)

    # While the difference between estimators is greater than tolerance
    # continue to utilize x_n+1 as new estimator
    while abs(a - b) >= tolerance:
        a = b
        b = a - polyval(fpoly, a) / polyval(derivative(fpoly), a)

    # Once tolerance is met, return last estimator
    return b


""" Auxillary Functions """


def polyval(fpoly, x):
    """polyval(fpoly, x)
    Given a set of polynomial coefficients from highest order to x^0,
    compute the value of the polynomial at x.  We assume zero
    coefficients are present in the coefficient list/tuple.

    Example:  f(x) = 4x^3 + 0x^2 + 9x^1 + 3 evaluated at x=5
    polyval([4, 0, 9, 3], 5))
    returns 548
    """
    val = 0
    p = 10

    # Find sum of each term when plugging in x
    for i, c in enumerate(fpoly, 1):
        val += c * (x ** (len(fpoly) - i))

    return val


def derivative(fpoly):
    """derivative(fpoly)
    Given a set of polynomial coefficients from highest order to x^0,
    compute the derivative polynomial.  We assume zero coefficients
    are present in the coefficient list/tuple.

    Returns polynomial coefficients for the derivative polynomial.
    Example:
    derivative((3,4,5))  # 3 * x**2 + 4 * x**1 + 5 * x**0
    returns:  [6, 4]     # 6 * x**1 + 4 * x**0
    """
    # Find derivative by looping through fpoly and multiplying the coefficient
    # by the respective index starting at 1
    deriv = [c * (len(fpoly) - i) for i, c in enumerate(fpoly, 1)]

    # Return slice of derivative, removing 0 term
    return deriv[0:2]


if __name__ == '__main__':
    print(NewtonRaphson([4, 0, -1], -1))
    print(NewtonRaphson([4, 0, -1], 1))
