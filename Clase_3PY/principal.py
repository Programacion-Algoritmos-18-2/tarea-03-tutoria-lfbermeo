from paquete_1.modelo import *
d = Docente("BD", "Loja")
d2 = Docente("Programacion", "Quito")

listado = [d, d2]

e = Estudiante("Luis", listado)
print(e.presentar_datos())
