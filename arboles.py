

class Arbol:
    def __init__(self, nombre, area, volumen, masa):
        self.nombre = nombre
        self.area = area
        self.volumen = volumen
        self.masa = masa

    def mostrarDatos(self):
        print("Nombre: ", self.nombre)
        print("Area: ", self.area, "m2")
        print("Volumen: ", self.volumen, "m3")
        print("Masa: ", self.masa, "Kg")
