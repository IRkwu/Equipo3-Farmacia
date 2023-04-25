
#Clase cliente revisada

import csv #Para poder GUARDAR los DATOS
import random #Para asiganar un ID al AZAR

class Cliente:
    def __init__(self,id:int,nombres:str,apellidos:str,genero:str,fecha_nacimiento:str,email:str,rut:str,telefono:str,domicilio:str):
        self.__id = id
        self.__nombre = nombres
        self.__apellidos = apellidos
        self.__genero = genero
        self.__fecha_nacimiento = fecha_nacimiento
        self.__email = email
        self.__rut = rut
        self.__telefono = telefono
        self.__domicilio = domicilio
        #Faltan los atributos PRIVADOS mascotas(arreglo) y Historial(arreglo) con sus respectivos get y set

    #Setters
    def set_id(self):
        self.__id = random.randint(1000, 9999)

    def set_nombre(self, nombres):
        self.__nombre = nombres

    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos

    def set_genero(self, genero):
        self.__genero = genero

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    def set_email(self, email):
        self.__email = email

    def set_rut(self, rut):
        self.__rut = rut

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_domicilio(self, domicilio):
        self.__domicilio = domicilio

    #Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_apellidos(self):
        return self.__apellidos

    def get_genero(self):
        return self.__genero

    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento

    def get_email(self):
        return self.__email

    def get_rut(self):
        return self.__rut

    def get_telefono(self):
        return self.__telefono

    def get_domicilio(self):
        return self.__domicilio


# Crea una lista para almacenar los objetos Cliente
clientes = []

# Pide al usuario que ingrese los datos de los clientes
for i in range(1):
    cliente = Cliente(id=int,nombres=str,apellidos=str,genero=str,fecha_nacimiento=str,email=str,rut=str,telefono=str,domicilio=str)
    cliente.set_id()    #se le setea un numero random, porque llamamos a la funcion set_id()
    nombre = input('Ingresa tu nombre: ')
    cliente.set_nombre(nombre)
    apellidos = input('Ingresa tu apellidos: ')
    cliente.set_apellidos(apellidos)
    genero = input('Ingresa tu género: ')
    cliente.set_genero(genero)
    fecha_nacimiento = input('Ingresa tu fecha de nacimiento (DD/MM/AAAA): ')
    cliente.set_fecha_nacimiento(fecha_nacimiento)
    email = input('Ingresa tu correo electrónico: ')
    cliente.set_email(email)
    rut = input('Ingresa tu RUT: ')
    cliente.set_rut(rut)
    telefono = input('Ingresa tu número de teléfono: ')
    cliente.set_telefono(telefono)
    domicilio = input('Ingresa tu domicilio: ')
    cliente.set_domicilio(domicilio)
    
    # Verifica que el ID no se repita
    while any(cliente.get_id() == c.get_id() for c in clientes): 
      cliente.set_id()  #Cada vez que un ID se repita a otro, entonces, entrara en este ciclo y no saldra hasta que el id setiado no se a = otro

    clientes.append(cliente)

#Sirve para crear los encabezados solo cuando se crea el archivo por primera vez
try:
    with open ('clientes.csv', mode ='x', newline='') as file:
        escritor_csv= csv.writer(file)
        escritor_csv.writerow(["ID , NOMBRE , apellidos , GENERO , FECHA NACIEMIENTO , EMAIL, RUT , TELEFONO , DOMICILIO "])
except FileExistsError:
        pass

# Abre el archivo CSV en modo de escritura
with open('clientes.csv', mode='a', newline='') as file:

  # Crea el objeto writer
  writer = csv.writer(file)
   
  # Escribe los encabezados 
  #writer.writerow(['ID', 'Nombre', 'apellidos', 'Genero', 'Fecha de Nacimiento', 'Correo Electrenico', 'RUT', 'Telefono', 'Domicilio'])
    
  # Escribe los datos de los clientes
  for cliente in clientes:
      writer.writerow([cliente.get_id(), cliente.get_nombre(), cliente.get_apellidos(), cliente.get_genero(), cliente.get_fecha_nacimiento(), cliente.get_email(), cliente.get_rut(), cliente.get_telefono(), cliente.get_domicilio()])



#falta que te pida cuantos usuarios hay que agregar
#funcionan los getters y setters 
#main no definido
