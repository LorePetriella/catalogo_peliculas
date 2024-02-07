
from catalogo import CatalogoPelicula
from pelicula import Pelicula
import os




def menu():   

    print('1 - Consultar un catalogo')
    print('2 - Agregar una película')
    print('3 - Eliminar una película')
    print('4 - Crear catálogo')
    print('5 - Eliminar catálogo')
    print('6 - Listar catálogos disponibles')
    print('0 - Salir')
    option = input('Introduzca el número de la opción deseada: ')
    return option

def input_lower(prompt):
    return input(prompt).lower()

def catalogo():  
   
    nombre_catalogo = ""
    ruta_archivo = ""
    c = CatalogoPelicula(nombre_catalogo, ruta_archivo)

    while True:
        option = menu()

        if option == '1':
            nombre_catalogo = input_lower('Por favor introduzca el nombre del catálogo que quiere consultar: ')
            ruta_archivo = f'C:\\Lore\\python\\{nombre_catalogo}.txt'
            c = CatalogoPelicula(nombre_catalogo, ruta_archivo)

            if os.path.isfile(c.ruta_archivo):
             print(c.listar_peliculas())
            
            else:

             print(f'No encontramos el catálogo "{nombre_catalogo}". Por favor, verifique el nombre y vuelva a intentarlo.')   
               

                
        elif option == '2':        

          nombre_catalogo = input_lower('Introduce el nombre del catálogo en el que deseas agregar la película: ')
          ruta_archivo = f'C:\\Lore\\python\\{nombre_catalogo}.txt'
    
          c = CatalogoPelicula(nombre_catalogo, ruta_archivo)

          if os.path.isfile(c.ruta_archivo):
            titulo = input_lower('Introduce el título de la película: ')
            anio = input('Introduce el año del estreno: ')
            director = input_lower('Ingrese el nombre de su director: ')
            peli1 = Pelicula(titulo, anio, director)
            print(c.agregar_película(peli1))
          else:
            print(f'No se ha encontrado el catálogo "{nombre_catalogo}". Por favor, verifique el nombre y cree el catálogo primero.')
        
        
        elif option == '3':
            nombre_catalogo_a_editar = input_lower('Por favor indique a qué catálogo pertenece la película que quiere eliminar: ')
            ruta_archivo = f'C:\\Lore\\python\\{nombre_catalogo_a_editar}.txt'
            c = CatalogoPelicula(nombre_catalogo_a_editar, ruta_archivo)

            if os.path.isfile(c.ruta_archivo):
               titulo = input_lower('Introduce el título de la película que quieres eliminar: ')
               print(c.eliminar_pelicula(titulo))
            else:
               print(f'No se ha encontrado el catálogo "{nombre_catalogo_a_editar}". Por favor, verifique el nombre y vuelva a intentarlo.')

        elif option == '4':
        
            nombre_catalogo = input_lower('Ingrese un género de películas para crear el catálogo: ')
            ruta_archivo = f'C:\\Lore\\python\\{nombre_catalogo}.txt'
            nuevo_catalogo = CatalogoPelicula(nombre_catalogo, ruta_archivo)  # Crear una nueva instancia para el nuevo catálogo
            print(nuevo_catalogo.crear_catalogo())
          

        elif option == '5':
           
            nombre_catalogo = input_lower('Ingrese el nombre del catálogo que quiere eliminar: ')
            ruta_archivo = f'C:\\Lore\\python\\{nombre_catalogo}.txt'
            
            c = CatalogoPelicula(nombre_catalogo, ruta_archivo)
            if os.path.isfile(c.ruta_archivo):
               print(c.eliminar_catalogo())
            else:
               print(f'El catálogo "{nombre_catalogo}" no existe. Por favor, verifique el nombre y vuelva a intentarlo.')

        elif option == '6':
            
            c.listar_catalogos()



        elif option == '0':
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida.')
            break
    return


catalogo()


    
 

           





