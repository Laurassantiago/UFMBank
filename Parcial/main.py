class Transacciones:
    def __init__(self, monto, fecha, categoria, descripcion):
        self.monto = float(monto)
        self.fecha = int(fecha)
        self.categoria = categoria.capitalize()
        self.descripcion = descripcion.capitalize()
   
    def __str__(self):
        return f"Monto: {self.monto}, Fecha: {self.fecha}, Categoría: {self.categoria}, Descripción: {self.descripcion}"

class Categorias:
    def __init__(self, comida, servicios, salario):
        self.comida = comida.capitalize()
        self.servicios = servicios.capitalize()
        self.salario = float(salario)
    def __str__(self):
        return f"Comida: {self.comida}, Sevicios: {self.servicios}, Salarios: {self.salarios}"
