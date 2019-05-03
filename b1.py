import math
import random


def dist(x, y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return math.sqrt(d_x ** 2 + d_y ** 2)


current = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]


sigma = 0.10
delta = 0.1
N = 10000

for steps in range(N):
    a = random.choice(current)
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
    min_dist = min(dist(b, c) for c in current if c != a)

    if min_dist / 2 < sigma:
        continue

    a[0] = b[0] % 1.0
    a[1] = b[1] % 1.0

print(current)
