class CatalogoPelicula():
    def __init__(self, nombre, ruta_archivo):
     self.peliculas = [] 
     self.catalogos = []
     self.nombre = nombre  
     self.ruta_archivo = ruta_archivo  

    def agregar_película(self, pelicula):
       if pelicula not in self.peliculas:
        self.peliculas.append(pelicula)

# otra opción
   #       def __init__(self):
   #      self.peliculas = set()

   #  def agregar_pelicula(self, pelicula):
   #      self.peliculas.add(pelicula)
   #      print("Película agregada correctamente.")


    def listar_peliculas(self):
       return [pelicula.titulo for pelicula in self.peliculas]
   
    def eliminar_catalogo(self):
      nombre_catalogo_a_eliminar = input("Ingrese el nombre del catálogo a eliminar: ")
      catalogo_a_eliminar = next((c for c in self.catalogos if c.nombre == nombre_catalogo_a_eliminar), None)