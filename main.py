
def hc():
    from hc import hc

    obj = hc.Main()
    initial_state = obj.generate_initial_state()
    obj.driver()


def sa():
    from sa import sa

    obj = sa.Main()
    initial_state = obj.generate_initial_state()
    obj.driver()


def ga():
    from ga import ga

    obj = ga.Main()
    initial_state = obj.generate_initial_states()
    [print(x) for x in initial_state]
    obj.driver()

# hc()
# sa()
ga()