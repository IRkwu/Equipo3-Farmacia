
#Clase Carrito revisada

class Carrito:
    def __init__(self, Monto:int ,Ventas:int):
        self.__Monto=Monto
        self.__Ventas=Ventas
        self.__Productos=[]  
        pass


    #Getters
    def get_Monto(self):
        return self.__Monto 

    def get_Ventas(self):
        return self.__Ventas 

    def get_Productos(self):
         return self.__Productos
    
    def get_Producto(self,i):
         return self.__Productos[i]

#Clase incompleta
#Faltan setters (para poder agregar)
#funcion main no esta definida y no existe
#falta si un producto es de venta presencial o virtual para que se derive a envioen el caso de