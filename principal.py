from registro_libro import *
from interfaz import *
import validaciones
from logica import generos
import logica


def principal():
    vec_libros = []

    # Variable para el control del conteo (bandera) de generos (punto 3 y 6)
    conteo_ok = False
    # Variable para el guardado del genero mas ofrecido y el id del genero mas ofrecido
    gen_mas_ofrecido = 0

    opcion = -1

    while opcion != 8:
        opcion = mostrar_menu()
        print()

        # Si no se realizo la carga de libros, no se puede ejecutar ningunaotra funcionalidad que dependa u
        # opere sobre esa carga
        if opcion != 1 and opcion != 8 and len(vec_libros) == 0:
            print(determinar_cant_simbolos('Debe haber cargado libros para poder hacer eso'))
            print('Debe haber cargado libros para poder hacer eso')
            print(determinar_cant_simbolos('Debe haber cargado libros para poder hacer eso'))

            input('Presione enter para continuar')
            print()

        # el usuario debe elegir entre cargar los libros manualmente o aleatoriamente
        elif opcion == 1:
            opcion_1 = validaciones.validar_entre(0, 2, 'Ingrese 1 para generar un vector de libros de manera '
                                                        'aleatoria, de lo contrario ingrese 2: ',
                                                  'ERROR, DEBE INGRESAR 0 o 2')

            cantidad_de_libros = int(input('Ingrese la cantidad de libros a cargar: '))

            # generacion de libros

            if opcion_1 == 1:
                vec_libros = generar_vec_libros(cantidad_de_libros)
                conteo_ok = False
            else:
                cargar_vec_libros(cantidad_de_libros, vec_libros)
                conteo_ok = False

        # invocacion de la funcion ordenamiento de titulos de forma ascendente
        elif opcion == 2:
            logica.shell_sort_for_titles(vec_libros)
            for libro in vec_libros:
                write(libro)
            print()
            print()
            input('Presione enter para continuar')

        # invocacion de la funcion  de conteo de generos, y la muestra del genero mas ofrecido
        elif opcion == 3:
            vec_cont_generos = logica.contar_libros_por_genero(vec_libros)
            mostrar_generos_ofrecidos(vec_cont_generos)

            conteo_ok = True

            gen_mas_ofrecido = logica.buscar_genero_mas_ofrecido(vec_cont_generos)
            # a_imprimir se utiliza para facilitar el uso y la comrension (durante la invocacion)
            # de la funcion determinar_cant_simbolos
            a_imprimir = f'El genero con mas libros ofrecidos es del de {generos()[gen_mas_ofrecido]} con ' \
                         f'{vec_cont_generos[gen_mas_ofrecido]}'

            print(determinar_cant_simbolos(a_imprimir))
            print(a_imprimir)
            print(determinar_cant_simbolos(a_imprimir))
            print()
            input('Presione enter para continuar')

        # invocacion de  la funcion de pedir el idioma a analizar y mostrar el libro mas caro de dicho idioma

        elif opcion == 4:
            idioma_a_buscar = cargar_idioma()
            ind_libro_con_may_precio = logica.buscar_mayor_precio_de_libro_de_idioma(idioma_a_buscar, vec_libros)

            a_imprimir = f'El libro con mayor precio del idioma {idioma_a_buscar} es: ' \
                         f'{to_string(vec_libros[ind_libro_con_may_precio])}'

            print()
            print(determinar_cant_simbolos(a_imprimir))
            print(a_imprimir)
            print(determinar_cant_simbolos(a_imprimir))
            print()
            input('Presione enter para continuar')

            # invocacion de la funcion para verificar si el ISBN contiene una x al final

        elif opcion == 5:
            isbn_a_buscar = input('Ingrese el ISBN a buscar: ')
            isbn_a_buscar = validaciones.validar_isbn(isbn_a_buscar)

            indice_de_isbn_buscado = logica.linear_search_isbn(isbn_a_buscar, vec_libros)

            if indice_de_isbn_buscado != -1:
                # El precio anterior solo se guarda a fines de la impresion en pantalla
                precio_anterior = vec_libros[indice_de_isbn_buscado].precio

                logica.aumentar_precio_libro(vec_libros, indice_de_isbn_buscado)

                a_imprimir = f'Se ha aumentado un 10% el precio del libro ' \
                             f'{isbn_a_buscar}-"{vec_libros[indice_de_isbn_buscado].titulo}". ' \
                             f'Su valor paso de {precio_anterior}$ a -->' \
                             f' {vec_libros[indice_de_isbn_buscado].precio}$'
                print()
                print(determinar_cant_simbolos(a_imprimir))
                print(a_imprimir)
                print(determinar_cant_simbolos(a_imprimir))
                print()
                input('Presione enter para continuar')

            else:
                a_imprimir = f'ERROR, el libro indentificado con el ISBN, {isbn_a_buscar}, ' \
                             f'no se encuentra dentro del stock'
                print()
                print(determinar_cant_simbolos(a_imprimir, '='))
                print(a_imprimir)
                print(determinar_cant_simbolos(a_imprimir, '='))
                print()
                input('Presione enter para continuar')

        # invocacion del listado del genero del mayor, ordenados de mayor a menor por su precio
        elif opcion == 6:
            if not conteo_ok:
                vec_cont_generos = logica.contar_libros_por_genero(vec_libros)
                gen_mas_ofrecido = logica.buscar_genero_mas_ofrecido(vec_cont_generos)

            logica.shell_sort_for_precios(vec_libros)

            print(determinar_cant_simbolos('Los datos de los libros pertenecientes al genero '
                                           'con mayor cantidad de libro es:'))
            print('Los datos de los libros pertenecientes al genero con mayor cantidad de libro es:')
            print(determinar_cant_simbolos('Los datos de los libros pertenecientes al genero '
                                           'con mayor cantidad de libro es:'))

            for libro in vec_libros:
                if libro.genero == gen_mas_ofrecido:
                    write(libro)

            print()
            input('Presione enter para continuar')

        # invocacion de la funcion de pedido de isbn y validacion del mismo
        # muestra del los libros pedidos, con el total a pagar

        elif opcion == 7:
            cant_isbn_a_buscar = int(input('Ingrese la cantidad de libros a buscar: '))
            vec_isbn_a_buscar = []
            total_a_pagar = 0

            for i in range(cant_isbn_a_buscar):
                isbn = input(f'Ingrese el ISBN {i}: ')
                isbn = validaciones.validar_isbn(isbn)

                vec_isbn_a_buscar.append(isbn)

            indices_de_isbn_buscados = logica.linear_search_isbn_group(vec_libros, vec_isbn_a_buscar)

            print(indices_de_isbn_buscados)

            for j in range(len(indices_de_isbn_buscados)):
                if indices_de_isbn_buscados[j] == -1:
                    print(f'El libro con el ISBN {vec_isbn_a_buscar[j]} no se encuentra en el catalogo')
                    print()

                else:
                    write(vec_libros[indices_de_isbn_buscados[j]])
                    total_a_pagar += vec_libros[indices_de_isbn_buscados[j]].precio

            print()
            print(determinar_cant_simbolos(f'El total a pagar es:{total_a_pagar}'))
            print(f'El total a pagar es:{total_a_pagar}')
            print(determinar_cant_simbolos(f'El total a pagar es:{total_a_pagar}'))

            print()
            input('Presione enter para continuar')

        elif opcion == 8:
            print(determinar_cant_simbolos('Gracias por usar este programa, adios'))
            print('Gracias por usar este programa, adios')
            print(determinar_cant_simbolos('Gracias por usar este programa, adios'))

            print()
            input('Presione enter para Finalizar')


if __name__ == '__main__':
    principal()
