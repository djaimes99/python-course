# #listas tipicas
demo_list = [1, 'hello', 1.14, True,[1,2,3]]
# print(demo_list)
colors = ['red', 'green', 'blue','red']
# print(colors)

# #creadas con el constructor list()
# number_list = list((1, 2, 3, 4))
# print(number_list)

# #listas con rangos (range)
# r = list(range(1,11))
# r2 = list(range(1,21))
# print(r,r2) 

# #métodos que se pueden ejecutar a partir de una lista
# #print(dir(colors))

# #longitud de una lista
# print(len(colors))

# #obtener algun elemento de la lista
# print(demo_list [4])

# #comprobar si un elemento esta en la lista
# print('green' in colors)

#comprobar si un elemento esta en la lista
print('green' in colors)

#alterando los datos de una lista
print(colors)
colors[2] = 'yellow'
print(colors)

#agregar un elemento a la lista
colors.append('violet')
print(colors)

#agregar varios elemento a la lista Se debe usar extends
colors.extend(['orange', 'purple'])
print(colors)

#agregar elementos en una posición especifica Pos 1
colors.insert(1, 'pink')
print(colors)
  
#insertar elemento en la última posición
colors.insert(len(colors), 'black')
print(colors)

#eliminar elementos de final a principio
colors.pop() #quita 1 elemento
print(colors)
colors.pop()#quita 1 elemento
print(colors)

#quitar un elemento especifico nombrandolo
colors.remove('yellow') #quita 1 elemento
print(colors)

#quitar un elemento de una posición especifica
colors.pop(2) #quita elemento pos 2 (green)
print(colors)

# #limpiar completamente la lista
# colors.clear()
# print(colors)


#ordenar la lista alfabeticamente
colors.sort() 
print(colors)

#ordenar la lista inversa alfabeticamente
colors.sort(reverse = True) 
print(colors) 

#obtener el indice de un elemento de la lista
print(colors.index('red'))

#contar cuantas veces aparece un elemento en una lista
print(colors.count('red'))





