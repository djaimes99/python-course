product = {
    "name":"book",
    "price":4.99,
    "quantity":3
}

# print(product)
# print(type(product))

person = {
    "first_name":"ryan",
    "last_name":"ray"
}
# print(person)
# print(type(person))

# #ver métodos disponibles para diccionarios
# print(dir(person))

# #obtener los keys de un diccionario
# print(person.keys())  # dict_keys(['first_name', 'last_name'])

#obtener los items de un diccionario
print(person.items())  

# #eliminar el diccionario
# del person
# print(person) # da error pues intentamos imprimir un diccionario que no existe (fué borrado)

#solo vacíar el diccionario
person.clear()
print(person)

#varios diccionarios pueden estar contenidos en una lista:
products = [
	{"name":"book","price":10.99},
      {"name":"laptop", "price": 1000}
]
print(products)


