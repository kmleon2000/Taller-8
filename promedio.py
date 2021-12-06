#bucle for promedio
list = [20,13,14,15,10,8,7,4,2,21,11,12,30,16,18,9,1,3,5,31,35,25,22,23,28]
mean = 0

for n in list:
    mean += n

mean /= len(list)

print("el promedio es: ")
print(mean)

