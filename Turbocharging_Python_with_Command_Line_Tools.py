#Turbocharging Python with Command-Line Tools
"""
1. Click Framework: For creating command-line interfaces.
2. Numba Framework: For Just in Time(JIT) compilation to speed up Python functions.
3. Python CUDA Framework: For GPU acceleration.
4. Scikit-learn: For machine learning capabilities.
 
 """
#Example: Using Numba JIT for Performance Boost
#1. Timing Decorator
# First, we define a decorator to measure the runtime of our functions.

# wraps is decorator from 'functools' module.It is used preserve the original function's
# metadata when it is decorated.This mean attributes like function's name and docstring
# are kept intact.

# 'f': This is the function that will be decorated. The decorator will wrap around this
#      function to add timing functionality.

# '@wrap(f)' : This decorator ensures that the metadata of the original function 'f' is
#              copied from the 'wrap' function.

# 'def wrap(*args, **kwargs)' : This inner function, 'wrap', is what we called instead of 'f'. It takes
#                               any positional ('*args') and keyword('**kwargs') arguments that the original
#                               function 'f' would take.

import time #Provides time related functions
from functools import wraps


def timing(f):
    @wraps(f) 
    def wrap(*args, **kwargs):
        ts = time.time() #time.time() to measure current time in seconds and store it.
        result = f(*args, **kwargs)
        te = time.time() #This variable stores the end time, which is current time after the function 'f' has
                         # finished executing.
        print(f"func: {f.__name__}, args: [{args}, {kwargs}] took: {te-ts} sec")
        return result
    return wrap

"""
@timing
def example_function(x,y):
    return x + y

#call the decorated function
z = example_function(3,4)
print("The sum of x and y: ",z)
"""
"""
O/P: (.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents$ /home/gauravmtwt1/Documents/git-demo/.venv/bin/python "/home/gauravmtwt1/Documents/Python for DevOps/revision_python09feb2024onward.py"
gauravmtwt1
func: example_function, args: [(3, 4), {}] took: 5.4836273193359375e-06 sec
The sum of x and y:  7
"""

#2. Numba JIT Decorator
# We apply the 'numba.jit' decorator with the 'nopython' argument set to 'True' to ensure
# the function is compiled to machine code.

# pip install numba

# numba: This is a Just-in-Time(JIT) compiler that translate a subset of Python and NumPy code
#        into fast machine code.

# @numba.jit(nopython=True): This decorator tells Numba to compile the function to machine
#                            code using the JIT compiler.
#'nopython=True': It means function should be compiled in "nopython" mode, meaning that Numba
#                 will generate machine code that does not rely on python interpreter, thus
#                 providing signficant speed improvements.

import numba

@timing
@numba.jit(nopython=True)
def expmean_jit(rea):
    """Perform multiple mean calculations"""
    val = rea.mean() ** 2 #Calculate the mean of the array 'rea' and squares it, storing the 
                          # the result in the variable 'val'.               
    return val
"""
#Example

import numpy as np

#Example array
rea = np.array([[1.0,420800.0,423500.0],
                [2.0, 542400.0, 546700.0],
                [3.0,70900.0,71200.0]], dtype=np.float32)
# call the decorated functions
result = expmean_jit(rea)
print("Result:",result)
"""
"""
O/P: (.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents$ /home/gauravmtwt1/Documents/git-demo/.venv/bin/python "/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Turbocharging_Python_with_Command_Line_Tools.py"
func: expmean_jit, args: [(array([[1.000e+00, 4.208e+05, 4.235e+05],
       [2.000e+00, 5.424e+05, 5.467e+05],
       [3.000e+00, 7.090e+04, 7.120e+04]], dtype=float32),), {}] took: 1.1071295738220215 sec
Result: 53181792049.82716
"""

