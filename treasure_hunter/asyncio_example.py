import logging
import asyncio
import time
import aiofiles

logging.getLogger().setLevel(logging.DEBUG)

N = 10000
num_of_process = 10
treasure_found = False
count = int(N/num_of_process)


async def read_file(i):
    global treasure_found
    async with aiofiles.open(f"treasure_data/file_{i}.txt", "r") as f:
        a = await f.readlines()
        if a[0] == "Treasure\n":
            treasure_found = i
            return


async def find_treasure(start, end):
    logging.debug(f"{start}, {end}")
    global treasure_found

    for i in range(start, end):
        logging.debug(i)
        if treasure_found:
            logging.info("Returning....")
            return
        await read_file(i)


async def main():
    tasks = [find_treasure(i, i+count)
            for i in range(0, N, count)]
    await asyncio.gather(
            *tasks
    )


start_time = time.time()
asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
print (f"Found treasure {treasure_found}")
