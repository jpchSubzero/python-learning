class MyClass:

    i = 0
    name = ''
    age = 0

    def __init__(self, i, name, age):
        self.i = i
        self.name = name
        self.age = age

    def f(self):
        return 'hello world ' + self.name

    def show(self):
        print('prueba imprimir ' + str(self.age))

lista = []

x = MyClass(10, 'Juan Pablo', 45)
x1 = MyClass(20, 'Melania', 43)
x2 = MyClass(30, 'Aurora', 5)
x3 = MyClass(40, 'Juan Manuel', 15)
x4 = MyClass(50, 'Abigail', 18)

# print(x.i)
# print(x.f())
# x.show()

lista.append(x)
lista.append(x1)
lista.append(x2)
lista.append(x3)
lista.append(x4)

print(lista.__len__())

def show_list():
    for item in lista:
        print(f'Orden: {item.i}, Nombre: {item.name}, Edad: {item.age}')

show_list()