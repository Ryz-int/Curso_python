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


while True:
     print(menu())
     opcion = int(input("Ingrese una opcion: "))
     if opcion == 1:
          valor1 = float(input("Ingrese el primer valor: "))
          valor2 = float(input("Ingrese el segundo valor: "))
          print(sumar(valor1, valor2))
          input()

     elif opcion == 2:
            valor1 = float(input("Ingrese el primer valor: "))
            valor2 = float(input("Ingrese el segundo valor: "))
            print(restar(valor1, valor2))
            input()

     elif opcion == 3:
             valor1 = float(input("Ingrese el primer valor: "))
             valor2 = float(input("Ingrese el segundo valor: "))
             print(multiplicar(valor1, valor2))
             input()

     elif opcion == 4:
            valor1 = float(input("Ingrese el primer valor: "))
            valor2 = float(input("Ingrese el segundo valor: "))
            print(dividir(valor1, valor2))
            input(3)

     elif opcion == 5:
           print("Gracias por usar mi programa")
           break
     else:
           print("La opcion ingresada no es valida, por favor vuelve a intentarlo")