import os

class CatalogoPelicula  :   
   
   def __init__(self, nombre_catalogo, ruta_archivo):
    
     self.nombre_catalogo = nombre_catalogo  
     self.ruta_archivo = ruta_archivo  

   def hay_catalogo(ruta):
    """Verifica si un archivo existe."""
    return os.path.isfile(ruta) 

   def agregar_película(self, pelicula):
 
        try: 
            f = open(self.ruta_archivo, 'a', encoding='utf-8')
        except FileNotFoundError:
            return('¡El catálogo ' + self.nombre + ' no existe!\n')
        else:
            f.write(pelicula.titulo + ', ' + pelicula.anio + ' de ' + pelicula.director + '\n')
            f.close()
            return('La pelicula se ha añadido.\n')




   
   def crear_catalogo(self):

    if os.path.isfile(self.ruta_archivo):
            print(f'El catálogo'  + self.nombre_catalogo +  'ya existe.')
    else:      
               
            f = open(self.ruta_archivo, 'w', encoding='utf-8')
            f.close()
            return f'Se ha creado el catálogo {self.nombre_catalogo} ,  en la ruta {self.ruta_archivo}.\n'
  
   

   def listar_peliculas(self):
    
    if os.path.isfile(self.ruta_archivo):
        f = open(self.ruta_archivo, 'r',  encoding='utf-8')
        pelis = f.readlines()
        resultado = ''.join(pelis)
        
        return resultado
   
        # return [pelicula.titulo for pelicula in self.peliculas]
    # def get_phone(file, client):
    # """Devuelve el teléfono de un cliente de un fichero dado."""
    # if file_exists(file):
    #     with open(file, 'r') as f:
    #         for line in f:
    #             name, phone = line.strip().split(',')
    #             if name == client:
    #                 return phone
    #     return f"No se encontró el teléfono para el cliente '{client}'."
    # else:
    #     return f"Error: El fichero '{file}' no existe."
   def eliminar_catalogo(self):
        os.remove(self.ruta_archivo)
        return 'Se ha borrado el catálogo'



   def eliminar_pelicula(self, titulo):
       

        try: 
            f = open(self.ruta_archivo, 'r')
        except FileNotFoundError:
            return('¡El catálogo ' + self.ruta_archivo + ' no existe!\n')
        else:
            catalogo = f.readlines()
            f.close()
            catalogo = dict([tuple(line.split(',')) for line in catalogo])
            if self.pelicula.titulo in self.catalogo:
                del self.catalogo[titulo]
                f = open(self.ruta_archivo, 'w')
                for titulo, anio, director in catalogo.items():
                    f.write(titulo + ',' + anio + 'de' + director)
                f.close()
                return ('¡La película se ha borrado!\n')
            else:
                return('¡La película ' + titulo + ' no existe!\n')
    