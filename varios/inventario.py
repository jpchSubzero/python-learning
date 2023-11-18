# Librería para manejar fechas
import datetime

# Librería para funciones del sistema operativo
import os

class ProductoDeInventario:
    codigo = 0
    nombre = ''
    descripcion = ''
    stock_inicial = 0
    fecha_de_ingreso = datetime.datetime.now()
    fecha_de_salida = datetime.datetime.min
    total_stock = 0

    def __init__(self, codigo, nombre, descripcion, stock_inicial):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.stock_inicial = stock_inicial
        self.total_stock = stock_inicial

    def ingresar(self, valor):
        self.total_stock += valor

    def egresar(self, valor):
        self.total_stock -= valor
        self.fecha_de_salida = datetime.datetime.now()

    def presentar(self):
        print(f'\nCódigo: {self.codigo}\nNombre: {self.nombre}\nDescripción: {self.descripcion}\nStock Inicial: {self.stock_inicial}\nFecha de Ingreso: {self.fecha_de_ingreso}\nFecha de Egreso: {self.fecha_de_salida}\nTotal Stock: {self.total_stock}\n')

class Inventario:
    productos = []

    def buscar_producto(self, codigo):
        for producto in self.productos:
            if (producto.codigo == codigo):
                return producto
        return None

    def pausa(self):
        input('\nPresione una tecla para continuar...')

    def no_encontrado(self): 
        print('\nNo existe el producto')
        self.pausa()

    def agregar_item(self, item):
        self.productos.append(item)

    def ingresar_stock(self, codigo, cantidad):
        producto = self.buscar_producto(codigo)
        if producto == None:
            self.no_encontrado()
        else:
            producto.ingresar(cantidad)

    def egresar_stock(self, codigo, cantidad):
        producto = self.buscar_producto(codigo)
        if producto == None:
            self.no_encontrado()
        else:
            producto.egresar(cantidad)

    def presentar_por_codigo(self, codigo):
        producto = self.buscar_producto(codigo)
        if producto == None:
            self.no_encontrado()
        else:
            producto.presentar()
            self.pausa()

    def presentar_todos(self):
        if (self.productos.__len__() == 0):
            print('No hay productos')
        else:
            for producto in self.productos:
                producto.presentar()
        self.pausa()
       
class GestorInventario:
    activo = True
    opcion = 0
    inventario = Inventario()

    def limpiar_pantalla(self):
        clear = lambda: os.system('cls')
        clear()

    def salir(self):
        print('\n\n\n\nGracias...\n\n\n\n')
        self.activo = False

    def leer_codigo(self):
        codigo = (input('Código: '))
        return codigo

    def crear_producto(self):
        print('Ingrese las propiedades del producto')
        codigo = self.leer_codigo()
        nombre = (input('Nombre: '))
        descripcion = (input('Descripcion: '))
        stock_inicial = (input('Stock Inicial: '))
        self.inventario.agregar_item(ProductoDeInventario(codigo, nombre, descripcion, int(stock_inicial)))

    def presentar_producto(self):
        codigo = self.leer_codigo()
        self.inventario.presentar_por_codigo(codigo)

    def ingresar_stock(self):
        codigo = self.leer_codigo()
        cantidad = (input('Cantidad: '))
        self.inventario.ingresar_stock(codigo, int(cantidad))

    def egresar_stock(self):
        codigo = (input('Código: '))
        cantidad = (input('Cantidad: '))
        self.inventario.egresar_stock(codigo, int(cantidad))

    def iniciar(self):
        while self.activo:
            self.limpiar_pantalla()
            print('Menú de opciones')
            print('1. Crear producto')
            print('2. Ver producto')
            print('3. Ver todos los productos')
            print('4. Ingreso de stock de producto')
            print('5. Egreso de stock de producto')
            print('6. Salir')
            self.opcion = (input('Seleccione una opción: '))

            if (self.opcion == '1'):
                self.crear_producto()
            elif (self.opcion == '2'):
                self.presentar_producto()
            elif (self.opcion == '3'):
                self.inventario.presentar_todos()
            elif (self.opcion == '4'):
                self.ingresar_stock()
            elif (self.opcion == '5'):
                self.egresar_stock()
            elif (self.opcion == '6'):
                self.salir()

gestor_inventario = GestorInventario()

gestor_inventario.iniciar()