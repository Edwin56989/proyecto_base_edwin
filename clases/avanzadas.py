import math

class Operaciones:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resultado = 0

    def leerNumeros(self):
        while True:
            try:
                self.num1 = int(input("Número 1: "))
                break
            except Exception:
                print("Número inválido")
                continue
        while True:
            try:
                self.num2 = int(input("Número 2: "))
                break
            except Exception:
                print("Número inválido")
                continue    

    def sumar(self):
        self.resultado = f"La suma de {self.num1} + {self.num2} es igual a {self.num1 + self.num2}"
    
    def restar(self):
        self.resultado = f"La resta de {self.num1} - {self.num2} es igual a {self.num1 - self.num2}"
    
    def multiplicar(self):
        self.resultado = f"La multiplicación de {self.num1} * {self.num2} es igual a {self.num1 * self.num2}"
    
    def dividir(self):
        if self.num2 == 0:
            self.resultado = "Error: No se puede dividir entre cero"
        else:
            self.resultado = f"La división de {self.num1} / {self.num2} es igual a {self.num1 / self.num2}"
    
    def modulo(self):
        if self.num2 == 0:
            self.resultado = "Error: No se puede calcular el módulo con divisor cero"
        else:
            self.resultado = f"El módulo de {self.num1} % {self.num2} es igual a {self.num1 % self.num2}"
    
    def mostrarResultado(self):
        print(self.resultado)


# Clase avanzada añadida por Ari
class Avanzadas:
    def __init__(self):
        self.num = 0.0
        self.resultado = None

    def leerNumero(self):
        while True:
            try:
                self.num = float(input("Número: "))
                break
            except Exception:
                print("Número inválido, intenta de nuevo.")

    def raizCuadrada(self):
        if self.num < 0:
            self.resultado = "Error: no se puede calcular raíz de un número negativo."
        else:
            self.resultado = f"La raíz cuadrada de {self.num} es {math.sqrt(self.num)}"

    def mostrarResultado(self):
        print(self.resultado)
