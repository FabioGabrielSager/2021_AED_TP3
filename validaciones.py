import interfaz


# Valida que la opcion ingresada este comprendida entre los limetes de opciones disponibles
def validar_entre(lim_inferior, lim_superior, mensaje_ingreso='Ingrese un valor:',
                  mensaje_error='Valor inválido. Reintente'):
    opcion = int(input(mensaje_ingreso))
    while opcion < lim_inferior or opcion > lim_superior:
        print()
        print(interfaz.determinar_cant_simbolos(mensaje_error, '='))
        print(mensaje_error)
        print(interfaz.determinar_cant_simbolos(mensaje_error, '='))
        input('Presione enter para continuar')
        print()

        opcion = int(input(mensaje_ingreso))

    return opcion


# Valida segun el metodo modulo 11 si un isbn (en forma de cadena de caracteres)
def validar_modulo_11_isbn(isbn):
    cont_guiones = 0
    num = 0
    multiplo = 10
    for i in isbn:
        if i != '-':
            if i == 'x':
                num += 10
            else:
                num += int(i) * multiplo
            multiplo -= 1
        else:
            cont_guiones += 1

    return num % 11, cont_guiones


def validar_isbn(isbn):
    resto, cant_guiones = validar_modulo_11_isbn(isbn)
    longitud_isbn = len(isbn)

    while longitud_isbn != 13 or resto != 0 or cant_guiones != 3:
        print(longitud_isbn, resto, cant_guiones)
        print(interfaz.determinar_cant_simbolos('ERROR, ISBN INVALIDO', '='))
        print('ERROR, ISBN INVALIDO')
        print(interfaz.determinar_cant_simbolos('ERROR, ISBN INVALIDO', '='))
        input('Presione enter para continuar')

        isbn = input('Ingrese el ISBN-10 del libro: ')
        longitud_isbn = len(isbn)
        resto = validar_modulo_11_isbn(isbn)

    return isbn


if __name__ == '__main__':
    pass
