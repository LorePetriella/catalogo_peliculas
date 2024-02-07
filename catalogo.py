import os

class CatalogoPelicula  :   
   
   def __init__(self, nombre_catalogo, ruta_archivo):
    
     self.nombre_catalogo = nombre_catalogo  
     self.ruta_archivo = ruta_archivo  

   def hay_catalogo(ruta):
       return os.path.isfile(ruta) 
    

   def listar_peliculas(self):
    
    if os.path.isfile(self.ruta_archivo): 
        
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as f:
                pelis = f.readlines()

            if not pelis:
                return "No hay películas en el catálogo.\n"

            resultado = ''.join(pelis)
            return resultado
        except FileNotFoundError:
            return "Error: No existen películas para mostrar.\n"
        except Exception as e:
            return f'Error al intentar listar las películas: {e}\n' 
        

   def agregar_película(self, pelicula):
 
        
    try:
            with open(self.ruta_archivo, 'a', encoding='utf-8') as f:
                f.write(f'{pelicula.titulo}, {pelicula.anio}, {pelicula.director}\n')
            return 'La película se ha añadido.\n'
    except FileNotFoundError:
            return f'¡El catálogo {self.ruta_archivo} no existe!\n'
    except Exception as e:
            return f'Error al intentar agregar la película: {e}\n'

   def eliminar_pelicula(self, titulo):      
       
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as f:
                catalogo = f.readlines()

            with open(self.ruta_archivo, 'w', encoding='utf-8') as f:
                pelicula_encontrada = False
                for linea in catalogo:
                    pelicula_info = linea.strip().split(', ') 
                    if len(pelicula_info) == 3 and titulo.lower() in pelicula_info[0].lower():
                        pelicula_encontrada = True
                        continue
                    f.write(linea)

                if not pelicula_encontrada:
                    return '¡La película no existe en el catálogo!\n'

            return f'¡La película "{titulo}" se ha borrado!\n'
        except FileNotFoundError:
            return f'¡La película "{titulo}" no existe!\n'
        except Exception as e:
            return f'Error al intentar eliminar la película: {e}\n'
        

   def crear_catalogo(self):

    if os.path.isfile(self.ruta_archivo):
            
            return f'El catálogo ' + self.nombre_catalogo +  ' ya existe.'
    else:      
               
            f = open(self.ruta_archivo, 'w', encoding='utf-8')
            f.close()
            return f'Se ha creado el catálogo {self.nombre_catalogo},  en la ruta {self.ruta_archivo}.\n'



   def eliminar_catalogo(self):
       
    try:
        os.remove(self.ruta_archivo)
        return f'El catálogo "{self.nombre_catalogo}" se ha borrado.\n'
    except FileNotFoundError:
        return f'El catálogo "{self.nombre_catalogo}" no existe.\n'
    except Exception as e:
        return f'Error al intentar eliminar el catálogo: {e}\n'
    

   def listar_catalogos(self):
        ruta_directorio = "C:\\Lore\\python\\" 
        catalogos = [archivo.replace('.txt', '') for archivo in os.listdir(ruta_directorio) if archivo.endswith('.txt')]
        if catalogos:
            print("Catálogos disponibles:")
            for catalogo in catalogos:
                 print("- ", catalogo)
        else: print("No hay Catálogos disponibles. Por favor cree uno.")     