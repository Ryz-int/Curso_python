#Las listas se pueden modificar 
lista = ["Nombre", "Maquina", 1.883, False]

    
#Las tuplas no se pueden modificar
tupla = ("Nombre", "Maquina", 1.883, False)

#Esto es valido
lista[2] = "Maquinola"

#Esto no
#tupla[2] = "Maquinola"

#-------------------------------------------------------------
#Conjuntos (set)
#En los coonjuntos no se pueden repetir valores, tampoco puedes acceder a ellos por el indice ya que no tienen un orden especifico
conjunto = {"Tomas", "Apellido", 1212.22, True}


#Pero se pueden acceder a ellos mediante un bucle, aunque los datos seran aleatorios ya que no tienen un orden especifico
for elemento in conjunto:
    print(elemento)


#-------------------------------------------------------------
#Creando un diccionario (dict)
diccionario = {
    "nombre" : "Tomas",
    "esta_feliz_de_aprendere" : True,
    "Altura" : 1.69,
    "sera_ingeniero_en_5_anios" : True,
    "dato_duplciado" : "Tomas",
    }
#A diferencia de las listas y tuplas, para poder llamar a un elemento de un diccionario, se debe llamar al nombre de la clave, no al indice 