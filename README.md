### 1. Justification of why you have chosen your topic.
 In our previous paper, **"[Here, There, Anywhere: Profiling-Driven Services to Tame the Heterogeneity of Edge Applications] (https://ieeexplore.ieee.org/document/9592388)"**, we proposed a profiling-based methodology that effectively matches edge computational tasks with the available devices to best satisfy programmer-defined non-functional requirements. In this project, I want to extend my paper and include a genetic algorithm to efficiently schedule tasks to the edge devices based on the execution time of the task. The main idea is to complete task in limited amount of time. 






### 2. What is the topic?
**A Genetic Algorithm to schedule task in edge computing**
### 3. Design decision explaining why you select:

![Solution](https://pandeymanish.com/images/solution.png) 
Here E1, E2, E3 are the edge nodes and T1, T2, T3, T4, T5, are the input task.


  1. **Input Parameter**
     - **Population Size (popSize):** 1000 
     - **Number of edge devices (noOfEdge):** 10
     - **Number of tasks (noOfTask):** 150
     - **Execution Time of each task:** Currently execution time is set randomly from 2 to 50 seconds 
     - **Threshold (threshold):** 70s
     - **Maximum Repeat (maxRepeat):** 15
     -  **Maximum Generation (maxGen):** 15
     -  **Maximum Running Time in seconds (maxTime):** 1200
     > Each of the input can be modify based on the requirement of users
     >
     > **How population and individual looks like**
     > [[8, 3, 1, 8, 3, 4, 2, 4, 1, 6, 9, 6, 1, 2, 6, 7, 6, 6, 8, 3, 4, 6, 6, 3, 0, 4, 5, 5, 3, 8, 0, 3, 3, 2, 2, 4, 0, 5, 7, 6, 6, 6, 4, 0, 4, 2, 8, 2, 1, 6, 3, 1, 0, 0, 5, 4, 1, 8, 9, 6, 1, 1, 2, 9, 0, 6, 7, 1, 9, 9, 6, 1, 7, 2, 2, 1, 6, 2, 9, 8, 5, 5, 1, 7, 6, 9, 1, 1, 8, 7, 9, 7, 8, 6, 8, 8, 1, 7, 1, 7, 6, 8, 2, 5, 9, 3, 0, 6, 8, 6, 3, 4, 9, 9, 4, 4, 6, 6, 7, 6, 0, 2, 8, 3, 2, 1, 3, 6, 9, 9, 4, 4, 4, 9, 1, 1, 0, 4, 3, 6, 5, 4, 6, 9, 5, 7, 7, 6, 4, 8], ......,[8, 6, 3, 0, 0, 7, 1, 3, 8, 9, 3, 5, 3, 2, 3, 5, 2, 8, 2, 8, 3, 4, 7, 4, 9, 3, 8, 4, 0, 2, 3, 3, 4, 3, 8, 3, 5, 1, 3, 1, 4, 9, 3, 4, 0, 7, 8, 9, 7, 1, 0, 1, 1, 9, 0, 4, 5, 3, 7, 5, 1, 6, 2, 9, 9, 6, 8, 4, 6, 7, 7, 0, 1, 2, 1, 9, 4, 8, 9, 4, 6, 6, 3, 4, 7, 3, 8, 1, 8, 3, 2, 0, 4, 8, 4, 8, 0, 5, 1, 4, 2, 6, 2, 9, 3, 6, 7, 2, 6, 1, 5, 6, 0, 5, 8, 4, 6, 7, 0, 4, 1, 3, 7, 5, 6, 8, 6, 2, 4, 9, 6, 9, 0, 4, 6, 7, 5, 9, 4, 0, 7, 7, 2, 6, 9, 0, 1, 5, 1, 8]]
    - **What are the input digit (0 - 9)**
    - Each input digit is the edge device id. Initially there are 10 input edge devices so the digits are from 0 to 9.
    -  **What is the length of individual**
    -  The length of individual is equall to the number of task (i.e 150)
    -  **What is the maximum execution time?**
    -   max(sum of time taken by each edge devices)
    - **What is the expected output of the program?**
     - The output is
     - **Edge Device 0:** 11 15 22 33 34 41 46 58 62 71 83 85 87 89 149
     - **Edge Device 1:** 5 26 29 39 51 68 82 86 106 118 119 127 134 148
     - **Edge Device 2:** 8 9 19 32 36 57 70 73 95 97 117 120 132 133 135 138 146
     - **Edge Device 3:** 3 10 35 66 72 74 88 109 112 115 143
     - **Edge Device 4:** 14 42 52 53 55 56 76 78 90 104 111 116 124 128 131 142
     - **Edge Device 5:** 4 16 20 25 28 30 44 59 61 65 84 102 105 108 123 140
     - **Edge Device 6:** 1 7 12 17 37 43 54 60 63 64 69 96 125 129 130 147
     - **Edge Device 7:** 0 6 18 21 24 31 47 48 77 80 91 98 99 110 113 139 144
     - **Edge Device 8:** 2 13 23 45 67 75 100 101 114 121 122 126 136 137
     - **Edge Device 9:** 27 38 40 49 50 79 81 92 93 94 103 107 141 145
     - **Total execution time is:** 10.89s

  2. Stopping criteria   
    The program will be stopped if one of the following crieteria is meet
     - The fitness value is greater than the input threshold.
     - If the fitness values remains constant for more than 15 times.
     - If the number of generations is greater than maximum Generation 
     - We stop the function either when the task is complete or exceeds the fixed time interval. 
  3. Fitness function
     - fitness_score = max([sum of task executed Edge1, ....., Sum of tasks executed in EdgeN ]) 

  4. Selection operator
     - We use roulette tournament selection
  5. Crossover operator
     - We use single point crossover
  6. Mutation operator
     - For mutation operator, task are randomly selected and local modification is performed.
  7. Generational selection strategy
     - For Generational selection strategy, we use the Generation Replacement
 ### 4. How to run your project
```bash
root@manish:~$ python app.py
```
 ### 4. How to adjust parameters.
- The program allows to modify the following input inside main function
  - popSize = 1000
  - noOfEdge = 10
  - noOfTask = 170
  - maxGen = 100
  - threshold = 170
  - maxRepeat = 15
  - maxTime = 1200


