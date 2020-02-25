""" Write a Python module newtonraphson.py that contains functions to
find the roots of an equation for a polynomial in x using the 
Newton-Raphson method. 

Coefficients should be an iterable (tuple or list) of coefficients 
for the powers of x.  As an example:

    7𝑥^4 + 3𝑥^3 − 5𝑥^2 + 32𝑥 − 7𝑥^0 = 0

    would be represented as [7, 3,−5, 32,−7].    
    Show the answers for the equation above given 
    starting points of x=5 and x = -50:

    NewtonRaphson( [7, 3, -5, 32, -7], 5) and 
    NewtonRaphson( [7, 3, -5, 32, -7], -50)

Note that only real roots will be returned when we start the search 
with a real value.  YOU MAY NOT USE ANY library functions for taking 
derivatives or evaluating polynomials.

"""


# Solution Function

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

    # eps_step = 1e-5;
    # eps_abs = 1e-5;
    # N = 100;
    # x = 0.2;

    # for i=1:N
    #     xn = x - cos(x)/( -sin(x) );

    #     if abs( x - xn ) < eps_step && abs( cos( xn ) ) < eps_abs
    #     break;
    #     elseif i == N
    #     error( 'Newton\'s method did not converge' );
    #     end

    #     x = xn;
    # end

    # xn
    
    original = polyval(fpoly, a)
    deriv = polyval(derivative(fpoly), a)
    
    b = a - (original / deriv)
    h = 0
    for i in range(n):
      original = polyval(fpoly, a + h)
      deriv = polyval(derivative(fpoly), a + h)

      xn = (a + h) - (original / deriv)

      if abs(x - xn) < tolerance and abs()

      new_b = (a + h) - (original / deriv)
      diff = b - new_b
      if abs(diff) < tolerance or a + h > N:
          raise Exception("No root found")
      b = new_b
      print(h)
      h += 1
    return (a + h)

# Auxillary Functions

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
    for i, c in enumerate(fpoly, 1):
        val += c * x ** (len(fpoly) - i)

    print(val)
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
    deriv = [c * (len(fpoly) - i) for i, c in enumerate(fpoly, 1)]

    print(deriv[0:-1])
    return deriv[0:-1]

if __name__ == '__main__':
  print(NewtonRaphson([1, -1, 2], -20))
