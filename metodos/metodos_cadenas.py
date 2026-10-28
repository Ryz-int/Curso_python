cadena1 = (24234234123)
cadena2 = ("Soy un capo programando") 

#convierte a mayuscula
mayusucla = cadena1.upper()

#convierte a minsucula
minuscula = cadena1.lower()

#convierte la primera letra a mayuscua, pero transforma todo el texto a minuscula antes
primer_letra_mayuscula = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencia devuelve -1, si hay coincidencia devuelve la posicion de la primera letra de la cadena buscada
busqueda_find = cadena1.find("T")

#Buscamos una cadena en otra cadena, pero si no hay coincidencia devuelve un error, si hay coincidencia devuelve la posicion de la primera letra de la cadena buscada
#busqueda_index = cadena1.index("T")

#Si es numerico devuelve True, si no devuelve False
es_numerico = cadena1.isnumeric()


print(es_numerico)
