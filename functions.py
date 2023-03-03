def hello(nombre= "Por defecto"):
	print("Mi nombre es: " + nombre)

hello("deivie jaimes")
hello("Pedro perez")
hello("todo dulces!!")
hello()   #  Mi nombre es: Por defecto

#funcion lambda

add = lambda number_one ,number_two: number_one + number_two

print(add(10, 30)) #40