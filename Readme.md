## Curve Fitting with Genetic Algorithms 
By Max Wiesner
<br>
<br>
#### The High Level Rundown
In this project we will look at how genetic algorithms can use evolutionary search to mutate a number of generations to find a regression curve estination. We will compare our results to the sumulated annealing algorithm, and look at the overall fitness acheived through both methods, and the run time differences between the two. 
<br>
We will apply these tequniques to estimate the following five functions.
<ul>
    <li>$f_1 (x) = \frac{1}{5}e^{\frac{x}{4}} - \sin{2x}$</li>
    <li>$f_2 (x) = \sin{2x} - \cos{3x - 1} + 2\sin{\frac{x}{2} + 1}$</li>
    <li>$f_3 (x) = e^{\sin{2x} - e^{\cos{3x}}}$</li>
    <li>$f_4 (x) = \frac{1}{20}x^2 - \frac{1}{2}x + 5\sin{3x}$</li>
    <li>$f_5 (x) = \frac{1}{20}x^2 - \frac{1}{2}\sqrt{x} + 5\sin{3x}$</li>
</ul>
Performance will also be dependant on the different inputs to each algorithm we have manifest below. Note, the main focus of this project is the genetic algorithm and evolutionary search, not the sumulated annealing algorithm, thus, we will not go in depth on analyzing the changes in performance that come with varying the temperature, cooling rate, and cooling step fraction. Instead, we will vary two parameters that both these functions share (in a sense). 
<ul>
    <li> Iterations - The number of iterations each algorithm will run, with the genetic algorithm this is the number of generations it will mutate and breed; with the simulated annealing, this is the number of times we pick a random neighbor that potentially replaced our current best answer.</li>
    <li> Population - Population is the number of new candidates we produce or hold on to in each iteration. So, for the genetic algorithm, this is clearly the population; ie. in each iteration, we either update the current population, or we reorder it and reevaluate the current fitness of the population. For the simulated annealing, this is the number of new neighbors we produce from our current best state. </li>
    <li><i>Optional Parameters</i> - The number of points we are estimating against, the total number of tests to be run for each function per each (Iterations, Instances) combination. We will not focus on these in the analysis. </li>
<\ul>
Below we see the call to startAllIterations, it takes the following arguments:
<div align="center"><br>$startAllIterations(iterations, instances, points, numTests)$<br></div>
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

      6%|▌         | 9/150 [08:15<1:58:17, 50.33s/it]C:\Users\maxan\CSCI\CSCI_3202\genetic_ai\symbolicExpressions.py:176: RuntimeWarning: overflow encountered in double_scalars
      return reduce(lambda a,b:a*b, flist, 1.0 )
    100%|██████████| 150/150 [2:22:45<00:00, 57.10s/it]   
    

    
    
    


<style  type="text/css" >
    #T_f046f754_87aa_11eb_835e_2816a86e46cb caption {
          color: blue;
          font-size: 18px;
    }    #T_f046f754_87aa_11eb_835e_2816a86e46cbrow0_col6 {
            background-color:  lightblue;
        }    #T_f046f754_87aa_11eb_835e_2816a86e46cbrow1_col2 {
            background-color:  lightgreen;
        }    #T_f046f754_87aa_11eb_835e_2816a86e46cbrow2_col0 {
            background-color:  lightgreen;
        }    #T_f046f754_87aa_11eb_835e_2816a86e46cbrow2_col1 {
            background-color:  lightgreen;
        }    #T_f046f754_87aa_11eb_835e_2816a86e46cbrow2_col3 {
            background-color:  lightgreen;
        }    #T_f046f754_87aa_11eb_835e_2816a86e46cbrow2_col4 {
            background-color:  lightgreen;
        }    #T_f046f754_87aa_11eb_835e_2816a86e46cbrow2_col5 {
            background-color:  lightblue;
        }    #T_f046f754_87aa_11eb_835e_2816a86e46cbrow3_col0 {
            background-color:  lightblue;
        }    #T_f046f754_87aa_11eb_835e_2816a86e46cbrow3_col5 {
            background-color:  #ffcccb;
        }    #T_f046f754_87aa_11eb_835e_2816a86e46cbrow4_col0 {
            background-color:  lightblue;
        }    #T_f046f754_87aa_11eb_835e_2816a86e46cbrow4_col6 {
            background-color:  #ffcccb;
        }</style><table id="T_f046f754_87aa_11eb_835e_2816a86e46cb" style='display:inline'><caption>Genetic Algorithm - Regression Estimation</caption><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Function 1</th>        <th class="col_heading level0 col1" >Function 2</th>        <th class="col_heading level0 col2" >Function 3</th>        <th class="col_heading level0 col3" >Function 4</th>        <th class="col_heading level0 col4" >Function 5</th>        <th class="col_heading level0 col5" >Fitness Avg by Criteria</th>        <th class="col_heading level0 col6" >Run Time Avg by Criteria</th>    </tr>    <tr>        <th class="index_name level0" >Criteria: Num of Iterations, Population Size</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_f046f754_87aa_11eb_835e_2816a86e46cblevel0_row0" class="row_heading level0 row0" >5000, 20</th>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow0_col0" class="data row0 col0" >-6.57723</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow0_col1" class="data row0 col1" >-51.9662</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow0_col2" class="data row0 col2" >-5.40471</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow0_col3" class="data row0 col3" >-638.75</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow0_col4" class="data row0 col4" >-282.398</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow0_col5" class="data row0 col5" >-197.019</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow0_col6" class="data row0 col6" >212.362</td>
            </tr>
            <tr>
                        <th id="T_f046f754_87aa_11eb_835e_2816a86e46cblevel0_row1" class="row_heading level0 row1" >2500, 40</th>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow1_col0" class="data row1 col0" >-4.88371</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow1_col1" class="data row1 col1" >-50.5247</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow1_col2" class="data row1 col2" >-5.31989</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow1_col3" class="data row1 col3" >-777.571</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow1_col4" class="data row1 col4" >-234.66</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow1_col5" class="data row1 col5" >-214.592</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow1_col6" class="data row1 col6" >178.045</td>
            </tr>
            <tr>
                        <th id="T_f046f754_87aa_11eb_835e_2816a86e46cblevel0_row2" class="row_heading level0 row2" >1250, 80</th>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow2_col0" class="data row2 col0" >-3.82035</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow2_col1" class="data row2 col1" >-46.0323</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow2_col2" class="data row2 col2" >-11.0322</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow2_col3" class="data row2 col3" >-529.35</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow2_col4" class="data row2 col4" >-230.333</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow2_col5" class="data row2 col5" >-164.114</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow2_col6" class="data row2 col6" >131.969</td>
            </tr>
            <tr>
                        <th id="T_f046f754_87aa_11eb_835e_2816a86e46cblevel0_row3" class="row_heading level0 row3" >Fitness Avg by Function</th>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow3_col0" class="data row3 col0" >-5.09376</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow3_col1" class="data row3 col1" >-49.5077</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow3_col2" class="data row3 col2" >-7.25226</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow3_col3" class="data row3 col3" >-648.557</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow3_col4" class="data row3 col4" >-249.13</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow3_col5" class="data row3 col5" >-191.908</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow3_col6" class="data row3 col6" >nan</td>
            </tr>
            <tr>
                        <th id="T_f046f754_87aa_11eb_835e_2816a86e46cblevel0_row4" class="row_heading level0 row4" >Run Time Avg by Function</th>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow4_col0" class="data row4 col0" >206.587</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow4_col1" class="data row4 col1" >189.603</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow4_col2" class="data row4 col2" >172.393</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow4_col3" class="data row4 col3" >188.105</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow4_col4" class="data row4 col4" >113.937</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow4_col5" class="data row4 col5" >nan</td>
                        <td id="T_f046f754_87aa_11eb_835e_2816a86e46cbrow4_col6" class="data row4 col6" >174.125</td>
            </tr>
    </tbody></table>


    
    
    


<style  type="text/css" >
    #T_f058d7dc_87aa_11eb_bdb6_2816a86e46cb caption {
          color: blue;
          font-size: 18px;
    }    #T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow0_col3 {
            background-color:  lightgreen;
        }    #T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow0_col6 {
            background-color:  lightblue;
        }    #T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow1_col2 {
            background-color:  lightgreen;
        }    #T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow1_col4 {
            background-color:  lightgreen;
        }    #T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow2_col0 {
            background-color:  lightgreen;
        }    #T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow2_col1 {
            background-color:  lightgreen;
        }    #T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow2_col5 {
            background-color:  lightblue;
        }    #T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow3_col0 {
            background-color:  lightblue;
        }    #T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow3_col5 {
            background-color:  #ffcccb;
        }    #T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow4_col2 {
            background-color:  lightblue;
        }    #T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow4_col6 {
            background-color:  #ffcccb;
        }</style><table id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cb" style='display:inline'><caption>Simulated Annealing Algorithm - Regression Estimation</caption><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Function 1</th>        <th class="col_heading level0 col1" >Function 2</th>        <th class="col_heading level0 col2" >Function 3</th>        <th class="col_heading level0 col3" >Function 4</th>        <th class="col_heading level0 col4" >Function 5</th>        <th class="col_heading level0 col5" >Fitness Avg by Criteria</th>        <th class="col_heading level0 col6" >Run Time Avg by Criteria</th>    </tr>    <tr>        <th class="index_name level0" >Criteria: Num of Iterations, Population Size</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cblevel0_row0" class="row_heading level0 row0" >5000, 20</th>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow0_col0" class="data row0 col0" >-24.381</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow0_col1" class="data row0 col1" >-181.165</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow0_col2" class="data row0 col2" >-76.6704</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow0_col3" class="data row0 col3" >-1628.19</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow0_col4" class="data row0 col4" >-450.115</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow0_col5" class="data row0 col5" >-472.105</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow0_col6" class="data row0 col6" >12.4314</td>
            </tr>
            <tr>
                        <th id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cblevel0_row1" class="row_heading level0 row1" >2500, 40</th>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow1_col0" class="data row1 col0" >-19.1429</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow1_col1" class="data row1 col1" >-171.348</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow1_col2" class="data row1 col2" >-47.8884</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow1_col3" class="data row1 col3" >-2323.14</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow1_col4" class="data row1 col4" >-312.704</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow1_col5" class="data row1 col5" >-574.845</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow1_col6" class="data row1 col6" >5.16175</td>
            </tr>
            <tr>
                        <th id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cblevel0_row2" class="row_heading level0 row2" >1250, 80</th>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow2_col0" class="data row2 col0" >-15.2662</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow2_col1" class="data row2 col1" >-134.526</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow2_col2" class="data row2 col2" >-71.0594</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow2_col3" class="data row2 col3" >-1800.88</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow2_col4" class="data row2 col4" >-315.565</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow2_col5" class="data row2 col5" >-467.459</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow2_col6" class="data row2 col6" >9.39109</td>
            </tr>
            <tr>
                        <th id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cblevel0_row3" class="row_heading level0 row3" >Fitness Avg by Function</th>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow3_col0" class="data row3 col0" >-19.5967</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow3_col1" class="data row3 col1" >-162.346</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow3_col2" class="data row3 col2" >-65.2061</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow3_col3" class="data row3 col3" >-1917.41</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow3_col4" class="data row3 col4" >-359.461</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow3_col5" class="data row3 col5" >-504.803</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow3_col6" class="data row3 col6" >nan</td>
            </tr>
            <tr>
                        <th id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cblevel0_row4" class="row_heading level0 row4" >Run Time Avg by Function</th>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow4_col0" class="data row4 col0" >9.69294</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow4_col1" class="data row4 col1" >2.88638</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow4_col2" class="data row4 col2" >13.4725</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow4_col3" class="data row4 col3" >9.97884</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow4_col4" class="data row4 col4" >8.94304</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow4_col5" class="data row4 col5" >nan</td>
                        <td id="T_f058d7dc_87aa_11eb_bdb6_2816a86e46cbrow4_col6" class="data row4 col6" >8.99475</td>
            </tr>
    </tbody></table>


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

    Funciton 4 Variance and Standard Deviation - Genetic Algorithm
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Test 1</th>
      <th>Test 2</th>
      <th>Test 3</th>
      <th>Test 4</th>
      <th>Test 5</th>
      <th>Mean</th>
      <th>Std Dev</th>
      <th>Variance</th>
    </tr>
    <tr>
      <th>Criteria: Num of Iterations, Population Size</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5000, 20</td>
      <td>-638.750</td>
      <td>-757.077</td>
      <td>-832.292</td>
      <td>-708.430</td>
      <td>-867.538</td>
      <td>-760.817</td>
      <td>82.652</td>
      <td>107,327.138</td>
    </tr>
    <tr>
      <td>2500, 40</td>
      <td>-898.042</td>
      <td>-838.222</td>
      <td>-889.485</td>
      <td>-927.620</td>
      <td>-777.571</td>
      <td>-866.188</td>
      <td>52.851</td>
      <td>122,989.728</td>
    </tr>
    <tr>
      <td>1250, 80</td>
      <td>-743.797</td>
      <td>-728.548</td>
      <td>-656.962</td>
      <td>-529.350</td>
      <td>-621.810</td>
      <td>-656.093</td>
      <td>77.694</td>
      <td>81,950.744</td>
    </tr>
  </tbody>
</table>
</div>


    
    
    Funciton 4 Variance and Standard Deviation - Simulated Annealing Algorithm
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Test 1</th>
      <th>Test 2</th>
      <th>Test 3</th>
      <th>Test 4</th>
      <th>Test 5</th>
      <th>Mean</th>
      <th>Std Dev</th>
      <th>Variance</th>
    </tr>
    <tr>
      <th>Criteria: Num of Iterations, Population Size</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5000, 20</td>
      <td>-638.750</td>
      <td>-757.077</td>
      <td>-832.292</td>
      <td>-708.430</td>
      <td>-867.538</td>
      <td>-760.817</td>
      <td>82.652</td>
      <td>107,327.138</td>
    </tr>
    <tr>
      <td>2500, 40</td>
      <td>-898.042</td>
      <td>-838.222</td>
      <td>-889.485</td>
      <td>-927.620</td>
      <td>-777.571</td>
      <td>-866.188</td>
      <td>52.851</td>
      <td>122,989.728</td>
    </tr>
    <tr>
      <td>1250, 80</td>
      <td>-743.797</td>
      <td>-728.548</td>
      <td>-656.962</td>
      <td>-529.350</td>
      <td>-621.810</td>
      <td>-656.093</td>
      <td>77.694</td>
      <td>81,950.744</td>
    </tr>
  </tbody>
</table>
</div>


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
> <b>mutate_all_exprs</b> : In this method, we are doing two operations to the 80% that need to be improved. First, we assign all of the childrens in pairs, next we randomly do one of two operations on them. Either we swap their sub trees (cross their genes), or we mutate them separately. This is like randomly changing a random part of their sub trees, but independent of its pair. Finally, we check if their new expression is valid, ie. no $\sqrt{-1}$, and if so, we move on to the next pair, until the entire 80% we were passed is an entirely new group. Then we pass these back to be joined with the elite 20% that were good enough to avoid this process. <br>

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
The computing time was the main difficulty in this. Having to mutate a population of size $.8N$, for <i>n_iter</i> generations, while also having to sort them descending at each step to reevaluate the new elitism group, is heavy on the CPU. Thats why we added the variables at the beginning so this simulation can be ran at lets say 50%, where we can still observe the results in proportion to what they are meant to be observed at. Though it should go without saying, a simulation ran at 50% the intended amount of iterations, and population size, will display worst results to that ran at a higher percentage with considerably more iterations, and population size.  
<br>
### Final Charts
Here we display the 'best of' categories we highlighted in our first set of data tables. For each algorithm, we chart the best performing function in the best performing group of functions, and we chart the function with the fastest runtime in the group of functions that had the fastest average runtime. These results will change for each new simulation, but the functions with the same criteria outlined will always be displayed. 


```python
printVizs(2)
```

    
    
    
    Genetic Algorithm : 
       [Best Performing Function in Highest Average Fitness Column] : Function 1
       Iterations = 1250, Population = 80
       Function: sin((x * -2.0) - (exp(x)/(((x * 6.695091554281198) * x * -2.0) + -1.0)))
       Fitness: -3.8203523318932935
       Runtime: 58.14371919631958
    
    


![png](output_9_1.png)



![png](output_9_2.png)


    
    
    
    Genetic Algorithm : 
       [Best Performing Funciton in Fastest Average Runtime Column] : Function 1
       Iterations = 125, Neighborhood Size = 80
       Function: sin((x * -2.0) - (exp(x)/(((x * 6.695091554281198) * x * -2.0) + -1.0)))
       Fitness: -3.8203523318932935
       Runtime: 58.14371919631958
    
    


![png](output_9_4.png)



![png](output_9_5.png)


    
    
    
    
    
    Simulated Annealing Algorithm : 
       [Best Performing Function in Highest Average Fitness Column] : Function 1
       Iterations = 1250, Population = 80
       Function: cos((1.0 + x + x))
       Fitness: -15.266224902439523
       Runtime: 12.952633619308472
    
    


![png](output_9_7.png)



![png](output_9_8.png)


    
    
    
    Simulated Annealing Algorithm : 
       [Best Performing Funciton in Fastest Average Runtime Column] : Function 3
       Iterations = 250, Neighborhood Size = 40
       Function: sin((x + -1.0 + 0.8012856433095585 + x))
       Fitness: -47.88835330900699
       Runtime: 3.1621313095092773
    
    


![png](output_9_10.png)



![png](output_9_11.png)


#### Thats All Folks!
