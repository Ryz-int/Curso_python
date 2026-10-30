import os
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Salir")


def sumar(valor1, valor2):
    resultado = valor1 + valor2
    total = (valor1, "+", valor1, "=", resultado)
    
    return total


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
    limpiar_pantalla()
    menu()
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 5:
        print("Gracias por usar mi programa")
        break
    elif opcion >= 1 and opcion <= 4:
        valor1 = float(input("Ingrese el primer valor: "))
        valor2 = float(input("Ingrese el segundo valor: "))
        if opcion == 1:
            limpiar_pantalla()
            print(sumar(valor1, valor2))
            input("Presione enter para continuar")

        elif opcion == 2:
            limpiar_pantalla()
            print(restar(valor1, valor2))
            input("Presione enter para continuar")

        elif opcion == 3:
            limpiar_pantalla()
            print(multiplicar(valor1, valor2))
            input("Presione enter para continuar")

        elif opcion == 4:
            limpiar_pantalla()
            print(dividir(valor1, valor2))
            input("Presione enter para continuar")
    else:
        limpiar_pantalla()
        print("Opcion invalida")
        input("Presione enter para continuar")
