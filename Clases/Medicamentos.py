import csv

class Medicamentos:
    def __init__(self, ID: str, Nombre_Medicamento: str, Precio: int, Stock: int, Descripcion: str, Lote1: int, caducidadLote1: str, Lote2: int, caducidadLote2: str):
        self.__ID = ID
        self.__Nombre_Medicamento = Nombre_Medicamento
        self.__Precio = Precio
        self.__Stock = Stock
        self.__Descripcion = Descripcion
        self.__Lote1 = Lote1
        self.__caducidadLote1 = caducidadLote1
        self.__Lote2 = Lote2
        self.__caducidadLote2 = caducidadLote2

    # Getters
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

    def get_lote1(self):
        return self.__Lote1

    def get_vencL1(self):
        return self.__caducidadLote1

    def get_lote2(self):
        return self.__Lote2

    def get_vencL2(self):
        return self.__caducidadLote2

    # Setters
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

    def set_lote1(self, Lote1):
        self.__Lote1 = Lote1

    def set_vencL1(self, caducidadLote1):
        self.__caducidadLote1 = caducidadLote1

    def set_lote2(self, Lote2):
        self.__Lote2 = Lote2

    def set_vencL2(self, caducidadLote2):
        self.__caducidadLote2 = caducidadLote2
             
    def guardar_medicamentos_CSV(self, lista_medicamentos):
        with open('ArchivosCSV/Medicamentos.csv', mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['ID', 'Nombre', 'Precio', 'Stock', 'Descripcion', 'Lote 1', 'Caducidad Lote 1', 'Lote 2', 'Caducidad Lote 2'])
            for medicamento in lista_medicamentos:
                writer.writerow([medicamento.get_id(), medicamento.get_nombre(), medicamento.get_precio(), medicamento.get_stock(), medicamento.get_descripcion(),
                                 medicamento.get_lote1(), medicamento.get_caducidadLote1(), medicamento.get_lote2(), medicamento.get_caducidadLote2()])
                
    def cargar_medicamentos_CSV(self):
        lista_medicamentos = []
        with open('ArchivosCSV/Medicamentos.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                ID, Nombre_Medicamento, Precio, Stock, Descripcion, Lote1, caducidadL1, Lote2, caducidadLote2 = row
                medicamento = Medicamentos(ID, Nombre_Medicamento, Precio, Stock, Descripcion, Lote1, caducidadL1, Lote2, caducidadLote2)
                lista_medicamentos.append(medicamento)
        return lista_medicamentos

# Inicializar la lista de medicamentos
lista_medicamentos = Medicamentos.cargar_medicamentos_CSV(None)