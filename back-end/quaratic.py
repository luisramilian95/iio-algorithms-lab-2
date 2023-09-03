from evaluate import get_matrix
import numpy as np
    
from numpy import linalg as LA
import pandas as pd


dictionary = {
    'Q' : [], 
    'c' : []
}

'''
f(x) = 1/2 x^T Q x + c^Tx
'''

def gradient_q(x):
    Q = dictionary.get('Q')
    c = dictionary.get('c')

    Q_sum= Q + np.transpose(Q)
    dot = np.dot(Q_sum, x)

    return  0.5* dot + c


def get_optimal_learning_rate(x_k):
    gradient_ = gradient_q(x_k)
    product = np.dot(np.transpose(gradient_), gradient_)
    Q = dictionary.get('Q')
    product_ = np.dot(np.transpose(gradient_), Q)
    product_ =LA.inv(np.dot(product_, gradient_))
    return np.dot(product, np.transpose(product_)) 
                       

def get_learning_rate(step_size, k, x_k) :
    if step_size == 'exacto' :
        return  get_optimal_learning_rate(x_k)
    elif step_size == 'variable':
        return float(1/(k+1))
    else:
        return float(step_size)

def gradient_descent_q(gradient, x_0, k_max, learning_rate, epsilon):

    x_k = x_0
    k = 0

    table = []

    for k in range(k_max):

        gradient_ = gradient(x_k)
        norm = LA.norm(gradient_)

        table.append([float(k), f'{x_k}', f'{gradient_}', float(norm)])
    
        if norm < epsilon:
            break

        a_k = get_learning_rate(learning_rate, k=k, x_k=x_k)

        print(a_k)

        x_k = x_k -  a_k * gradient_

    return pd.DataFrame(table, columns=["k", "x_k", 'pk', "error"])

def quadratic_function(x_str, Q_str, c_str, k_max, learning_rate, epsilon):

    x_0 = get_matrix(x_str)
    Q = get_matrix(Q_str)
    c = get_matrix(c_str)

    dictionary['Q'] = Q
    dictionary['c'] = c

    print(k_max, learning_rate, epsilon)

    gradient_ = gradient_descent_q(gradient_q, x_0, int(k_max), (learning_rate), float(epsilon))
    
    print(gradient_)

    return gradient_

Q = "[[2, -1, 0], [-1, 2, -1], [0, -1, 2]]"
c = "[[1], [0], [1]]"
x = "[[3], [5], [7]]"

quadratic_function(x, Q, c, 100, "exacto", 0.00000001)