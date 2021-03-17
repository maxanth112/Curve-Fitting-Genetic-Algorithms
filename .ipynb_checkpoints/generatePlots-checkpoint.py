from curveFitting import one_dimensional_curve_fitting_test
from matplotlib import pyplot as plt
from IPython.display import display, HTML
from tqdm import tqdm

import numpy as np
import pprint
import pandas as pd
import math


names = ['Genetic Algorithm', 'Simulated Annealing Algorithm']
plot_printout_indexs = []
tests = [
    [lambda x: 0.2*math.exp(x/4.0) -  math.sin(2*x), (-10.0, 10.0), 25],
    [lambda x: math.sin(2*x) - math.cos(3*x-1) + 2*math.sin(x/2+1.0), (-15.0, 15.0), 60],
    [lambda x: math.exp(math.sin(2*x)) - math.exp(math.cos(3*x)), (-15.0, 15.0), 60],
    [lambda x: 0.05*x**2 - 0.5*x + 5.0 * math.sin(3*x) , (-15.0, 15.0), 60],
    [lambda x: 0.05*x**2 - 0.5*math.sqrt(x) + 5.0 * math.sin(3*x) , (0.0, 15.0), 30]
]

def startAllIterations(iterations = 1, population_num = 1, point_count = 1, each_test = 5):

    global GA_criteria 
    GA_criteria = np.array([[iterations*10000, population_num*40, point_count*100], 
                            [iterations*5000, population_num*80, point_count*100], 
                            [iterations*2500, population_num*160, point_count*100]]).astype(int)
    global SA_criteria
    SA_criteria = np.array([[iterations*1000, population_num*40, point_count*100],
                                [iterations*500, population_num*80, point_count*100],
                                [iterations*250, population_num*160, point_count*100]]).astype(int)

    global test_instances
    test_instances = [{'results': [[-float('inf')]*5 for i in range(3)],
                           'all': [[0]*5 for i in range(3)],
                           'conditions': criteria} for criteria in [GA_criteria, SA_criteria]]
    
    with tqdm(total = each_test*len(GA_criteria)*len(test_instances)*len(tests)) as pbar:
        for iteration in range(each_test):
            for curr_algorithm_index in range(len(test_instances)):
                for curr_condition_index in range(len(test_instances[curr_algorithm_index]['conditions'])):
                    for curr_test_index in range(len(tests)):
                        all_data_results = one_dimensional_curve_fitting_test(tests[curr_test_index][0], 
                            tests[curr_test_index][1], 
                            tests[curr_test_index][2], 
                            test_instances[curr_algorithm_index]['conditions'][curr_condition_index][0],
                            test_instances[curr_algorithm_index]['conditions'][curr_condition_index][1], 
                            test_instances[curr_algorithm_index]['conditions'][curr_condition_index][2],
                            'ga' if curr_algorithm_index == 0 else 'sa')

                        if all_data_results[1] > test_instances[curr_algorithm_index]['results'][curr_condition_index][curr_test_index]:
                            test_instances[curr_algorithm_index]['results'][curr_condition_index][curr_test_index] = all_data_results[1]
                            test_instances[curr_algorithm_index]['all'][curr_condition_index][curr_test_index] = all_data_results
                        pbar.update(1)       
                        
                        
        
        
def highlight_last_max(data, colormax='antiquewhite', colormaxlast='lightgreen'):

    colormax_attr = f'background-color: {colormax}'
    colormaxlast_attr = f'background-color: {colormaxlast}'
    max_value = data.max()
    is_max = [colormax_attr if v == max_value else '' for v in data]
    is_max[len(data) - list(reversed(data)).index(max_value) -  1] = colormaxlast_attr
    return is_max




def highlight_max_save(data, colormax='antiquewhite', colormaxlast='lightgreen', index = 0):
    
    is_max = [1 if v == data.max() else 0 for v in data]
    max_index_x = is_max.index(max(is_max))
    max_contendors = [test_instances[index]['results'][i][max_index_x] for i in range(3)]
    max_index_y = max_contendors.index(max(max_contendors))
    plot_printout_indexs.append([index, max_index_x, max_index_y])
    
    return highlight_last_max(data, colormax, colormaxlast)
    
    
    
    
def create_data_frames():
    dfs = [None]*2
     
    for ind in range(len(names)):
        df = pd.DataFrame(np.array([[test_instances[ind]['results'][i][j] for j in range(5)] for i in range(3)]), index = [f'{crit[0]}, {crit[1]}' for crit in GA_criteria], 
                                   columns = [f'Function {i}' for i in range(1, 6)])
        df.style.set_table_attributes("style='display:inline'").set_caption(f'{names[ind]} - Regression Estimation')
        df.loc['Fitness Avg by Function']= df.mean(numeric_only=True, axis=0)
        df.loc[:,'Fitness Avg by Criteria'] = df.mean(numeric_only=True, axis=1)
        pd.options.display.float_format = '{:,.3f}'.format        
        df = df.rename_axis('Criteria: Num of Iterations, Population Size')
        
        df['Run Time Avg by Criteria'] = [np.mean([test_instances[ind]['all'][i][j][3] for j in range(5)]) for i in range(3)] + [None]
        df.loc['Run Time Avg by Function'] = [np.mean([test_instances[ind]['all'][i][j][3] for i in range(3)]) for j in range(5)] + \
            [None, np.mean([np.mean([test_instances[ind]['all'][i][j][3] for i in range(3)]) for j in range(5)])]
        css = """
            .output {
                flex-direction: row;
            }
        """
        HTML('<style>{}</style>'.format(css))

        df = df.style.apply(highlight_last_max, subset = pd.IndexSlice[[f'{crit[0]}, {crit[1]}' for crit in GA_criteria], [f'Function {i}' for i in range(1, 6)]], axis = 0) \
            .set_table_attributes("style='display:inline'") \
            .set_caption(f'{names[ind]} - Regression Estimation') \
            .set_table_styles([{
                    'selector': 'caption',
                    'props': [
                        ('color', 'blue'),
                        ('font-size', '18px')
                    ]
                }]) \
            .apply(highlight_max_save, subset = pd.IndexSlice["Fitness Avg by Function", \
                                            [f'Function {i}' for i in range(1, 6)]], axis = 1, colormaxlast = 'lightblue', index = ind) \
            .apply(highlight_max_save, subset = pd.IndexSlice["Run Time Avg by Function", \
                                            [f'Function {i}' for i in range(1, 6)]], axis = 1, colormaxlast = 'lightblue', index = ind) \
            .apply(highlight_last_max, subset = pd.IndexSlice[ [f'{crit[0]}, {crit[1]}' for crit in GA_criteria], \
                                            ['Fitness Avg by Criteria', 'Run Time Avg by Criteria']], axis = 0, colormaxlast = 'lightblue') \
            .apply(highlight_last_max, subset = pd.IndexSlice["Fitness Avg by Function", ['Fitness Avg by Criteria']], axis = 0, colormaxlast = '#ffcccb')  \
            .apply(highlight_last_max, subset = pd.IndexSlice["Run Time Avg by Function", ['Run Time Avg by Criteria']], axis = 0, colormaxlast = '#ffcccb')  
        dfs[ind] = df        
    return dfs




def print_plots(plot, message = 0):
    message = "Best Performing Function in Highest Average Fitness Column" if message == 0 else "Best Performing Funciton in Fastest Average Runtime Column"
    criteria = GA_criteria if plot[0] == 0 else SA_criteria
    population_name = "Population" if plot[0] == 0 else "Neighborhood Size"
    data = test_instances[plot[0]]['all'][plot[2]][plot[1]][4].regression_training_data
    test_points = test_instances[plot[0]]['all'][plot[2]][plot[1]][4].test_points
    best_expr = test_instances[plot[0]]["all"][plot[2]][plot[1]][0]
    stats = test_instances[plot[0]]["all"][plot[2]][plot[1]][2]
    print(f'\n\n\n{names[plot[0]]} : \n   [{message}] : Function {plot[1] + 1}')
    print(f'   Iterations = {criteria[plot[2]][0]}, {population_name} = {criteria[plot[2]][1]}')
    print(f'   Function: {best_expr}')
    print(f'   Fitness: {test_instances[plot[0]]["all"][plot[2]][plot[1]][1]}')
    print(f'   Runtime: {test_instances[plot[0]]["all"][plot[2]][plot[1]][3]}\n')

    plt.figure(1)
    x_values = [x_value for ([x_value], _) in data]
    plt.plot(x_values, [y for (_,y) in data],'x')
    test_xvalues = sorted([x for [x] in test_points])
    result = [best_expr.eval({'x':x_value}) for x_value in test_xvalues]

    gTruth = [tests[plot[1]][0](x_value) for x_value in test_xvalues ]
    plt.plot(test_xvalues, result, 'r-',label='ga_fit')
    plt.plot(test_xvalues, gTruth, 'g-', label='ground-truth')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.figure(2)
    plt.plot(range(len(stats)), [st for st in stats], 'b-')
    plt.xlabel('Iters')
    plt.ylabel('Max Fitness')
    plt.plot(range(len(stats)), [(st if st > -100 else -100) for st in stats], 'r--')
    plt.show()
    
    
    
    
def printVizs():
    dfs = create_data_frames()
    print('\n')
    display(dfs[0])
    print_plots(plot_printout_indexs[0], 0)
    print_plots(plot_printout_indexs[1], 1)
    print('\n')
    display(dfs[1])
    print_plots(plot_printout_indexs[2], 0)
    print_plots(plot_printout_indexs[3], 1)