## Curve Fitting with Genetic Algorithms 
By Max Wiesner <i>*head to projectDetails.ipynb to run and test simulations</i>
<br>
<br>
#### The High Level Rundown
In this project we will look at how genetic algorithms can use evolutionary search to mutate a number of generations to find a regression curve estination. We will compare our results to the sumulated annealing algorithm, and look at the overall fitness acheived through both methods, and the run time differences between the two. 
<br>
We will apply these tequniques to estimate the following five functions.
<ul>
    <li><img src="https://render.githubusercontent.com/render/math?math=f_1 (x) = \frac{1}{5}e^{\frac{x}{4}} - \sin{2x}"></li>
    <li><img src="https://render.githubusercontent.com/render/math?math=f_2 (x) = \sin{2x} - \cos{3x - 1} + 2\sin{\frac{x}{2} + 1}"></li>
    <li><img src="https://render.githubusercontent.com/render/math?math=f_3 (x) = e^{\sin{2x} - e^{\cos{3x}}}"></li>
    <li><img src="https://render.githubusercontent.com/render/math?math=f_4 (x) = \frac{1}{20}x^2 - \frac{1}{2}x + 5\sin{3x}"></li>
    <li><img src="https://render.githubusercontent.com/render/math?math=f_5 (x) = \frac{1}{20}x^2 - \frac{1}{2}\sqrt{x} + 5\sin{3x}"></li>
</ul>
Performance will also be dependant on the different inputs to each algorithm we have manifest below. Note, the main focus of this project is the genetic algorithm and evolutionary search, not the sumulated annealing algorithm, thus, we will not go in depth on analyzing the changes in performance that come with varying the temperature, cooling rate, and cooling step fraction. Instead, we will vary two parameters that both these functions share (in a sense). 
<ul>
    <li> Iterations - The number of iterations each algorithm will run, with the genetic algorithm this is the number of generations it will mutate and breed; with the simulated annealing, this is the number of times we pick a random neighbor that potentially replaced our current best answer.</li>
    <li> Population - Population is the number of new candidates we produce or hold on to in each iteration. So, for the genetic algorithm, this is clearly the population; ie. in each iteration, we either update the current population, or we reorder it and reevaluate the current fitness of the population. For the simulated annealing, this is the number of new neighbors we produce from our current best state. </li>
    <li><i>Optional Parameters</i> - The number of points we are estimating against, the total number of tests to be run for each function per each (Iterations, Instances) combination. We will not focus on these in the analysis. </li>
<\ul>
Below we see the call to startAllIterations, it takes the following arguments:
    <div align="center"><br><b>startAllIterations(iterations, instances, points, numTests)</b><br></div>
    <br>
The different combinations of iterations, population for each test and algorithm has already been picked out, and will be highlighted in the results summary below. The reason for the parameters below are for accomodating available CPU performance; ie. if you are confident in your super fast new MacBook Pro with the M1 chip, then put iterations = population = 1, 100%. This will run the intended amount of each combination. But if you are repping the google chromebook, then you may put iterations = population = .25, 25%. This will still run all of the intended combinations, but adjust the totals proportionally to the percentages entered, since running the full intended amount, 100%, might take some hours.  
<br>
<br>
A progress bar will update as tests are completed. 
<br>
<br>

### Simulation Results


```python
%matplotlib inline
from generatePlots import startAllIterations, printVizs

iterations = 0.5 # optimal : 1, otherwise : must be at least 5% to avoid Null equations 
population = 0.5 # optimal : 1, otherwise : must be at least 5% to avoid Null equations
num_points = 1 # optimal : 1
num_tests = 5 # optimal : 5
startAllIterations(iterations, population, num_points, num_tests)
printVizs()
```

#### Data Table Details
> <span style="color:lightgreen">Green : </span> Best fitness per column - Function, cooresponding to the index column of iterations, population<br>
> <span style="color:lightblue">Blue : </span> Overall best performance - Highlights the column and row best performances on average.<br>
> <span style="color:#ffcccb">Red </span> Benchmark KPI for each algorithm - Shows the average fitness acheived from the overall tests with the ranging criteria. Ans the overall runtime per test against the ranging average inputs. 
<br>
##### Observations 
As seen above, the two tables highlight the observed statistics for each of the algorithms. Simmulated annealing seems to perform a lot faster on average, but at the cost of its fitness functions. The genetic algorithm takes longer, but has almost twice as good fitness functions as compared to the simulated annealing. On average, we also observed that the first and third functions were the functions we were able to consistently approximate the best, followed by the second, then fifth, then fourth function. Since the fourth function was consistently the hardest to estimate, we will look closer at its estimations and cooresponding fitness values next. 
<br> 
<br>
#### Fitness : Standard Deviation, and Variance
Here we look closer at function 4; since it was the worst performing on average, it is likely to show better insight as compared to the consistently top performing function 1. Below we see the total tests used in estimating function 4. Five tests for each of the three conditions. Notice the high standard deviation and variance of each of the categories. Generally, the more iterations, the better results we got, thus less variance. This is why we see in all of the cases we run, that the top category with the most iterations performing the best. It also gives insight that a lower population leads to better results to a certain degree in the genetic algorithm. This makes since because there will be considerably better 'average genes' in a smaller population once good genes are found. With simulated annealing on the other hand, we saw the best performance with somewhat balanced iterations to population criteria. 


```python
if num_tests == 5:
    printVizs(1)
```

Write a brief analysis of your results. Some questions to answer:
- Which problem ran the fastest? Why do you think this is the case?
- Which problem ended with the highest fitness? Why do you think this is the case?
- How similar were the running times across the 5 repetitions?
- How similar were the final fitness scores across the 5 repetitions?
- Was there anything else interesting in your results?

### The Implementation
<b>Genetic Algorithm</b><br>
The structure for the genetic algorithm was split up into three main parts, with a few additional helper functions. We put everything inside of a class GASolver, where the details and specifics of the state could be easily tracked and accessed. All of our expressions that we mutated or passed on in each iteration were kept in a data structure called 'chillums', slang for them childrens, since we are dabbling in genetics and evolutionary mutation, it seemed fitting. Each child of the current population was stored with its fitness value, and its selection weight, thus we could easily locate all the needed details when mutating the population and deciding who to keep and scrap. 
> <b>run_ga_iterations</b> : This method initiated the evolution, we first randomly created N children, and then we made these kids have kids, then we bred their kids with some of them, or maybe other kids, and continued this for iter_n generations. We loop through this process in this function, but we call another function to do the work for us. <br>
> <b>make_next_generation</b> : Here, we sort all of the current children by their fitness level, and keep the top 20% for breeding in the next generation. The other 80% are sent off to a figuritive labratory where we mix and match their genes. In this case, we are swapping sub trees of their expressions. Next, we join the two groups back together, in descending order of fitness values, and we record our current bests.<br>
> <b>mutate_all_exprs</b> : In this method, we are doing two operations to the 80% that need to be improved. First, we assign all of the childrens in pairs, next we randomly do one of two operations on them. Either we swap their sub trees (cross their genes), or we mutate them separately. This is like randomly changing a random part of their sub trees, but independent of its pair. Finally, we check if their new expression is valid, ie. no <img src="https://render.githubusercontent.com/render/math?math=\sqrt{-1}">, and if so, we move on to the next pair, until the entire 80% we were passed is an entirely new group. Then we pass these back to be joined with the elite 20% that were good enough to avoid this process. <br>

*All of the code for this can be found in geneticSearchAlgorithms.py, and the code mangling, storing, and analyzing this data can be found in generatePlots.py
<br><br>
<b>Simulated Annealing Algorithm</b><br>
This algorithm was comprised of two main funcitons. Here, our goal was to start with an initial child, and through each iteration, we generated N mutations of our one child, this was done by the same random subtree alteration we used above in the genetic algorithms implementation. From here, we randomly selected a expression from this group of 'neighbors' (since they are closely related to the main child), and we then chose either to take this random one, of keep our current. 
> <b>run_simulated_annealing</b> : This is the main function where our control logic lives. We first generate a random expression, making sure that this random expression is a valid one. Next we record its fitness level in longitutal array of stats that keeps a record of our iterations best for later plotting. Then, we enter the main loop. From here, we check if we need to reduce our temperature, the temperature updated based on what iteration we are currently on and the provided cooling step we set. It is used in making the descision of randomly keeping a less than optimal expression with the methodology that it could save us from local maxima and help us toward the goal of finding the global maxima; we reduce the temperature by the cooling fraction (how fast we want to decrement the temperature). Next, we compute a single step, save out current fitness, and update our global statistics. <br>
> <b>single_step</b> : In this function, we are passed the current expression (child) for the current iteration. Here, is where we generate the N neighbors of our current expression, also checking that we get N valid expressions. Next, we automatically accept better answers, with the caviot of that special occasion we highlighted above where we will take a worse expression to replace our good one on occasion, according to our current temperature. The temperature decreases as the iterations grow, so we are less likely to accept worse answers later on in the algorithm, and more likely at the beginning. 
<br>

*The code relating to this algorithm is found in simulatedAnnealing.py, as well as the data wrangling associated in generatePlots.py
<br><br><br>
#### Better Results?
With the genetic algorithm we observed that more iterations (generations) were always better. This is clear since if we only keep the top in each generation, there is only one way to generally go, up, unless we are incredibly statistically unfortunate and we can't randomly generate or mutate any better expressions. This could be the case when we are so close to the actual expression, but not the case when we are a fair ways away. So, better results will come with more generations (iterations), and varying the population size accordingly. Too small a population will take a long time to dramatically improve, but not longer than an incredibly large population. This is because as we increase the population, we increase the time that much more because at every iteration we will need to calculate the increase. 
<br>
##### Struggles? 
The computing time was the main difficulty in this. Having to mutate a population of size .8N, for <i>n_iter</i> generations, while also having to sort them descending at each step to reevaluate the new elitism group, is heavy on the CPU. Thats why we added the variables at the beginning so this simulation can be ran at lets say 50%, where we can still observe the results in proportion to what they are meant to be observed at. Though it should go without saying, a simulation ran at 50% the intended amount of iterations, and population size, will display worst results to that ran at a higher percentage with considerably more iterations, and population size.  
<br>
### Final Charts
Here we display the 'best of' categories we highlighted in our first set of data tables. For each algorithm, we chart the best performing function in the best performing group of functions, and we chart the function with the fastest runtime in the group of functions that had the fastest average runtime. These results will change for each new simulation, but the functions with the same criteria outlined will always be displayed. 


```python
printVizs(2)
```

#### Thats All Folks!
