from clases.avanzadas import Operaciones, Avanzadas

def main():
    calculadora = Operaciones()

    while True:
        print("\n=== CALCULADORA ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Módulo")
        print("6. Salir")
        print("7. Raíz cuadrada (opción avanzada)")

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == "6":
            print("¡Hasta luego!")
            break

        if opcion in ["1", "2", "3", "4", "5"]:
            calculadora.leerNumeros()
            if opcion == "1":
                calculadora.sumar()
            elif opcion == "2":
                calculadora.restar()
            elif opcion == "3":
                calculadora.multiplicar()
            elif opcion == "4":
                calculadora.dividir()
            elif opcion == "5":
                calculadora.modulo()

            calculadora.mostrarResultado()

        elif opcion == "7":
            avanzada = Avanzadas()
            avanzada.leerNumero()
            avanzada.raizCuadrada()
            avanzada.mostrarResultado()

        else:
            print("Opción inválida. Por favor, seleccione 1-7.")

if __name__ == "__main__":
    main()
