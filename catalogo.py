class Catalogo():
    def __init__(self, nombre, ruta_archivo):
     self.peliculas = [] 
     self.nombre = nombre
     self.ruta_archivo = ruta_archivo  

    def agregar_película(self, pelicula):
       self.peliculas.append(pelicula)

    # def listar_catalogo(self):
       
    # def eliminar_catalogo(self):