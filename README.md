### 1. Justification of why you have chosen your topic.
 In our previous paper, **"[Here, There, Anywhere: Profiling-Driven Services to Tame the Heterogeneity of Edge Applications] (https://ieeexplore.ieee.org/document/9592388)"**, we proposed a profiling-based methodology that effectively matches edge computational tasks with the available devices to best satisfy programmer-defined non-functional requirements. In this project, I want to extend my paper and include a genetic algorithm to efficiently schedule tasks to the edge devices based on task priority and its dependency. There can be multiple tasks, and task might includes some dependency with other task as well as task can have different level of priority.  





### 2. What is the topic?
**A Genetic Algorithm to schedule task in edge computing**
### 3. Design decision explaining why you select:

![Solution](https://pandeymanish.com/images/solution.png) 

  1. Input Parameter
     - Population Size: 1000
     - Number of edge devices: 5
     - Number of tasks: 7
     - Length of each task: random from 1 to 20 seconds
     - Task Dependency: Half of tasks has no dependency, and other half tasks are dependent to one of the early half task
     - Task Priority: Chosen randomly
     - Threshold to complete the task = 100 seconds 
     - Initially, we select the size of population as 100, however, it can be adjusted to obtain optimal solution    
     - max_generation_value = 200
     - time_weight = 0.8
     - priority_weight = 0.2
     > Each of the input can be modify based on the requirement of users

    - Initialize 
     - Total_time = sum of all tasks (t1+ t2 + t3 + t4 + t5 + t6 + t7)
     - Priority_time = sum of each task (time * priority)
  2. Stopping criteria   
    The program will be stopped if one of the following crieteria is meet
     - The fitness value is greater than the input threshold.
     - If the fitness values remains constant for more than 10 times.
     - If the number of generations is greater than max_generation_value 
     - We stop the function either when the task is complete or exceeds the fixed time interval. 
  3. Fitness function
     - If population schedule has unique task append 0 to fitness list
     - task_completion_time = maximum of task completion
     - if task_completion_time > threshold_time:  append 0 to the fitness list
     - task_priority_time = sum of each task (time * priority)
     - fitness_value = round(time_weight * (Total_time - task_completion_time) + priority_weight * (priority_time - task_priority_time))
     - append fitness_value to the fitness list
  4. Selection operator
     - We use roulette wheel selection, where each solution has random chances.
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


