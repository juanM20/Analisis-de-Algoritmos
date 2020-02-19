from matplotlib import pyplot
import random


a = 0
b = 1
n = 1000000

def f1(x):
    return x**2


def aprox_integral(n, b, a):
    sum  = 0
    for i in range(0, n):
        i=i
        ui = random.uniform(a, b)
        sum  = sum + f1(ui*(b-a) + a)
    return (b-a)/n * sum



x = range(-100,100)
pyplot.plot(x, [f1(i) for i in x])

pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")
pyplot.xlim(-100, 100)


pyplot.show()

print('aproximacion f1:', aprox_integral(n, b, a))