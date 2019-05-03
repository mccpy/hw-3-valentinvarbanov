import math
import random
import pylab

def dist(x, y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return math.sqrt(d_x ** 2 + d_y ** 2)


current = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]


eta = 0.4
sigma = math.sqrt(eta / (len(current) * math.pi))
delta = 0.1
n_tries = 10000

for steps in range(n_tries):
    a = random.choice(current)
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
    min_dist = min(dist(b, c) for c in current if c != a)

    if min_dist / 2 < sigma:
        continue

    a[0] = b[0] % 1.0
    a[1] = b[1] % 1.0

def show_conf(L, sigma, title, fname):
    pylab.axes()
    for [x, y] in L:
        for ix in range(-1, 2):
            for iy in range(-1, 2):
                cir = pylab.Circle((x + ix, y + iy), radius=sigma,  fc='r')
                pylab.gca().add_patch(cir)
    pylab.axis('scaled')
    pylab.title(title)
    pylab.axis([0.0, 1.0, 0.0, 1.0])
    pylab.savefig(fname)
    pylab.show()
    pylab.close()


show_conf(current, sigma, "Disks", "b2.png")
