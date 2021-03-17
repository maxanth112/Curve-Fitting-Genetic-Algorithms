from geneticAlgParams import GAParams
from geneticSearchAlgorithms import curve_fit_using_genetic_algorithm
from random import random
from matplotlib import pyplot as plt
from simulatedAnnealing import run_simulated_annealing 

import math 
import time


def one_dimensional_curve_fitting_test(lambda_fun, x_limits, n_data_points, pop_size = 1000, num_iters = 100, n_test_points = 100, method='ga'):
    
    params = GAParams()
    (a, b) = x_limits
    assert a < b
    # first generate data 
    data = [] 
    for i in range(n_data_points):
        x_value = a + random() * (b-a)
        data.append( ([x_value], lambda_fun(x_value)) )
    
    delta = (b-a)/(n_test_points)
    test_points = []
    for j in range(n_test_points+1):
        test_points.append([a + j * delta])
    
    params.test_points = test_points
    params.regression_training_data = data 
    
    start = time.time()
    
    if method == 'ga':
        (best_expr, best_fitness, stats) = curve_fit_using_genetic_algorithm(params, ['x'], pop_size, num_iters)
        best_expr = best_expr.simplify()
    else: 
        params.temperature = params.simulated_annealing_start_temp
        (best_expr, best_fitness, stats) = run_simulated_annealing(num_iters, pop_size, ['x'], params)
        
    end = time.time()
    elapsed_time = end - start
    return (best_expr, best_fitness, stats, elapsed_time, params)

if __name__ == '__main__':
    one_dimensional_curve_fitting_test(lambda x: 0.2*math.exp(x/4.0) -  math.sin(2*x)  , (-10.0, 10.0), 25, method='sa')
    