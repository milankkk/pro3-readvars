# /usr/bin python3
import random
import time

with open('out.txt','a') as f:
    f.truncate(0)
    f.seek(0)
for i in range(10):
    time.sleep(1)
    random.seed()
    n = random.random()
    with open('out.txt', 'a') as f:
        f.write("n = " + str(n) + '\n')
    print(n)
