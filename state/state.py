import itertools
import random
from os import getrandom

class State:
    '''
        State example: 0-1-2-3-4-5-6-7-8-9-10-11-12-13
        Swap: 0-2-1-3-4-5-6-7-8-9-10-11-12-13
        Eval: w(0-2) + w(2-1) + w(1-3)...
    '''

    state        = None
    total_weight = None
    edges        = None
    NO_SHUFFLES  = 2


    def __init__(self, s=None, t=None, edges=None):
        self.state = s
        self.total_weight = t
        self.edges = edges


    def eval(self, state):
        # print("State primit: ", state)
        try:
            links = state.split('-')
        except:
            links = state
        s_weights = .0
        for i, x in enumerate(links[:-1]):
            try:
                s_weights += float(self.edges[links[i]+'-'+ links[i+1]])
            except:
                s_weights += float(self.edges[links[i+1]+'-'+ links[i]])

        return s_weights


    @staticmethod
    def get_neighbor(state, seed=1):
        '''
            Because there are no "new" neighbors (all neighbors are already known from the first state)
            We can generate new states and simply compare the path cost
        '''
        random.seed(a=getrandom(5), version=2)
        no_vert = len(state.split('-')) # number of edges
        state_split = tuple(state.split('-'))
        pos = list()
        n_state = [x for x in state_split]

        while len(pos) < no_vert:
            pos.append(random.randint(1, no_vert-1 ))
        pos = list(pos)
        for x in range(1,no_vert):
            # print("init state: ", state, "neighbor: ", n_state)
            n_state[x], n_state[pos[x]] = n_state[pos[x]], n_state[x]

        return n_state

