import state as st
import random

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
    already_generated   = []
    edges               = dict()
    state               = None
    MAX_ITER            = 1000
    INIT_STATE          = None
    min_weight          = 0
    START_NODE          = 0


    def __init__(self):
        with open("m_burma.csv",'r') as f:
            contents = f.read().split('\n')
            f.close()

        for l in contents[1:]:
            self.edges[l.split(',')[0]] = l.split(',')[1]
        print("Edges: ", self.edges)
        self.state = st.State(edges=self.edges)


    def generate_initial_state(self):
        taken = [self.VERTICES[self.START_NODE]]
        while len(taken) < len(self.VERTICES):
            for i in range(len(self.VERTICES)):
                if random.random() > .5 :
                    if self.VERTICES[i] not in taken:
                        taken.append(self.VERTICES[i])
        self.INIT_STATE = '-'.join(taken)
        self.min_weight = self.state.eval(self.INIT_STATE)
        return self.INIT_STATE


    def driver(self):

        for i in range(self.MAX_ITER):
            ngs = self.state.get_neighbor(state=self.INIT_STATE)
            print("init state: ", self.INIT_STATE)

            nstate = '-'.join(ngs)
            nweight = self.state.eval(nstate)

            if nweight < self.min_weight:
                self.INIT_STATE = nstate
                self.min_weight = nweight


        print(self.INIT_STATE, self.min_weight)


obj = Main()
initial_state = obj.generate_initial_state()
obj.driver()

