from makeRandomExpressions import generate_random_expr
from fitnessAndValidityFunctions import is_viable_expr, compute_fitness
from numpy.random import choice
import numpy as np
import math
from crossOverOperators import random_expression_mutation, random_subtree_crossover
from geneticAlgParams import GAParams
from matplotlib import pyplot as plt 

class GASolver: 
    def __init__(self, params, lst_of_identifiers, n):
        
        self.params = params                     # parameters for GA, includes test data for regression and checking validity
        self.N = n                               # The population size
        self.chillums = []                       # store the population, fitness, and probability for mutation
        self.identifiers = lst_of_identifiers    # A list of identifiers for the expressions
        self.population_stats = []               # Maintain statistics on best fitness in each generation
        self.best_solution_so_far = None         # Store best solution so far across all generations
        self.best_fitness_so_far = -float('inf') # Store the best fitness so far across all generations

    
    def create_chillum(self, expr):
        expr_fitness = compute_fitness(expr, self.identifiers, self.params)
        return {
            'expr' : expr, 
            'fitness' : expr_fitness, 
            'prob' : np.exp(expr_fitness/self.params.temperature)
        }
    
    
    def sort_chillums_by(self, chillum_list, sort_method = 'fitness'):
        return sorted(chillum_list, key = lambda chillum : chillum[sort_method], reverse = True)
    
    
    def generate_initial_pop(self):        
        gen_success = 0
        while gen_success < self.N:
            rand_expr = generate_random_expr(self.params.depth, self.identifiers, self.params)            
            if is_viable_expr(rand_expr, self.identifiers, self.params):
                self.chillums.append(self.create_chillum(rand_expr))
                gen_success += 1
#                 print(f'generated initial: {gen_success} {self.chillums[gen_success - 1]}')
    
    
    def mutate_all_exprs(self, candidates, method = 'crossover'):
    
        mutated_list = []
        candidates = self.sort_chillums_by(candidates, 'prob')
        candidate_weights = [chillum['prob'] for chillum in candidates]
        while True:            
            chillum_pair = choice(candidates, 2, candidate_weights)
            
            if method == 'crossover' or (method == 'mix' and random.randint(1, 10) <= 5):
                mutated_pair = random_subtree_crossover(chillum_pair[0]['expr'], chillum_pair[1]['expr'])
            elif method == 'mutation' or (method == 'mix'):
                mutated_pair = [random_expression_mutation(chillum['expr']) for chillum in chillum_pair]
                
            for mutated_expr in mutated_pair:
                if is_viable_expr(mutated_expr, self.identifiers, self.params):
                    mutated_list.append(self.create_chillum(mutated_expr))
                    if len(mutated_list) == len(candidates):
                        break
            
        return mutated_list
            
            
    def make_next_generation(self):
      
        self.chillums = self.sort_chillums_by(self.chillums, 'fitness')
        elitism_carryover = self.chillums[:int(self.N*self.params.elitism_fraction)]
        new_mutated = self.mutate_all_exprs(self.chillums[int(self.N*self.params.elitism_fraction):])
        next_gen = elitism_carryover + new_mutated
        
        print(self.chillums)
        
        self.chillums = sort_chillums_by(self.chillums, 'fitness')
        self.best_solution_so_far = self.chillums[0]['expr']
        self.best_fitness_so_far = self.chillums[0]['fitness']
        self.population_stats.append(self.chillums[0]['fitness'])
    
    
    def run_ga_iterations(self, generations=1000):
        self.generate_initial_pop()
        for evolve in range(generations):
#             print(f'iteration: {evolve} best value: {self.best_fitness_so_far}')
            self.make_next_generation()
            

## Function: curve_fit_using_genetic_algorithms
# Run curvefitting using given parameters and return best result, best fitness and population statistics.
def curve_fit_using_genetic_algorithm(params, lst_of_identifiers, pop_size, num_iters):
    solver = GASolver(params, lst_of_identifiers, pop_size)
    solver.run_ga_iterations(num_iters)
    return (solver.best_solution_so_far, solver.best_fitness_so_far, solver.population_stats)


# Run test on a toy problem.
if __name__ == '__main__':
    params = GAParams()
    params.regression_training_data = [
       ([-2.0 + 0.02*j], 5.0 * math.cos(-2.0 + 0.02*j) - math.sin((-2.0 + 0.02*j)/10.0)) for j in range(201)
    ]
    params.test_points = list([ [-4.0 + 0.02 * j] for j in range(401)])
    solver = GASolver(params,['x'],500)
    solver.run_ga_iterations(100)
    print('Done!')
    print(f'Best solution found: {solver.best_solution_so_far.simplify()}, fitness = {solver.best_fitness_so_far}')
    stats = solver.population_stats
    niters = len(stats)
    plt.plot(range(niters), [st[0] for st in stats] , 'b-')
    plt.show()



