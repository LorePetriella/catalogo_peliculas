#Maneja interacción del usuario, llama a funciones desde otros archivos, muestra menú. Al ejecutar el programa se solicita ingresar el nombre del catálogo de películas:
# Si el catálogo de películas no existe se creará uno nuevo. Este catálogo se va a guardar en un archivo txt donde posteriormente se guardarán las películas. Si el catálogo existe se podrá seguir modificando el archivo.
# Se debe mostrar un menú de opciones, que permita realizar las siguientes operaciones:
#     	1. Agregar Película
#     	2. Listar Películas
#     	3. Eliminar catálogo películas
#     	4. Salir
# Funcionamiento de las opciones:
# Agregar Película: se va a solicitar el nombre de la película y esta película se va a guardar en el archivo txt.
# Listar Peliculas: va a mostrar todas las peliculas del catalogo y guardadas en el archivo txt.
# Eliminar catálogo: elimina el archivo txt que corresponde al catálogo de películas.
# Salir: debe finalizar el programa mostrando un mensaje al usuario.


from catalogo import CatalogoPelicula
from pelicula import Pelicula
import os



# ruta = os.path.join("carpeta", "subcarpeta", "archivo.txt")
# print(ruta)


        
# def agregar_pelicula(pelicula):
#         agregar_pelicula = input("Agregar película: ")
        
#         f = open("C:\\Ada\catalogo_peliculas.py-first_create.txt", mode = "x")
#         f.close()


def menu():   

    print('1 - Consultar un teléfono')
    print('2 - Agregar una película')
    print('3 - Eliminar un catálogo')
    print('4 - Crear catálogo')
    print('0 - Salir')
    option = input('Introduzca el número de la opción deseada: ')
    return option