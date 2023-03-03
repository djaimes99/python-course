#sets coleccion desordenada de datos sin indice..
colors = {'Red', 'Green', 'Blue'}
print(colors)
# print(type(colors))

# print('Red' in colors)

# #agregar elementos (como es una colección desordenada se agregan los elementos al inicio del mismo, no al final)
# colors.add('Violet')
# print(colors)
# #remover elementos
# colors.remove('Red')
# print(colors)

#vaciar el sets 
colors.clear()
print(colors)  #  set()

#eliminar el sets
del colors
print(colors)  # NameError: name 'colors' is not defined
