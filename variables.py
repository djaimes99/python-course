# estudio de tipos de variables

name = "Todo dulces, tu dulcería tradicional venezolana..!!"
print(name)

x,book = 100, "I am Robot"
print(x, book)

#Constantes  (por lo general se escriben todo en mayúsculas)
PI = 3.14
MY_NAME= "Deivie Jaimes"
print(PI, MY_NAME)

#Es un Lenguaje Dinamico
variable_tipos= "hola soy String"
print(variable_tipos)
variable_tipos= 100    # ahora soy numero
#print("ahora soy numero: "+variable_tipos)TypeError: can only concatenate str (not "int") to str
print(variable_tipos) 
variable_tipos= 100.99    # ahora soy float
#print("ahora soy float: "+variable_tipos) TypeError: can only concatenate str (not "float") to str
print(variable_tipos) 
variable_tipos= {
	'name': 'Deivie',
	'lastname': 'Jaimes'
}# ahora soy dictionary

#print("ahora soy dictionary: "+ variable_tipos)TypeError: can #only concatenate str (not "dict") to str
print(variable_tipos)


