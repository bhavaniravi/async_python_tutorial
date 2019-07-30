import logging
import threading
import time

logging.getLogger().setLevel(logging.DEBUG)

N = 10000

treasure_found = False


def find_treasure(start, end):
    logging.debug(f"{start}, {end}")
    global treasure_found
    for i in range(start, end):
        if treasure_found:
            return
        with open(f"treasure_data/file_{i}.txt", "r") as f:
            if f.readlines()[0] == "Treasure\n":
                treasure_found = i
                return


num_of_process = 50
count = int(N/num_of_process)


start_time = time.time()
threads = [threading.Thread(target=find_treasure, args=[i, i+count])
           for i in range(0, N, count)]


[thread.start() for thread in threads]

[thread.join() for thread in threads]


print("--- %s seconds ---" % (time.time() - start_time))
print (f"Found treasure {treasure_found}")
