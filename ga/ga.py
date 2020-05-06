from state import obj
import random
from numpy import interp
import numpy as np
'''
Vertices: from 0-13
Edges: all edges are connected (Complete Graph): https://mathworld.wolfram.com/CompleteGraph.html
Weights: FP numbers <-> in the symmetric TSP, the distance between two cities is the same in each opposite direction, forming an undirected graph.
Goal: find the shortest path
Start node: 0
Goal node: 13
Number of all possible permutations: 14! = 87178291200
'''


class Main:
    VERTICES            = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13']
    NO_VERTICES         = 14
    already_generated   = []
    edges               = dict()
    state               = None
    MAX_ITER            = 1000
    INIT_POP            = None      # initial population
    # -> list of list of fitness_score and dict [{1:state},{1:state},{0:state}...]
    min_weight          = 0
    START_POP_NO        = 4        # initial population will have 10 elements
    fitness             = None
    mating_pairs        = None
    offspring           = None
    mutation            = None

    def __init__(self):
        with open("m_burma.csv",'r') as f:
            contents = f.read().split('\n')
            f.close()

        for l in contents[1:]:
            self.edges[l.split(',')[0]] = l.split(',')[1]
        print("Edges: ", self.edges)
        self.state = obj(edges=self.edges)


    def generate_initial_states(self):      # generate population
        self.INIT_POP = [[None, dict()] for _ in range(self.START_POP_NO)]

        for x in range(self.START_POP_NO):
            taken = []
            while len(taken) < len(self.VERTICES):
                for i in range(len(self.VERTICES)):
                    if random.random() > .5 :
                        if self.VERTICES[i] not in taken:
                            taken.append(self.VERTICES[i])
            temp = tuple(taken)

            self.INIT_POP[x]= [ self.state.eval(temp), {'1':temp} ]
        return self.INIT_POP


    def crossover(self, pair_1, pair_2):
        offspring = []
        for i, v in enumerate(pair_1[:-1]):
            choice_1 = random.randint(1, self.START_POP_NO - 2)  # index 1 , index n-2
            temp = list(pair_1[i][1]['1'])
            temp2 = list(pair_1[i+1][1]['1'])
            child_1 = temp[:choice_1]
            cpy = list(tuple([x for x in temp2 if x not in child_1]))
            child_1.extend(cpy)
            offspring.append(child_1)

        for i, v in enumerate(pair_2[:-1]):
            choice_1 = random.randint(1, self.START_POP_NO - 2)  # index 1 , index n-2
            temp = list(pair_2[i][1]['1'])
            temp2 = list(pair_2[i+1][1]['1'])
            child_1 = temp[:choice_1]
            cpy = list(tuple([x for x in temp2 if x not in child_1]))
            child_1.extend(cpy)
            offspring.append(child_1)


        # print('child1: ', offspring)
        # choice_1 = random.randint(1, self.START_POP_NO - 2) # index 1 , index n-2
        # temp = list(pair_1[0][1]['1'])
        # temp2 = list(pair_1[1][1]['1'])
        # child_1 = temp[:choice_1]
        # cpy = list(tuple([x for x in temp2 if x not in child_1]))
        # child_1.extend(cpy)
        # print('child1: ', child_1)
        #
        # exit(1)
        #
        # child_2 = temp2[:choice_1]
        # cpy = list(tuple([x for x in temp if x not in child_2]))
        # child_2.extend(cpy)
        #
        # choice_1 = random.randint(1, self.START_POP_NO - 2)  # index 1 , index n-2
        # temp = list(pair_2[0][1]['1'])
        # temp2 = list(pair_2[1][1]['1'])
        # child_3 = temp[:choice_1]
        # cpy = list(tuple([x for x in temp2 if x not in child_3]))
        # child_3.extend(cpy)
        #
        # child_4 = temp2[:choice_1]
        #
        # cpy = list(tuple([x for x in temp if x not in child_4]))
        # child_4.extend(cpy)

        # return [child_1, child_2, child_3, child_4]
        return offspring

    def mutation(self, children):
        mutated = []
        for c in children:
            # if (some small probability) => mutate
            if self.state.eval(c) > (self.f_min + self.f_max)/2 :
                # print('c_begin: ', c)
                n_1 = random.randint(0, self.NO_VERTICES-1)
                n_2 = random.randint(0, self.NO_VERTICES-1)
                temp = c[n_1]
                c[n_1]=c[n_2]
                c[n_2]=temp
            mutated.append(c)

        return mutated


    def select_best(self, mutated):
        # print('mutated: ', mutated)
        # print('fit scores: ', self.fitness)
        mo = np.array(mutated)[np.array(self.fitness).argsort()].tolist()
        # print(mo)
        tr = [ [x, {'1':tuple(mo[i])}] for i,x in enumerate(self.fitness)]
        print('tr: ', tr)
        return tr


    def driver(self):
        # rank by fitness
        self.f_min = min([x[0] for x in self.INIT_POP])
        self.f_max = max([x[0] for x in self.INIT_POP])

        weights = [(-1)*x[0] for x in self.INIT_POP]

        # print('sorted: ', np.array(self.INIT_POP)[np.array(weights).argsort()])

        mapping = interp(weights, [-self.f_max, -self.f_min], [.2, .4])   # will be used to select the individual with the best fit
        # print('mapping: ', mapping)

        number_of_offspring = self.START_POP_NO
        for i in range(self.MAX_ITER):
            # select 2 pairs based on the mapping
            # choice_1 = random.choices(range(self.START_POP_NO),mapping)
            # choice_2 = random.choices(range(self.START_POP_NO),mapping)
            # print(choice_1, choice_2)
            make_choice = lambda : random.choices(range(self.START_POP_NO),mapping)[0]

            pair_1 = [ self.INIT_POP[make_choice()] for _ in range(number_of_offspring)]
            pair_2 = [ self.INIT_POP[make_choice()] for _ in range(number_of_offspring)]

            # print('pair_1: ', pair_1)
            # print('pair_2: ', pair_2)


            # crossover
            to_mutation = self.crossover(pair_1, pair_2)
            # print('crossover: ', to_mutation)
            # mutation
            mutated = self.mutation(to_mutation)
            # print('mutated: ', mutated)
            if self.fitness is None:
                self.fitness = self.state.fitness_function(mutated, self.edges)
            else:
                if sum(self.fitness) > sum(self.state.fitness_function(mutated, self.edges)):
                    self.fitness = self.state.fitness_function(mutated, self.edges)
                    self.INIT_POP = self.select_best(mutated)           # Current population is the best population


        print('Final: ', sum(self.fitness), '\nBest individual: ', min(self.fitness))
