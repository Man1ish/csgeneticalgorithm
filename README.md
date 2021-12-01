### Name: Manish Pandey
### Roll No: 2021327158

### 1. Justification of why you have chosen your topic.
 In our previous paper, **"[Here, There, Anywhere: Profiling-Driven Services to Tame the Heterogeneity of Edge Applications] (https://ieeexplore.ieee.org/document/9592388)"**, we proposed a profiling-based methodology that effectively matches edge computational tasks with the available devices to best satisfy programmer-defined non-functional requirements. In this project, I want to extend my paper and include a genetic algorithm to efficiently schedule tasks to the edge devices based on task priority and its dependency. There can be multiple tasks, and task might includes some dependency with other task as well as task can have different level of priority.  
![Solution](https://pandeymanish.com/images/solution.png) 

Solution of the proposed problem


### 2. What is the topic?
**A Genetic Algorithm to schedule task in edge computing**
### 3. Design decision explaining why you select:
  1. Parameters such as the size of an initial population 
     - Initially, we select the size of population as 100, however, it can be adjusted to obtain optimal solution    
  2. Stopping criteria   
     - We stop the function either when the task is complete or exceeds the fixed time interval. 
  3. Fitness function
     - To evaluate the fitness function, we will use the sum total execution time with the proiority of tasks. 
  4. Selection operator
     - We will use the we use roulette wheel selection, where each solution has random chances.
  5. Crossover operator
     - In the crossover, we will use the product of adjacent matrics. 
  6. Mutation operator
     - For mutation operator, we will randomly choose the task. 
  7. Generational selection strategy
     - For Generational selection strategy, we use the Generation Replacement
 ### 4. How to run your project
```bash
root@manish:~$ python app.py
```
 ### 4. How to adjust parameters.

