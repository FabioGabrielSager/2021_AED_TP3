import validaciones
import logica


# muestra del menu de opciones principal del programa, y mediante la funcion validar_entre perteneciente al
# modulo validaciones, permite la carga por teclado de una opcion la cual es validada y retornada
def mostrar_menu():
    menu = '\n1) Generar o cargar libros' \
           '\n2) Mostrar libros ordenados ascendentemente por titulo' \
           '\n3) Determinar la cantidad de libros ofrecidos por género' \
           '\n4) Determinar y mostrar el libro de mayor precio para un idioma' \
           '\n5) Buscar libro por ISBN y aumentar su precio un 10%' \
           '\n6) Mostrar los datos de los libros del género con mayor cantidad de libros' \
           '\n7) Consultar precio por grupo de libros' \
           '\n8) Salir' \
           '\n' \
           '\nIngrese una opción: ' \

    op = validaciones.validar_entre(1, 8,  menu, 'ERROR, ESA OPCIÓN NO EXISTE')
    return op


# Funcion para la determinación de la cantidad de simbolos necesarios para la creacion "viñetas" a
# la hora de imprimir en pantalla
def determinar_cant_simbolos(cadena_caracteres='', simbolo='■'):
    n = len(cadena_caracteres)

    return simbolo * n


# Funcion para la determinacion de la cantidad de espacios de separacion requeridos. Se utiliza en casos
# en los que se requiera imprimir en pantalla resultados en forma similar a una tabla. Esta funcion se complementa
# con la funcion replace() y end='' de Python
def determinar_separacion(vector, indice_de_dato, tam_requerido):
    espacios = 0
    dato = str(vector[indice_de_dato])
    longitud = len(dato)

    if longitud < tam_requerido:
        resta = tam_requerido - longitud
        espacios = ' ' * resta

    return espacios


# Funcion destinada a la impresion en pantalla de los resultados obtenidos en la resolucion del punto 3
def mostrar_generos_ofrecidos(vec_conteo):
    print('GENEROS       OFRECIDOS')

    for i in range(len(vec_conteo)):
        print(logica.generos()[i], end=' '.replace(' ', determinar_separacion(logica.generos(), i, 18)))
        print(vec_conteo[i])


# funcion para la construccion de menus de opciones apartir de vectores.
def armar_menu_de_vec(vec, encabezado='OPCIONES', msj_ingreso='Ingrese una opcion: '):
    menu = encabezado
    for i in range(len(vec)):
        menu += f'{i}: {vec[i]}\n'

    menu += msj_ingreso

    return menu


if __name__ == '__main__':
    mostrar_menu()
