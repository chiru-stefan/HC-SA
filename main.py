
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

# from threading import Thread
#
# t = []
# for _ in range(10):
#     th = Thread(target=ga)
#     th.run()
#     t.append(th)
#
# for _ in range(10):
#     t[_].join()
#

from concurrent.futures import ThreadPoolExecutor



executor = ThreadPoolExecutor(10)
future = executor.submit(ga)



# [ga() for x in range(10)]