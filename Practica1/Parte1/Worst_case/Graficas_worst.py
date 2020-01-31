import matplotlib.pyplot as plt

archivos = ['datos1_worst_case.txt', 'datos2_worst_case.txt']
color = ['blue', 'red']


i = 0
for a in archivos:
    X, Y = [], []
    for line in open(a, 'r'):
        values = [float(s) for s in line.split()]
        X.append(values[0])
        Y.append(values[1])
        plt.plot(X, Y, color=color[i])
    i = i +1

plt.show()
