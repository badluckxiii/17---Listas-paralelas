# Realizar un programa que pida la carga de dos listas numéricas enteras de
# 4 elementos cada una. Generar una tercer lista que surja de la suma de los
# elementos de la misma posición de cada lista. Mostrar esta tercer lista.
lista1=[]
lista2=[]
lista3=[]
for x in range(4):
    lista1.append(int(input('Valor lista 1: ')))
    lista2.append(int(input('Valor lista 2: ')))
for y in range(len(lista1)):
    lista3.append(lista1[y]+lista2[y])
for l in range(len(lista1)):
    print(lista1[l],'+', lista2[l],'=',lista3[l])