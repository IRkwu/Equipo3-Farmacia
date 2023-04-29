import csv

class Medicamentos:
    def __init__(self,ID:str,Nombre_Medicamento:str, Descripcion:str, Precio:int, Stock:int):
        self.__ID = ID
        self.__Nombre_Medicamento=Nombre_Medicamento
        self.__Descripcion=Descripcion
        self.__Precio=Precio
        self.__Stock=Stock

    #GETTERS
    def get_id(self):
        return self.__ID
    
    def get_nombre(self): 
        return self.__Nombre_Medicamento
     
    def get_descripcion(self):
        return self.__Descripcion
    
    def get_precio(self):
        return self.__Precio
    
    def get_stock(self):
        return self.__Stock
    
    #SETTERS
    def set_id(self, ID):
        self.__ID = ID
    
    def set_nombre(self, Nombre_Medicamento):
        self.__Nombre_Medicamento = Nombre_Medicamento

    def set_descripcion(self, Descripcion):
        self.__Descripcion = Descripcion
    
    def set_precio(self, Precio):
        self.__Precio = Precio

    def set_stock(self, Stock):
        self.__Stock = Stock
        
    def agregar_stock(self, Cantidad):
        self.__Stock = self.__Stock + Cantidad
        
    def retirar_stock(self, Cantidad):
        self.__Stock = self.__Stock - Cantidad
             
    def guardar_medicamentos_CSV(self, lista_medicamentos):
        with open('ArchivosCSV/Medicamentos.csv', mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['ID', 'Nombre', 'Descripcion', 'Precio', 'Stock'])
            for medicamento in lista_medicamentos:
                writer.writerow([medicamento.get_id(), medicamento.get_nombre(), medicamento.get_descripcion(), medicamento.get_precio(), medicamento.get_stock()])
                
    def cargar_medicamentos_CSV(self):
        lista_medicamentos = []
        with open('ArchivosCSV/Medicamentos.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                ID, Nombre_Medicamento, Descripcion, Precio, Stock = row
                medicamento = Medicamentos(ID, Nombre_Medicamento, Descripcion, Precio, Stock)
                lista_medicamentos.append(medicamento)
        return lista_medicamentos

# Inicializar la lista de medicamentos
lista_medicamentos = Medicamentos.cargar_medicamentos_CSV(None)