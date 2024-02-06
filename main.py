
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
    # c = None  # Initialize c outside the loop
    c = CatalogoPelicula(nombre_catalogo, ruta_archivo)
    while True:
        option = menu()

        if option == '1':
            nombre_catalogo = input('Por favor introduzca el nombre del catálogo que quiere consultar: ')
            ruta_archivo = f'C:\\Lore\\python\\{nombre_catalogo}.txt'
            c = CatalogoPelicula(nombre_catalogo, ruta_archivo)

            if os.path.isfile(c.ruta_archivo):
             print(c.listar_peliculas())
            
            else:

             print(f'No encontramos el catálogo "{nombre_catalogo}". Por favor, verifique el nombre y vuelva a intentarlo.')   
                # print("No se ha creado ningún catálogo. Por favor, cree uno primero.")

                
        elif option == '2':
            # if not c:
            #     print("No se ha creado ningún catálogo. Por favor, cree uno primero.")
            # else:
            #     titulo = input('Introduce el título de la película: ')
            #     anio = input('Introduce el año del estreno: ')
            #     director = input('Ingrese el nombre de su director: ')
            #     peli1 = Pelicula(titulo, anio, director)
            #     print(c.agregar_película(peli1))

          nombre_catalogo = input('Introduce el nombre del catálogo en el que deseas agregar la película: ')
          ruta_archivo = f'C:\\Lore\\python\\{nombre_catalogo}.txt'
    
          c = CatalogoPelicula(nombre_catalogo, ruta_archivo)

          if os.path.isfile(c.ruta_archivo):
            titulo = input('Introduce el título de la película: ')
            anio = input('Introduce el año del estreno: ')
            director = input('Ingrese el nombre de su director: ')
            peli1 = Pelicula(titulo, anio, director)
            print(c.agregar_película(peli1))
          else:
            print(f'No se ha encontrado el catálogo "{nombre_catalogo}". Por favor, verifique el nombre y cree el catálogo primero.')
        



        
        elif option == '3':
           if not c:
                print("No se ha creado ningún catálogo. Por favor, cree uno primero.")
           else:
                titulo = input('Introduce el título de la película que quiere eliminar: ')
                print(c.eliminar_pelicula(titulo))
        
        elif option == '4':
        
            nombre_catalogo = input('Ingrese un género de películas para crear el catálogo: ')
            ruta_archivo = f'C:\\Lore\\python\\{nombre_catalogo}.txt'
            
            print(c.crear_catalogo())

        elif option == '5':
            # nombre_catalogo = input('Ingrese el nombre del catálogo que quiere eliminar: ')
            # ruta_archivo = f'C:\\Lore\\python\\{nombre_catalogo}.txt'
            # if nombre_catalogo in c:
            #     print(c.eliminar_catalogo())
            #     # c = None  # Set c to None after deleting the catalog
            # else:
            #     print("No se ha creado ningún catálogo. Por favor, cree uno primero.")

            nombre_catalogo = input('Ingrese el nombre del catálogo que quiere eliminar: ')
            ruta_archivo = f'C:\\Lore\\python\\{nombre_catalogo}.txt'
            c = CatalogoPelicula(nombre_catalogo, ruta_archivo)
            if os.path.isfile(c.ruta_archivo):
               print(c.eliminar_catalogo())
            else:
               print(f'El catálogo "{nombre_catalogo}" no existe. Por favor, verifique el nombre y vuelva a intentarlo.')





        elif option == '0':
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida.')
            break
    return


catalogo()


    
 

           





