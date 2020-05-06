
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


from threading import Thread

ths = []
for _ in range(10):
    thread = Thread(target=ga)
    thread.start()
    ths.append(thread)

import time


for _ in range(10):
    if ths[_].is_alive():
        print(f'Sleep {10-_}')
        time.sleep(10-_)
    else:
        break


# [ga() for x in range(10)]