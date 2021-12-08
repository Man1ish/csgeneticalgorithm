import copy
import itertools
import random
import time
import sys
import copy as cp

# Create Initial Population
from functools import partial


def createInitPop(psize, dim):
    pop = []
    for idx in range(psize):
        pop.append(createIndividual(dim))
    return pop


# Create Individual
def createIndividual(dim, edgeNumber, taskNumber):
    ind = []
    for idx in range(dim):
        ind.append([random.choice(list(range(edgeNumber)))
                    for i in range(taskNumber)])
    return ind


class Dataset():
    # The class generate the dataset
    def __init__(self, name, noOfTask, noOfEdge):
        self.name = name
        self.noOfTask = noOfTask
        self.noOfEdge = noOfEdge

    @classmethod
    def executionTime(cls, noOfTask, noOfEdge):
        if noOfEdge < 1 or noOfTask < 1:
            raise ValueError("Number of edge or task should be atleast one")
        tasks = [round(random.uniform(2, 50), 2) for _ in range(noOfTask)]
        return tasks

    @classmethod
    def priority(cls, noOfTask, noOfEdge):
        if noOfEdge < 1 or noOfTask < 1:
            raise ValueError("Number of edge or task should be atleast one")
        return [random.randint(0, 10) for _ in range(noOfTask)]

    def generateIndividual(self):
        return [random.choice(list(range(self.noOfEdge)))
                for i in range(self.noOfTask)]

    def generatePopulation(self, popSize):
        return [self.generateIndividual()
                for _ in range(popSize)]


# This function provides the maximimum execution time when task are schedule in edge devices
def fitness(executionTime, ind):
    maxValue = max(ind)

    edgeExecutionTime = [0] * (maxValue+1)

    for task, edge in enumerate(ind):
        edgeExecutionTime[edge] += executionTime[task]

    score = max(edgeExecutionTime)

    return score


# Random Selection Algorithm
def randomSelection(pop, answer):
    aParent = random.choice(pop)
    bParent = random.choice(pop)

    return aParent, bParent



#Old tournament Selection Function
def tournamentSelection(pop, executionTime):
    pop_copy = cp.deepcopy(pop)
    parents = random.choices(pop_copy, k=5)

    first = 1000
    firstIdx = 0
    for idx in range(len(parents)):
        f1 = fitness(executionTime, parents[idx])
        if first < f1:
            first = f1
            firstIdx = idx

    aParent = parents[firstIdx]
    pop_copy.remove(parents[firstIdx])

    #select second best individual
    parents = random.choices(pop_copy, k=5)
    second = 1000
    secondIdx = 0
    for idx in range(len(parents)):
        f2 = fitness(executionTime, parents[idx])
        if second < f2:
            second = f2
            secondIdx = idx
    bParent = parents[secondIdx]
    return aParent, bParent


# Roulette wheel selection algorithm
def roulette_wheel(population, fitnesses):
    num = 2
    total_fitness = float(sum(fitnesses))
    rel_fitness = [f / total_fitness for f in fitnesses]
    # Generate probability intervals for each individual
    probabilities = [sum(rel_fitness[:i + 1]) for i in range(len(rel_fitness))]
    # print(probabilities)

    # Draw new population
    selected = []
    for n in range(num):
        r = random.random()

        for (i, individual) in enumerate(population):
            if r >= probabilities[i]:
                selected.append(individual)
                break
    return selected[0], selected[1]

#Mixture of tournament selection with random selection
def selectionAlgorithm(pop, fitnessScore, executionTime):
    bounds = list(itertools.accumulate(
        1 / l for l in fitnessScore
    ))

    pick = random.random() * bounds[-1]



    popCopy = cp.copy(pop)
    first = 1000
    selectedPopulation = []
    selectedFitnessScore = []
    for ch, bound in zip(popCopy, bounds):
        if pick < bound:
            f1 = fitness(executionTime, ch)

            if f1 < first:
                first = f1
                selectedPopulation.append(ch)
                selectedFitnessScore.append(f1)

    if (len(selectedPopulation) > 1):
        sortedData = sorted(enumerate(selectedFitnessScore), key=lambda x: x[1])
        firstSelection = sortedData[0][0]
        secondSelection = sortedData[1][0]
        return selectedPopulation[firstSelection], selectedPopulation[firstSelection]
    else:
        aParent = random.choice(popCopy)
        bParent = random.choice(popCopy)

        return aParent, bParent





def main():
    popSize = 1000  # Population Size
    maxGen = 100    # Maximum Generation
    noOfEdge = 10   # No of Edge
    noOfTask = 150  # No of Task
    threshold = 170 # Maximum threshold value
    maxRepeat = 10  # Maximum Repeat
    maxTime = 300   # Maximum Execution time in seconds

    #Generate the dataset
    d = Dataset("edge", noOfTask, noOfEdge)
    population = d.generatePopulation(popSize)
    executionTime = d.executionTime(noOfTask, noOfEdge)


    #Initialize variables
    finalOutput = []
    best_so_far = 10000
    t0 = time.time()
    currentGeneration = 0
    eval_with = partial(fitness, executionTime)
    repeat = 0
    exitLoop = True
    lastFitnessScore = 0
    loopTimes = 0
    initialScore = 0


    while exitLoop:
        #Record the fitness value
        fitnessScore = []
        for ind in population:
            score = fitness(executionTime, ind)
            fitnessScore.append(score)


        sortedPopulation = sorted(
            population, key=eval_with, reverse=False)
        latestFitnessValue = fitness(executionTime, sortedPopulation[0])

        if loopTimes == 0:
            initialScore = latestFitnessValue

        if (latestFitnessValue == lastFitnessScore):
            repeat += 1
        else:
            repeat = 0

        lastFitnessScore = latestFitnessValue


        if best_so_far > latestFitnessValue:
            best_so_far = latestFitnessValue
            currentGeneration += 1
            repeat += 1
            print('=' * 40)
            print(f'Number of Generation: {currentGeneration}')
            print(f'Best results so far: {best_so_far}')
            print(f'Individual: {sortedPopulation[0]}')



        nextPop = cp.deepcopy(population)

        for _ in range(int(popSize / 2)):


            # selectionAlgorithm(population, fitnessScore,executionTime)
            # aParent, bParent = tournamentSelection(population, executionTime)
            # aParent, bParent = randomSelection(population, fitnessScore)
            aParent, bParent = selectionAlgorithm(population, fitnessScore,executionTime)

            # Cross Over
            if random.uniform(0, 100) <= 75:
                crossing_point = random.randint(1, popSize - 1)

                # print(aParent[::crossing_point])


                aOffspring = aParent[:crossing_point] + bParent[crossing_point::]
                bOffspring = bParent[:crossing_point] + aParent[crossing_point::]


                nextPop.append(aOffspring)
                nextPop.append(bOffspring)


            #Mutation
            for idx in range(int(popSize/4)):
                if random.uniform(0, 100) < 5:
                    newInd = sortedPopulation[idx].copy()
                    newInd[random.randint(0, noOfTask -1)] = random.choice(newInd)
                    nextPop.append(newInd)



        sortedNextPop = cp.deepcopy(sorted(nextPop, key=eval_with, reverse=False))
        population = sortedNextPop[:popSize]
        eplasedTime = time.time() - t0
        if ((currentGeneration > maxGen) or (repeat > maxRepeat) or (best_so_far < threshold) or (eplasedTime > maxTime)):
            exitLoop = False
            finalOutput = population[0]

        # print(population)

        loopTimes += 1

    workingTime = time.time() - t0


    #Shows results
    print("="*23+" Results "+"="*23)
    outputString = ["The output is"]
    for l in set(finalOutput):
        outputString.append(f"Edge Devices {l}: " + ' '.join([
            str(i) for i in range(len(finalOutput)) if finalOutput[i] == l
        ]))

    print('\n'.join(outputString))
    print(f"Total execution time is "+"{:.2f}".format(workingTime)+'s')
    print(f"Initial execution time is "+"{:.2f}".format(initialScore)+'s')
    print(f"Best execution time is "+"{:.2f}".format(best_so_far)+'s')



if __name__ == '__main__':
    main()
