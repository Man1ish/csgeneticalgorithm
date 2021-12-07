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


# tournament selection
def selection(pop, scores, k=3):
    # first random selection
    pop_copy = copy.deepcopy(pop)
    selection_ix = random.randint(0,len(pop))
    for ix in random.randint(0,len(pop)):
        # check if better (e.g. perform a tournament)
        if scores[ix] < scores[selection_ix]:
            selection_ix = ix
    return pop[selection_ix]


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


def selectionAlgorithm(pop, fitnessScore, executionTime):
    bounds = list(itertools.accumulate(
        1 / l for l in fitnessScore
    ))



    pick = random.random() * bounds[-1]

    i = 0

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



def tournament_selection(pop, executionTime):

  pop_copy = cp.deepcopy(pop)
  parents = random.choices(pop_copy, k=5)
  # select the first indivisual
  first = 0
  firstIdx = 0
  for idx in range(len(parents)):
    f1 = fitness(executionTime, parents[idx])
    if first < f1:
      first = f1
      firstIdx = idx

  aParent = parents[firstIdx]
  pop_copy.remove(parents[firstIdx])

  # select the second indivisual
  parents = random.choices(pop_copy, k=5)
  second = 0
  secondIdx = 0
  for idx in range(len(parents)):
    f1 = fitness(executionTime, parents[idx])
    if second < f1:
      second = f1
      secondIdx = idx

  bParent = parents[secondIdx]
  return aParent, bParent




def main():
    # Population Size
    popSize = 1000
    maxGen = 100
    noOfEdge = 10
    noOfTask = 150
    threshold = 170
    maxRepeat = 15
    maxTime = 60

    d = Dataset("edge", noOfTask, noOfEdge)
    population = d.generatePopulation(popSize)
    executionTime = d.executionTime(noOfTask, noOfEdge)


    finalOutput = []

    best_so_far = 10000
    t0 = time.time()
    currentGeneration = 0
    eval_with = partial(fitness, executionTime)


    repeat = 0
    exitLoop = True

    while exitLoop:
        fitnessScore = []
        for ind in population:
            score = fitness(executionTime, ind)
            fitnessScore.append(score)

        # print(f"fitness score is {min(fitnessScore)}")

        sortedPopulation = sorted(
            population, key=eval_with, reverse=False)

        latestFitnessValue = fitness(executionTime, sortedPopulation[0])
        # print(latestFitnessValue)
        # print(sortedPopulation[0])



        if best_so_far > latestFitnessValue:
            best_so_far = latestFitnessValue
            currentGeneration += 1
            repeat += 1
            print('=' * 40)
            print(f'Number of Generation: {currentGeneration}')
            print(f'Best results so far: {best_so_far}')
            print(f'Individual: {sortedPopulation[0]}')
            maxRepeat = 0


        nextPop = cp.deepcopy(population)

        for _ in range(int(popSize / 2)):


            # selectionAlgorithm(population, fitnessScore,executionTime)
            # aParent, bParent = tournamentSelection(population, executionTime)
            aParent, bParent = randomSelection(population, fitnessScore)
            # aParent, bParent = selectionAlgorithm(population, fitnessScore,executionTime)

            if random.uniform(0, 100) <= 75:
                crossing_point = random.randint(1, popSize - 1)
                aOffspring = aParent[:crossing_point] + bParent[crossing_point::]
                bOffspring = bParent[:crossing_point] + aParent[crossing_point::]


                nextPop.append(aOffspring)
                nextPop.append(bOffspring)


            #Mutation
            for idx in range(int(popSize/2)):
                if random.uniform(0, 100) < 5:
                    newInd = sortedPopulation[idx].copy()
                    newInd[random.randint(0, noOfTask -1)] = random.choice(newInd)



        sortedNextPop = cp.deepcopy(sorted(nextPop, key=eval_with, reverse=False))
        population = sortedNextPop[:popSize]
        maxRepeat += 1
        eplasedTime = time.time() - t0
        if ((currentGeneration > maxGen) or (repeat > maxRepeat) or (best_so_far < threshold) or (eplasedTime > maxTime)):
            exitLoop = False
            finalOutput = population[0]

        # print(population)

    workingTime = time.time() - t0


    #Shows results
    print("="*20+" Results "+"="*20)
    outputString = ["The output is"]
    for l in set(finalOutput):
        outputString.append(f"Edge Devices {l}: " + ' '.join([
            str(i) for i in range(len(finalOutput)) if finalOutput[i] == l
        ]))

    print('\n'.join(outputString))
    print('Total execution time is '+str(workingTime)+' s')


if __name__ == '__main__':
    main()
