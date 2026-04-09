# Materia: Algoritmos y Estructuras de Datos II
# Alumno/a: Pablo Aguirre
# TP N°: 1 | Ejercicio N°: 1
# Fecha de entrega: 09/04/2026

class Vehiculo():
    def __init__(self, marca, velocidad_max,):
        self.marca = marca
        self.velocidad_max = velocidad_max

    def describir(self):
       pass
    
class Auto(Vehiculo):
    
    def describir(self):
        print(f"Soy un Auto de marca {self.marca} y mi velocidad máxima es {self.velocidad_max}")

class Moto(Vehiculo):

   def describir(self):
        print(f"Soy una Moto de marca {self.marca} y mi velocidad máxima es {self.velocidad_max}")
    

listaVehiculos = [Auto("Toyota", 120), Moto("Yamaha", 150), Auto("Ford", 140), Moto("Honda", 160)]

for vehiculo in listaVehiculos:
    vehiculo  .describir()
