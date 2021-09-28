import random

print(round(random.uniform(1, 2), 3))

l = [5, 4, 3, 2, 1]
for i in l:
    if i - 3 == 0:
        break
    print(i)