import numpy as np
from evaluate import evaluate_function, get_matrix
from gradient_descent import gradient_descent
import pandas as pd 

"""
f(x, y) = 100(y-x^2)^2 + (1 - x)^2
"""

MULTIPLICATION_REGULAR = r'(\d+(\.\d+)?)([a-z])'

MATRIX_REGEX =  r"(\[+([-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?,?)+[\]\,]+)+"

def get_matrix_(matrix_string):
    new_matrix = matrix_string.replace(r'\s', '')
   
    if (re.match(MATRIX_REGEX, new_matrix) is None): 
        print(matrix_string)
        raise 'No matrix'
    return np.array(json.loads(matrix_string))

def gradient_r(x_matrix):
    x = x_matrix[0]
    y = x_matrix[1]

    dx = "-400*x*(y-x^2) - 2*(1-x)"
    dy = "200*(y-x^2)"

    gradient = [
        float(evaluate_function(function_str=dx, x_ = x,  y_=y)),
        float(evaluate_function(function_str=dy, x_= x, y_=y))
    ]
    
    return np.array(gradient)


def rosenbrocks_function(x, k_max, learning_rate, epsilon):
    
    print(x, k_max, learning_rate, epsilon)
    print("X: ", x)
    x_0 = get_matrix(f'{x}')
   
    gradient_ = gradient_descent(gradient_r, x_0=x_0, k_max=int(k_max), learning_rate=float(learning_rate), epsilon=float(epsilon))
    
    print(gradient_)

    return gradient_.copy()



rosenbrocks_function("[0,0]", 10, 0.01, 0.000001)
