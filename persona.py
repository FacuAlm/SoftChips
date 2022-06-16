
from uuid import uuid4
from datetime import datetime
import time


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, idCli):

        super().__init__(nombre, apellido)
        self.idCli = idCli


class solicitudCliente(Cliente):
    def __init__(self, fecha, idCli, nombre, apellido, cantChips, tipoMadera):
        super().__init__(nombre, apellido, idCli)

        self.cantChips = cantChips
        self.tipoMadera = tipoMadera
        self.fecha = fecha

    def __str__(self):
        return "largo: " + str(self.fecha)+"m" + " diametro: " + str(self.idCli)+"m" + " densidad: " + str(self.nombre)+"Kg/m3" + " stock: " + str(self.apellido)+"unidades"

    @classmethod
    def cargarSolicitud(self):
        fecha = datetime.now().strftime('%d - %m - %Y')
        idCli = id(time.time())
        nombre = input("Nombre Cliente: ")
        apellido = input("Apellido Cliente: ")
        cantChips = float(input("Cantidad Chip en toneladas: "))
        tipoMadera = input("Madera: ")

        return self(fecha, idCli, nombre, apellido, cantChips, tipoMadera)

    def mostrarSolicitud(self):
        print("Fecha: ", self.fecha)
        print("ID Cliente: ", self.idCli)
        print("Nombre: ", self.nombre)
        print("Apellido: ", self.apellido)
        print("Cantidad Chips en Toneladas: ", self.cantChips)
        print("Tipo de Madera: ", self.tipoMadera)


class operario(Persona):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)

        self.nombre = nombre
        self.apellido = apellido

    @classmethod
    def ingresarDatos(self):
        nombre = input("Ingrese su Nombre: ")
        apellido = input("Ingrese apellido: ")

        return self(nombre, apellido)

    def mostrarDatos(self):
        print('\nBienvenido ', self.nombre, ' ', self.apellido, '\n')
