#  Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos 
# precios en otra. Definir dos listas paralelas. Mostrar cuantos productos tienen 
# un precio mayor al primer producto ingresado. 
precio=[]
nombre=[]
for x in range(5):
    nombre.append(input('Nombre del producto:'))
    precio.append(float(input('Introduce el precio:')))
suma=0
for y in range(len(nombre)):
    print('Nombre del producto:',nombre[y],
    '\nPrecio del producto: ',precio[y],
    )
    if(precio[0]<precio[y]):
        suma+=1

print('Productos con un valor elevado respecto al primero ',suma)