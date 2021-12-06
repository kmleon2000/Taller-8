#bucle for mediana
list = [20,13,14,15,10,8,7,4,2,21,11,12,30,16,18,9,1,3,5,31,35,25,22,23,28]
list.sort()

median = list[int((len(list)-1)/2)]

print("La mediana es: ",median)