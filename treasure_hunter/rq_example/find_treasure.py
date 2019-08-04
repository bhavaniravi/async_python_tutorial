import logging

treasure_found = False


def find_treasure(start, end):
    logging.debug(f"{start}, {end}")
    global treasure_found
    for i in range(start, end):
        if treasure_found:
            return
        with open(f"../treasure_data/file_{i}.txt", "r") as f:
            if f.readlines()[0] == "Treasure\n":
                treasure_found = i
                return i