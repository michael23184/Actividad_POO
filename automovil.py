class Automovil:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo 
        self.color = color
    def mostrar_informacion(self):
            print("Marca:", self.marca)
            print("Modelo:", self.modelo)
            print("Color:", self.color)
    def encender(self):
            print("El automovil esta encendido")
# Creacion de objetos
auto1 = Automovil("Toyota", "Corolla", "Blanco")
auto2 = Automovil("Chevrolet", "Spark", "Rojo")
print("Automovil 1")
auto1.mostrar_informacion()
auto1.encender()
print()
print("Automovil 2")
auto2.mostrar_informacion()
auto2.encender()