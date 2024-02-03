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




def menu():   

    print('1 - Consultar un catalogo')
    print('2 - Agregar una película')
    print('3 - Eliminar una película')
    print('4 - Crear catálogo')
    print('5 - Eliminar catálogo')
    print('0 - Salir')
    option = input('Introduzca el número de la opción deseada: ')
    return option

def catalogo():  
   
    nombre_catalogo = ""
    ruta_archivo = ""
    c = None  # Initialize c outside the loop

    while True:
        option = menu()

        if option == '1':
            if c:
                print(c.listar_peliculas())
            else:
                print("No se ha creado ningún catálogo. Por favor, cree uno primero.")
        elif option == '2':
            if not c:
                print("No se ha creado ningún catálogo. Por favor, cree uno primero.")
            else:
                titulo = input('Introduce el título de la película: ')
                anio = input('Introduce el año del estreno: ')
                director = input('Ingrese el nombre de su director: ')
                peli1 = Pelicula(titulo, anio, director)
                print(c.agregar_película(peli1))
        elif option == '3':
            if not c:
                print("No se ha creado ningún catálogo. Por favor, cree uno primero.")
            else:
                titulo = input('Introduce el título de la película que quiere eliminar: ')
                print(c.eliminar_pelicula(titulo))
        elif option == '4':
            nombre_catalogo = input('Ingrese un género de películas para crear el catálogo: ')
            ruta_archivo = f'C:\\Lore\\python\\{nombre_catalogo}.txt'
            c = CatalogoPelicula(nombre_catalogo, ruta_archivo)
            print(c.crear_catalogo())
        elif option == '5':
            if c:
                print(c.eliminar_catalogo())
                c = None  # Set c to None after deleting the catalog
            else:
                print("No se ha creado ningún catálogo. Por favor, cree uno primero.")
        elif option == '0':
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida.')
            break
    return


catalogo()


    
 

           





