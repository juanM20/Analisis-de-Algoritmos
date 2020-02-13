
a = 34
b = 21
aux = 0

print("N hojas")
for i in range(10,101):
    print('{} {}'.format(i,a+b))
    aux = a+b
    b = a
    a = aux


