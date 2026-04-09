# Materia: Algoritmos y Estructuras de Datos II
# Alumno/a: Pablo Aguirre
# TP N°: 1 | Ejercicio N°: 2
# Fecha de entrega: 09/04/2026

class Figura():
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

    def describir(self):
        print(f"Soy una figura de color {self.color} y mi área es {self.area()}")

class Rectangulo(Figura):
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return 3.14 * self.radio ** 2
    

listaFiguras = [Rectangulo("rojo", 5, 3), Circulo("azul", 4), Rectangulo("rojo", 5, 3), Circulo("azul", 4)]

for figura in listaFiguras:
    figura.describir()
