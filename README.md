# ZeroDivisionError in Python Function

This repository demonstrates a common Python error: ZeroDivisionError. The `bug.py` file contains a function that causes this error when called with a zero divisor. The `bugSolution.py` file provides a solution by adding error handling to prevent the error.

## Bug
The `my_function` function in `bug.py` does not handle the case where the divisor `b` is zero, resulting in a `ZeroDivisionError`. 

## Solution
The solution in `bugSolution.py` incorporates a `try-except` block to catch the `ZeroDivisionError`. If the error occurs, the function prints an error message instead of raising an exception.  Alternative solutions would include using the `math.isclose()` to check for near-zero values and returning an appropriate result. 