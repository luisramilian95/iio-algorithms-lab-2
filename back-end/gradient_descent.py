from numpy import linalg as LA
import pandas as pd


def gradient_descent(gradient, x_0, k_max, learning_rate, epsilon):

    x_k = x_0
    k = 0

    table = []

    for k in range(k_max):

        gradient_ = gradient(x_k)
        norm = LA.norm(gradient_)

        table.append([float(k), f'{x_k}', f'{gradient_}',float(norm)])

        if norm < epsilon:
            break

        x_k = x_k - learning_rate * gradient_


    return pd.DataFrame(table, columns=["k", "x_k", 'pk', "error"])