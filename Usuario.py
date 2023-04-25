
#clase usuario revisada

from datetime import date #esto es para la fecha
import random
import csv

#no definierion lo que era usuario
#verificar para que sirve el id

class Usuario:
    def __init__(self,id:int,nombres:str, apellidos:str,genero:str, fecha_nacimiento:date, rut:str):
        self.__Id=id
        self.__Nombre=nombres
        self.__Apellidos=apellidos
        self.__Genero=genero
        self.__Fecha_Nacimiento=fecha_nacimiento    #DateTime
        self.__Rut=rut
        self.__Cargo = []
        pass

    #GETTERS
    def get_id(self):
        print('esto es una prueba de que el get esta vacio')
        return self.__Id

    def get_nombre(self):
        return self.__Nombre

    def get_apellidos(self):
        return self.__Apellidos

    def get_genero(self):
        return self.__Genero

    def get_fecha_nacimiento(self):
        return self.__Fecha_Nacimiento

    def get_rut(self):
        return self.__Rut

    def get_cargo(self):
        return self.__Cargo #revisar luego

    #SETTERS
    # Nombre, apellido, genero fecha_nacimiento y rut inesesario ????????
    def set_id(self):
        self.__Id = random.randint(10000, 99999)

    def set_nombre(self,nombres):
        self.__Nombre=nombres
        

    def set_apellido(self,apellidos):
        self.__Apellidos=apellidos

    def set_genero(self,genero):
        self.__Genero=genero

    def set_fecha_nacimiento(self,fecha_nacimiento):
        self.__Fecha_Nacimiento=fecha_nacimiento

    def set_rut(self,rut):
        self.__Rut=rut
        
    def set_cargo(self):
        #Aca añadir, eliminar o modificar cargos
        pass



usuarios= []

# Pide al usuario que ingrese los datos de los clientes
for i in range(2):
    usuario = Usuario(id=int,nombres=str,apellidos=str,genero=str,fecha_nacimiento=str,rut=str,)
    usuario.set_id()
    nombre = input('Ingresa tu nombre: ')
    usuario.set_nombre(nombre)
    apellido = input('Ingresa tu apellido: ')
    usuario.set_apellido(apellido)
    genero = input('Ingresa tu género: ')
    usuario.set_genero(genero)
    fecha_nacimiento = input('Ingresa tu fecha de nacimiento (DD/MM/AAAA): ')
    usuario.set_fecha_nacimiento(fecha_nacimiento)
    rut = input('Ingresa tu RUT: ')
    usuario.set_rut(rut)

    # Verifica que el ID no se repita
    while any(usuario.get_id() == c.get_id() for c in usuarios): 
      usuario.set_id()
    
    usuarios.append(usuario)

#crea el archivo con un encabezado, la exepcion es para que tanto el archivo como el encabezado solo se cree una vez}
#mode x para crear y mode a es para append
try:
    with open('usuario.csv', mode='x', newline='') as file:
        escritor_csv = csv.writer(file)
        escritor_csv.writerow(['ID', 'Nombre', 'Apellido', 'Genero', 'Fecha de Nacimiento', 'RUT'])
except FileExistsError:
    pass

with open('usuario.csv', mode='a', newline='') as file:
  
  # Crea el objeto writer
  writer = csv.writer(file)
  # Escribe los datos de los clientes
  for usuario in usuarios:
      writer.writerow([usuario.get_id(), usuario.get_nombre(),usuario.get_apellidos(), usuario.get_genero(), usuario.get_fecha_nacimiento(),usuario.get_rut()])





test=Usuario(123,"juan","soto","hombre",date(1999,10,2),12345678)
# test.get_id()
# test.get_nombres()
# test.get_apellidos()
# test.get_genero()
# test.get_fecha_nacimiento()
# test.get_rut()



#falta que te pida cuantos usuarios hay que agregar
#funcionan los getters y setters 
#main no definido
#funcion set cargo: no hay para agregar cargo