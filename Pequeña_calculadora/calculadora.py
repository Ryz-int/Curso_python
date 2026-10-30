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
      menu()
      opcion = int(input("Ingrese una opcion: "))
      if opcion == 5:
          print("Gracias por usar mi programa")
          break
      elif opcion >=1 and opcion <=4:
           