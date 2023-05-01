import csv

class Medicamentos:
    def __init__(self,ID:str,Nombre_Medicamento:str, Precio:int, Stock:int, Descripcion:str):
        self.__ID = ID
        self.__Nombre_Medicamento=Nombre_Medicamento
        self.__Precio=Precio
        self.__Stock=Stock
        self.__Descripcion=Descripcion

    #GETTERS
    def get_id(self):
        return self.__ID
    
    def get_nombre(self): 
        return self.__Nombre_Medicamento
    
    def get_precio(self):
        return self.__Precio
    
    def get_stock(self):
        return self.__Stock
     
    def get_descripcion(self):
        return self.__Descripcion
    
    #SETTERS
    def set_id(self, ID):
        self.__ID = ID
    
    def set_nombre(self, Nombre_Medicamento):
        self.__Nombre_Medicamento = Nombre_Medicamento
    
    def set_precio(self, Precio):
        self.__Precio = Precio

    def set_stock(self, Stock):
        self.__Stock = Stock

    def set_descripcion(self, Descripcion):
        self.__Descripcion = Descripcion
        
    def agregar_stock(self, Cantidad):
        self.__Stock = self.__Stock + Cantidad
        
    def retirar_stock(self, Cantidad):
        self.__Stock = self.__Stock - Cantidad
             
    def guardar_medicamentos_CSV(self, lista_medicamentos):
        with open('ArchivosCSV/Medicamentos.csv', mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['ID', 'Nombre', 'Precio', 'Stock', 'Descripcion'])
            for medicamento in lista_medicamentos:
                writer.writerow([medicamento.get_id(), medicamento.get_nombre(), medicamento.get_precio(), medicamento.get_stock(), medicamento.get_descripcion()])
                
    def cargar_medicamentos_CSV(self):
        lista_medicamentos = []
        with open('ArchivosCSV/Medicamentos.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                ID, Nombre_Medicamento, Precio, Stock, Descripcion = row
                medicamento = Medicamentos(ID, Nombre_Medicamento, Precio, Stock, Descripcion)
                lista_medicamentos.append(medicamento)
        return lista_medicamentos

# Inicializar la lista de medicamentos
lista_medicamentos = Medicamentos.cargar_medicamentos_CSV(None)