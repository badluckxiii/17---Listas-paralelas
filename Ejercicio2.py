#  En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben 
# procesar de acuerdo a lo siguiente:
# a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas
#  paralelas)
# b) Realizar un listado que muestre los nombres, notas y condición del alumno.
#  En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno"
#  si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
# c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”. 
nombre=[]
nota=[]
condicion=[]
for x in range(4):
    nombre.append(input('Introduce el nombre del alumno:'))
    nota.append(int(input('Introduce una nota del 0 al 100:')))
for y in range(len(nota)):
   
    if nota[y]>=80:
        condicion[y].append('Muy bueno')
    if y>=40 and y <80:
        condicion.append('Suficiente')
    elif y<40:
        condicion.append('Suspendido')
iterador=0
for l in range(len(condicion)):
    print('Nombre:',nombre[l],'\nNota:',nota[l],'\nCondicion:',condicion[l])
    if nota[l]>=80:
        iterador+=1
print('Se repite muy bueno ',iterador)