from random import randint
import time
import logging
N = 10000

logging.getLogger().setLevel(logging.DEBUG)


def creating_treasure():
    """
    Creates N files with treasure randomly set in one of the files
    :return:
    """
    treasure_in = randint(1, N)
    for i in range(0, N):
        logging.debug(i)
        with open(f"treasure_data/file_{i}.txt", "w") as f:
            if i != treasure_in:
                f.writelines(["Not a treasure\n"] * N)
            else:
                f.writelines(["Treasure\n"] * N)
    print (f"treasure is in {treasure_in}")


# creating_treasure()


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
