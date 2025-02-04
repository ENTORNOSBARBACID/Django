class Lenguaje():
    def __init__(self, nombre, año, descripcion):
        self.nombre=nombre
        self.año=año
        self.descripcion=descripcion
        
    def __str__(self):
        
        cadena=" Nombre: "+str(self.nombre)   
        cadena+=" año: "+str(self.año)
        cadena+=" tipo: "+str(self.descripcion)

        return cadena 