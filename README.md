### 1. Justification of why you have chosen your topic.
 In our previous paper, **"[Here, There, Anywhere: Profiling-Driven Services to Tame the Heterogeneity of Edge Applications] (https://ieeexplore.ieee.org/document/9592388)"**, we proposed a profiling-based methodology that effectively matches edge computational tasks with the available devices to best satisfy programmer-defined non-functional requirements. In this project, I want to extend my paper and include a genetic algorithm to efficiently schedule tasks to the edge devices based on the execution time of the task. The main idea is to complete task in limited amount of time. 
 


The edge computing paradigm is introduced to overcome the limitation of cloud computing by bringing storage and processing near edge devices. In edge computing, edge server needs to effectively address the scarcity of heterogeneous resources to achieve edge processing performance goals. Our previous paper manages these scarcity issues by assigning the task to the best computing devices. 

![Solution](https://pandeymanish.com/images/task-assignment.jpg)

The above figure shows the task assigned to the edge devices. When the task is assigned randomly to the edge devices, we can't meet the objective of edge computing. This project aims to use the genetic algorithm to reduce the execution task time by selecting appropriate edge devices when there is n number of tasks.


![Solution](https://pandeymanish.com/images/gn_edge_computing.jpg)







### 2. What is the topic?
**A Genetic Algorithm to schedule task in edge computing**
### 3. Design decision explaining why you select:

![Solution](https://pandeymanish.com/images/solution.png)

In the above diagram, there are 5 tasks (T1, T2, T3, T4, and T5) and 3 edge nodes(E1, E2, and E3). The goal is to schedule task to the appropriate edge devices so that all task can be completed in limited amount of time. 



  1. **Input Parameter**
     - **Population Size (popSize):** 1000 
     - **Number of edge devices (noOfEdge):** 10
     - **Number of tasks (noOfTask):** 150
     - **Execution Time of each task:** Currently execution time is set randomly from 2 to 50 seconds 
     - **Threshold (threshold):** 70s
     - **Maximum Repeat (maxRepeat):** 15
     -  **Maximum Generation (maxGen):** 15
     -  **Maximum Running Time in seconds (maxTime):** 1200



     Each of the input can be modify based on the requirement of users
    

**How population and individual looks like**

     [[8, 3, 1, 8, 3, 4, 2, 4, 1, 6, 9, 6, 1, 2, 6, 7, 6, 6, 8, 3, 4, 6, 6, 3, 0, 4, 5, 5, 3, 8, 0, 3, 3, 2, 2, 4, 0, 5, 7, 6, 6, 6, 4, 0, 4, 2, 8, 2, 1, 6, 3, 1, 0, 0, 5, 4, 1, 8, 9, 6, 1, 1, 2, 9, 0, 6, 7, 1, 9, 9, 6, 1, 7, 2, 2, 1, 6, 2, 9, 8, 5, 5, 1, 7, 6, 9, 1, 1, 8, 7, 9, 7, 8, 6, 8, 8, 1, 7, 1, 7, 6, 8, 2, 5, 9, 3, 0, 6, 8, 6, 3, 4, 9, 9, 4, 4, 6, 6, 7, 6, 0, 2, 8, 3, 2, 1, 3, 6, 9, 9, 4, 4, 4, 9, 1, 1, 0, 4, 3, 6, 5, 4, 6, 9, 5, 7, 7, 6, 4, 8], ......,[8, 6, 3, 0, 0, 7, 1, 3, 8, 9, 3, 5, 3, 2, 3, 5, 2, 8, 2, 8, 3, 4, 7, 4, 9, 3, 8, 4, 0, 2, 3, 3, 4, 3, 8, 3, 5, 1, 3, 1, 4, 9, 3, 4, 0, 7, 8, 9, 7, 1, 0, 1, 1, 9, 0, 4, 5, 3, 7, 5, 1, 6, 2, 9, 9, 6, 8, 4, 6, 7, 7, 0, 1, 2, 1, 9, 4, 8, 9, 4, 6, 6, 3, 4, 7, 3, 8, 1, 8, 3, 2, 0, 4, 8, 4, 8, 0, 5, 1, 4, 2, 6, 2, 9, 3, 6, 7, 2, 6, 1, 5, 6, 0, 5, 8, 4, 6, 7, 0, 4, 1, 3, 7, 5, 6, 8, 6, 2, 4, 9, 6, 9, 0, 4, 6, 7, 5, 9, 4, 0, 7, 7, 2, 6, 9, 0, 1, 5, 1, 8]]


     
**Individual explanation**

The individual is the collection of task assigned to the particular edge devices. Suppose individual has value 8 in first place then the first task is assign to the edge device 8.


**What are the input digit (0 - 9)**

Each input digit is the edge device id. Initially there are 10 input edge devices so the digits are from 0 to 9.

**What is the length of individual**

The length of individual is equall to the number of task (i.e 150)


**What is the maximum execution time?**

max(sum of time taken by each edge devices)

**What is the expected output of the program?**
     
    The output is
    Edge Devices 0: 28 32 42 46 89 90 91 92 102 114 115 142 144 148
    Edge Devices 1: 3 6 22 25 26 38 45 52 53 63 68 73 97 107 110 126
    Edge Devices 2: 1 9 27 30 35 40 54 58 60 113 116 121 129 132 141
    Edge Devices 3: 14 48 50 62 94 95 103 105 118 124 131 134 147
    Edge Devices 4: 7 47 51 59 75 78 81 93 96 100 109 119 137 139 140
    Edge Devices 5: 0 8 12 31 36 41 49 57 70 72 77 108 143 146
    Edge Devices 6: 10 11 17 44 64 67 80 85 86 98 101 111 117 128 130 138 149
    Edge Devices 7: 2 5 15 24 33 37 61 65 69 83 84 88 122 123 135 145
    Edge Devices 8: 20 29 34 39 43 56 66 74 76 82 99 104 125 133 136
    Edge Devices 9: 4 13 16 18 19 21 23 55 71 79 87 106 112 120 127
    Total execution time is 147.89s
    Initial execution time is 458.62s
    Best execution time is 398.71s


  2. Stopping criteria   
    The program will be stopped if one of the following criteria is meet
     - The fitness value is greater than the input threshold.
     - If the score value remains constant for more than maxRepeat input
     - If the number of generations is greater than maximum Generation 
     - We stop the function either when the task is complete or exceeds the fixed time interval. 
  3. Fitness function
     - fitness_score = max([sum of task executed Edge1, ....., Sum of tasks executed in EdgeN ]) 

  4. Selection operator
     - For selection operator, we merge the tournament selection with random selection
  5. Crossover operator
     - We use single point crossover
     ![Alt text](crossover1.png?raw=true "Crossover Point")
     ![Alt text](crossover2.png?raw=true "Single Point Crossover")
     - 
  6. Mutation operator
     - For mutation operator, we use Elitism. It choose M best individual from the parent's generation.
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
  - noOfTask = 150
  - maxGen = 100
  - threshold = 170
  - maxRepeat = 10
  - maxTime = 600


