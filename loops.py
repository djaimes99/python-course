foods = ['apples', 'bread', 'cheese' , 'milk']
# print(foods[0])
# print(foods[1])
# print(foods[2])
# print(foods[3])

#con bucle y condicional if
for food in foods:
    if food == 'cheese':
        print('You have to buy this')    
    print(food)

# #con bucle y condicional break (rompe con la ejecución)
for food in foods:  ## con un bucle como este no importa si se le agrega mas datos
    if food == 'cheese':
        break
    print(food)

    # #con bucle y condicional continue, sigue ejecutando pero omite cheese
for food in foods:  ## con un bucle como este no importa si se le agrega mas datos
    if food == 'cheese':
        continue
    print(food)
#aca no ejecuta cheese,lo ignora y sigue ejecutando lo que viene después de cheese

#Atención con la tabulación!!, si no se coloca la debida identación entre linea y línea ..dará error!!

# mostrar rangos de números (range) y carácteres de palabras
for number in range(1, 8):
	print(number)
for letter  in "hello": #muestra cada caracter de la palabra
	print(letter)
     
#while
count = 4
while count <= 10:
	print(count)
	count = count + 1



