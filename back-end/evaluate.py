import numpy as np
import re
import sympy 
import json


x, y, z, e = sympy.symbols("x y z e")

MULTIPLICATION_REGULAR = r'(\d+(\.\d+)?)([a-z])'

MATRIX_REGEX =  r"(\[+([-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?,?)+[\]\,]+)+"

def get_matrix(matrix_string):
    new_matrix = matrix_string.replace(r'\s', '')
   
    if (re.match(MATRIX_REGEX, new_matrix) is None): 
        print(matrix_string)
        raise 'No matrix'
    return np.array(json.loads(matrix_string))

def multiplication_case(match_object):

    new_expression = ""

    for match_group in range(1, len(match_object.groups())):
        if match_object.group(match_group) is not None:
            new_expression +=  match_object.group(match_group)
    
    if match_object.group(3) is not None:
        new_expression += "*" + match_object.group(3)

    return new_expression

def evaluate_function(function_str, x_, y_ = 0, z_ = 0):

    function_parsed = function_str.replace('^', '**')
    function_parsed = re.sub(MULTIPLICATION_REGULAR, multiplication_case, function_str)

    expression = sympy.sympify(function_parsed)

    return expression.evalf(subs={x: x_, y : y_, z : z_, e : sympy.E})


def f(function_str, x):
    return evaluate_function(function_str, x)

def f_prime(function_str, x):
    delta_x = 0.00001
    return (evaluate_function(function_str, x + delta_x) - evaluate_function(function_str,x)) / delta_x


def f_bi_prime(function_str, x): 
    delta_x = 0.00001

    fx_plus_delta_x = f(function_str, x + delta_x)
    fx = f(function_str, x)
    fx_subs_delta_x = f(function_str, x - delta_x)

    return  (fx_plus_delta_x -  2 * fx + fx_subs_delta_x) / (delta_x ** 2)
