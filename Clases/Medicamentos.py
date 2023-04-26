#Clase Revisada

class Medicamentos:
    def __init__(self,Nombre_Medicamento:str, Descripcion:str, Precio:int, Stock:int):
        self.__Nombre_Medicamento=Nombre_Medicamento
        self.__Descripcion=Descripcion
        self.__Precio=Precio
        self.__Stock=Stock

#Atributos estan creados 
#Los getters Funciona (esta es la clase medic) y estan creados (lista)

    #GETTERS
    def get_nombre(self): 
        return self.__Nombre_Medicamento
     
    def get_descripcion(self):
        return self.__Descripcion
    
    def get_precio(self):
        return self.__Precio
    
    def get_stock(self):
        return self.__Stock


    
    #SETTERS

#set 1 funciona
    def set_nombre(self):
         
        self.__Nombre_Medicamento = str(input("Ingrese nuevo nombre: "))
  

#set 2 funciona
    def set_descripcion(self):
        self.__Descripcion = str(input("Ingrese nueva descripcion: "))
    
#pide edad al usuario en vez del precio

#set 3 funciona
    def set_precio(self):
        #try para que se ingrese un int
        try:
            new_price= int(input("Ingrese precio: "))
            #if para que el int sea mayor o igual a 0
            if new_price >= 0:
                self.__Precio=new_price
            else:
                print("El precio debe ser un número positivo.")
        except ValueError:
            print("El precio debe ser un número entero.")

#set 4 funciona
    def set_stock(self):
        try:
             new_stock = int(input("Introduce nuevo stock: "))
             if new_stock >= 0:
                  self.__Stock =new_stock
             else:
              print("El stock debe ser un número positivo.")
        except ValueError:
             print("El stock debe ser un número entero.")
             

medic1 = Medicamentos('paracetamol','sirve para todo', 200, 2)

print(medic1.get_nombre())
print(medic1.get_descripcion())
print(medic1.get_precio())
print(medic1.get_stock())


medic1.set_stock()
print(medic1.get_stock())


#No contiene Main formal (no estaba definido)