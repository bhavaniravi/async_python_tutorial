from random import randint
import time
import logging
N = 10000

logging.getLogger().setLevel(logging.DEBUG)


def find_treasure():
    for i in range(0, N):
        with open(f"treasure_data/file_{i}.txt", "r") as f:
            logging.debug(i)
            if f.readlines()[0] == "Treasure\n":
                print ("Found it....")
                return


start_time = time.time()
find_treasure()
print("--- %s seconds ---" % (time.time() - start_time))
