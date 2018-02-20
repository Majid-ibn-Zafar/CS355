from random import random

for _ in range(10):
    heads = 0
    for _ in range(100):
        if random() >= 0.5:
            heads += 1
            pass
    print(heads)
    pass
pass