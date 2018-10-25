class Docente:
    def __init__(self, n, a):
        self.nombre = n
        self.ciudad = a

    def presentar_datos(self):
        cadena = "\t- Docente %s\n\t\t%s\n" % (
            self.obtener_nombre(), self.obtener_ciudad())
        return cadena

    def agregar_nombre(self, n):
        self.nombre = n

    def obtener_nombre(self):
        return self.nombre

    def agregar_ciudad(self, c):
        self.ciudad = c

    def obtener_ciudad(self):
        return self.ciudad


class Estudiante:
    def __init__(self, n, lista_docentes):
        self.nombres = n
        self.docentes = lista_docentes

    def agregar_nombres(self, n):
        self.nombres = n

    def obtener_nombres(self):
        return self.nombres

    def agregar_lista_docentes(self, lista_docentes):
        self.docentes = lista_docentes

    def obtener_lista_docentes(self):
        return self.docentes

    def presentar_datos(self):
        cadena = "Estudiante: %s\n" % (self.obtener_nombres())
        cadena = "%s%s\n" % (cadena, "Lista Docentes")

        for docente in self.obtener_lista_docentes():
            cadena = "%s%s" % (cadena, docente.presentar_datos())

        return cadena
