import math
import random
import pylab
import os
import random

def dist(x, y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return math.sqrt(d_x ** 2 + d_y ** 2)


N_sqrt = 8
N = N_sqrt * N_sqrt
delxy = 0.5 / (N_sqrt)

# n_steps = 0
n_steps = 10000
eta = 0.42
sigma = math.sqrt(eta / (N * math.pi))
delta = sigma * 0.2

filename = 'disk_configuration_N%i_eta%.2f.txt' % (N, eta)

if os.path.isfile(filename):
    f = open(filename, 'r')
    current = []
    for line in f:
        a, b = line.split()
        current.append([float(a), float(b)])
    f.close()
    print('starting from file', filename)
else:
    current = []
    for k in range(N):
        current = [[delxy + i * 2 * delxy, delxy + j * 2 * delxy] for i in range(N_sqrt) for j in range(N_sqrt)]
    print('starting from a new random configuration')

f = open(filename, 'w')
for a in current:
   f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
f.close()

for steps in range(n_steps):
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


# show_conf(current, sigma, "Disks", "b4-1.png")
show_conf(current, sigma, "Disks", "b4-2.png")
