def menu():
     print("1) Sumar")
     print("2) Restar")
     print("3) Multiplicar")
     print("4) Dividir")
     print("5) Salir")
def sumar(valor1, valor2):
     resultado = valor1 + valor2
     return resultado
def restar(valor1, valor2):
     resultado = valor1 - valor2
     return resultado
def multiplicar(valor1, valor2):
     resultado = valor1 * valor2
     return resultado
def dividir(valor1, valor2):
     resultado = valor1 / valor2
     return resultado

     valor1 = float(input("Ingrese el primer valor: "))
     valor2 = float(input("Ingrese el segundo valor: "))
     return valor1, valor2
print(menu())
opcion = float(input("Ingrese una opcion: "))
if opcion == 1:
     valor1 = float(input("Ingrese el primer valor: "))
     valor2 = float(input("Ingrese el segundo valor: "))
     print(sumar(valor1, valor2))

elif opcion == 2:
     valor1 = float(input("Ingrese el primer valor: "))
     valor2 = float(input("Ingrese el segundo valor: "))
     print(restar(valor1, valor2))

elif opcion == 3:
     valor1 = float(input("Ingrese el primer valor: "))
     valor2 = float(input("Ingrese el segundo valor: "))
     print(multiplicar(valor1, valor2))

elif opcion == 4:
     valor1 = float(input("Ingrese el primer valor: "))
     valor2 = float(input("Ingrese el segundo valor: "))
     print(dividir(valor1, valor2))