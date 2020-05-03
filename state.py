import itertools
import random

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
        print("State primit: ", state)
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
    def get_neighbor(state, no_=1):
        '''
            Because there are no "new" neighbors (all neighbors are already known from the first state)
            We can generate new states and simply compare the path cost
        '''

        no_vert = len(state.split('-')) # number of edges

        state_split = state.split('-')
        pos = random.randint(1, no_vert%13)
        n_state = [x for x in state_split]
        for x in range(1,no_vert):
            n_state[x], n_state[pos] = n_state[pos], n_state[x]
            pos = random.randint(1, no_vert % 13)

        return n_state

