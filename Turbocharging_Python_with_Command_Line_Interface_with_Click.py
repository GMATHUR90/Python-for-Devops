# Command-Line Interface with Click

#Using Click, we can create a CLI command that allows us to run the function with or without
#JIT

import click
import numba
import numpy as np
import time
from functools import wraps

#Define the timing decorator

def timing(f):
    @wraps(f)
    def wrap(*args, **kwargs):  
        ts = time.time()
        result = f(*args, **kwargs)
        te = time.time()
        print(f"func: {f.__name__}, args: [{args},{kwargs}] took: {te-ts} sec")
        return result
    return wrap

# Define the function to create a simple array
def real_estate_array():
    # Creating a sample array with random numbers
    return np.random.rand(1000,1000).astype(np.float32)
#This function generates a 1000x1000 array of random float32 numbers to simulate real estate
# data

# Define the regular version of expmean

@timing
def expmean(rea):
    """Perform multiple mean calculations without JIT"""
    val = rea.mean() ** 2
    return val
# This is the non-JIT version of the function, decorated with the 'timing' decorator to measure
# its execution time.


# Define the JIT-compiled version of expmean
@timing
@numba.jit(nopython=True)
def expmean_jit(rea):
    """Perform multiple mean calculations with JIT"""
    val = rea.mean() ** 2
    return val
# This is the JIT-compiled version of the function, using Numba for optimization and also
# decorated with the 'timing' decorator.

# Define the CLI command using Click
@click.command
@click.option('--jit/--no-jit', default=False)
@click.option('--iterations', default=10, help='Number of iterations to run')
def jit_test(jit, iterations):
    rea = real_estate_array() #Initialize the array
    if jit:
        click.echo(click.style('Running with JIT', fg='green'))
        for _ in range(iterations):
            expmean_jit(rea)
    else:
        click.echo(click.style('Running NO JIT', fg='red'))
        for _ in range(iterations):
            expmean(rea) #Regular version of the function

# Entrypoint of the script
if __name__ == '__main__':
    jit_test

@click.command()
@click.option('--jit/--no-jit', default=False)
def jit_test(jit):
    rea = real_estate_array() # Assuming this function initializes the array
    if jit:
        click.echo(click.style('Running with JIT', fg='green'))
        expmean_jit(rea)
    else:
        click.echo(click.style('Running NO JIT', fg='red'))
        expmean(rea) #Regular version of the function

if __name__ == '__main__':
    jit_test()

"""
O/P:
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload$ python Turbocharging_Python_with_Command_Line_Interface_with_Click.py --no-jit
Running NO JIT
func: expmean, args: [(array([[0.6222017 , 0.29116824, 0.75004035, ..., 0.1673657 , 0.92112404,
        0.71150273],
       [0.38862473, 0.11667933, 0.8503344 , ..., 0.5071941 , 0.94329256,
        0.7693117 ],
       [0.04176548, 0.2622386 , 0.6732263 , ..., 0.3739553 , 0.05024098,
        0.48795897],
       ...,
       [0.9730357 , 0.04860296, 0.44037426, ..., 0.4806389 , 0.5505616 ,
        0.5194301 ],
       [0.24554905, 0.3035238 , 0.27687335, ..., 0.314904  , 0.61961913,
        0.7084576 ],
       [0.98229766, 0.08555766, 0.01296944, ..., 0.27698874, 0.8434139 ,
        0.09793457]], dtype=float32),),{}] took: 0.0005316734313964844 sec
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload$ python Turbocharging_Python_with_Command_Line_Interface_with_Click.py --jit
Running with JIT
func: expmean_jit, args: [(array([[0.39303678, 0.01924152, 0.95863134, ..., 0.30918205, 0.17745718,
        0.8958441 ],
       [0.9027833 , 0.6989918 , 0.83094996, ..., 0.83156323, 0.95567596,
        0.09647795],
       [0.2279758 , 0.23543786, 0.8085602 , ..., 0.9277576 , 0.4744672 ,
        0.16595455],
       ...,
       [0.8314101 , 0.9531228 , 0.6686256 , ..., 0.24319471, 0.73391163,
        0.29712427],
       [0.43262136, 0.3435728 , 0.5704595 , ..., 0.36457273, 0.9670207 ,
        0.70138097],
       [0.99508697, 0.783707  , 0.76394427, ..., 0.91403913, 0.6991258 ,
        0.81111205]], dtype=float32),),{}] took: 0.5215733051300049 sec

"""

