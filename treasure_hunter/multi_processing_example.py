import logging
from multiprocessing import Process
import time

N = 10000

treasure_found = False


def find_treasure(start, end):
    global treasure_found
    for i in range(start, end):
        if treasure_found:
            return
        with open(f"treasure_data/file_{i}.txt", "r") as f:
            logging.debug(i)
            if f.readlines()[0] == "Treasure\n":
                treasure_found = i
                return


num_of_process = 100

start_time = time.time()
processes = [Process(target=find_treasure, args=[i, int(i+N/num_of_process)])
             for i in range(0, N, int(N/num_of_process))]


[process.start() for process in processes]

[process.join() for process in processes]


print("--- %s seconds ---" % (time.time() - start_time))
print (f"Found treasure {treasure_found}")
