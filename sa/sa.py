from state import obj
import random


class Main:
    VERTICES            = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13']
    already_generated   = []
    edges               = dict()
    state               = None
    TEMPERATURE         = 1000
    L                   = 10
    r                   = .95
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
        self.state = obj(edges=self.edges)


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
        while self.TEMPERATURE:
            for i in range(self.L):
                ng = self.state.get_neighbor(state=self.INIT_STATE)
                print("State: ", self.INIT_STATE, " neighbor: ", ng)

                nstate = '-'.join(ng)
                nweight = self.state.eval(nstate)
                delta = self.state.eval(nstate) - self.state.eval(self.INIT_STATE)
                print("Delta: ", delta)
                if delta <= 0:
                    self.INIT_STATE = nstate
                else:
                    if random.random() < pow(2, (-1)*(delta/self.TEMPERATURE)): #
                        print("good probab")
                        self.INIT_STATE = nstate
                    self.min_weight = nweight
            self.TEMPERATURE *= self.r
            if self.TEMPERATURE < float("2.053726463766204e-15"):
                break
        print(self.INIT_STATE, self.min_weight)




