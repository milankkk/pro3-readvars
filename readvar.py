#! /usr/bin python3
import random

with open('out.txt','a') as f:
    f.truncate(0)
    f.seek(0)
for i in range(10):
    random.seed()
    n = random.random()
    with open('out.txt', 'a') as f:
        f.write(str(n) + '\n')
