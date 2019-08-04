from redis import Redis
from rq import Queue
from find_treasure import find_treasure, treasure_found
import time


# run rq worker in rq_example dir
# More the worker less the time

N = 10000
num_of_process = 10
count = int(N/num_of_process)

start_time = time.time()
q = Queue(connection=Redis())
results = [q.enqueue(find_treasure, i, i+count)
           for i in range(0, N, count)]


res = False
while not res:
    for job in results:
        res = job.result
        status = job.get_status()
        if "finished" == status and res:
            print (res)
            break

        if "failed" == status:
            q.delete()
            break

print("--- %s seconds ---" % (time.time() - start_time))
