from makeRandomExpressions import generate_random_expr
from fitnessAndValidityFunctions import is_viable_expr, compute_fitness
from tqdm import tqdm
from crossOverOperators import random_expression_mutation, random_subtree_crossover
from geneticAlgParams import GAParams

import random
import math 

    
def single_step(curr_state, curr_temp, n_neighbors, identifiers, params):
    
    all_neighbors = []
    neighbor_count = n_neighbors
    gen_success = 0
    while gen_success < neighbor_count:
        rand_n = random_expression_mutation(curr_state, identifiers, params)    
        if is_viable_expr(rand_n, identifiers, params):
            all_neighbors.append(rand_n)
            gen_success += 1
                
    rand_neighbor = random.choice(all_neighbors)
    diff_fitness = compute_fitness(rand_neighbor, identifiers, params) - compute_fitness(curr_state, identifiers, params)
    
    if diff_fitness > 0 or math.exp(diff_fitness/curr_temp) >= random.random():
        return rand_neighbor
    return curr_state
 
        
    
def run_simulated_annealing(n_iter, n_neighbors, identifiers, params):
    
    curr_state = generate_random_expr(params.depth, identifiers, params),
    while not is_viable_expr(curr_state, identifiers, params):
        curr_state = generate_random_expr(params.depth, identifiers, params)
    
    curr_temp = params.simulated_annealing_start_temp
    best_state = curr_state
    best_fitness = compute_fitness(curr_state, identifiers, params)
    
    stats = [best_fitness]
    for i in range(n_iter):
        if i > 0 and i % params.simulated_annealing_cool_steps == 0:
            curr_temp *= params.simulated_annealing_cool_frac
#             print('@Iter %d cooling to %f' % (i, curr_temp))
        curr_state = single_step(curr_state, curr_temp, n_neighbors, identifiers, params)
        curr_fitness = compute_fitness(curr_state, identifiers, params)
        
        if curr_fitness > best_fitness: 
            best_fitness = curr_fitness
            best_state = curr_state
#             print('@Iter %d - Best so far: %f' % (i, curr_fitness))
        stats.append(best_fitness)
    return (best_state, best_fitness, stats)