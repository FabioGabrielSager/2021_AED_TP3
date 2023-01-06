# funcion para la generacion y pasaje de manera comoda el vector idiomas
def idiomas():
    vec_idiomas = ['Español', 'Ingles', 'Frances', 'Italiano', 'otros']

    return vec_idiomas


# funcion para la generacion y pasaje de manera comoda el vector de generos
def generos():
    vec_generos = ['auto ayuda', 'arte', 'ficcion', 'computacion', 'economia', 'escolar', 'ficcion',
                   'gastronomia', 'infatil', 'otros']

    return vec_generos


# funcion para el ordenamiento de titulos de forma acendente
def shell_sort_for_titles(vec_libros):
    n = len(vec_libros)
    h = 1
    while h <= n // 9:
        h = 3*h + 1

    while h > 0:
        for j in range(h, n):
            y = vec_libros[j]  # registro
            k = j - h
            while k >= 0 and y.titulo < vec_libros[k].titulo:   # titulo(ordenar los titulos)
                vec_libros[k + h] = vec_libros[k]
                k -= h
            vec_libros[k + h] = y
        h //= 3


# funcion para sacar y sumar el diez porciento del precio con ISBN
def diez_porciento(precio):
    diez_porcentaje = (10 * precio) / 100 + precio

    return diez_porcentaje


# funcion para determinar el genero y contarlo
def contar_libros_por_genero(vector_registro):
    vec_conteo = [0] * len(generos())

    for i in range(len(vector_registro)):
        if vector_registro[i].genero == 0:
            vec_conteo[0] += 1

        elif vector_registro[i].genero == 1:
            vec_conteo[1] += 1

        elif vector_registro[i].genero == 2:
            vec_conteo[2] += 1

        elif vector_registro[i].genero == 3:
            vec_conteo[3] += 1

        elif vector_registro[i].genero == 4:
            vec_conteo[4] += 1

        elif vector_registro[i].genero == 5:
            vec_conteo[5] += 1

        elif vector_registro[i].genero == 6:
            vec_conteo[6] += 1

        elif vector_registro[i].genero == 7:
            vec_conteo[7] += 1

        elif vector_registro[i].genero == 8:
            vec_conteo[8] += 1

        elif vector_registro[i].genero == 9:
            vec_conteo[9] += 1

    return vec_conteo


# funcion que define el mayor genero ofrecido del total de libros
def buscar_genero_mas_ofrecido(vector_conteo):
    indice_de_may = 0

    for i in range(len(vector_conteo)):
        if vector_conteo[i] > vector_conteo[indice_de_may]:
            indice_de_may = i

    return indice_de_may


# funcion que busca el ISBN consultado
def linear_search_isbn(isbn_a_buscar, vec_libros):
    n = len(vec_libros)
    for i in range(n):
        if isbn_a_buscar == vec_libros[i].ISBN:
            return i
    return -1


# funcion para aumentar el diez porciento del precio total
def aumentar_precio_libro(vec_libros, indice_de_libro):
    precio = vec_libros[indice_de_libro].precio
    vec_libros[indice_de_libro].precio = round((precio * 0.1) + precio, 2)


# funcion que sirve para determinar el mayor precio para un idioma
def buscar_mayor_precio_de_libro_de_idioma(idioma, vec_libros):
    precio_may = 0
    indice_de_may = 0
    for i in range(len(vec_libros)):
        if vec_libros[i].idioma == idioma and vec_libros[i].precio > precio_may:
            precio_may = vec_libros[i].precio
            indice_de_may = i

    return indice_de_may


# funcion para el ordenamiento de precios de mayor a menor
def shell_sort_for_precios(vec_libros):
    n = len(vec_libros)
    h = 1
    while h <= n // 9:
        h = 3*h + 1

    while h > 0:
        for j in range(h, n):
            y = vec_libros[j]
            k = j - h
            while k >= 0 and y.precio > vec_libros[k].precio:
                vec_libros[k + h] = vec_libros[k]
                k -= h
            vec_libros[k + h] = y
        h //= 3


# funcion para buscar los ISBN cargados en el sistema
def linear_search_isbn_group(vec_libros, vec_isbn):
    n = len(vec_libros)
    indices_de_isbn_buscados = [-1] * len(vec_isbn)

    for i in range(n):
        for j in range(len(vec_isbn)):
            if vec_libros[i].ISBN == vec_isbn[j]:
                indices_de_isbn_buscados[j] = i

    return indices_de_isbn_buscados


if __name__ == '__main__':
    pass
