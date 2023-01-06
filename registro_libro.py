import random
import validaciones
import logica
import interfaz


# Creacion del registro libro
class Libro:
    def __init__(self, isbn, titulo, genero, idioma, precio):
        self.ISBN = isbn
        self.titulo = titulo
        self.genero = genero
        self.idioma = idioma
        self.precio = precio


# funciones para mostras los registros
def write(libro):

    print('\nISBN:', libro.ISBN, end=' ')
    print('- Titulo:', libro.titulo, end=' ')
    print('- Genero:', logica.generos()[libro.genero], end=' ')
    print('- Idioma:', logica.idiomas()[libro.idioma - 1], end=' ')
    print('- Precio:', libro.precio, end=' ')


def to_string(libro):
    r = ''
    r += ' ISBN: ' + str(libro.ISBN)
    r += ' - Titulo: ' + libro.titulo
    r += ' - Genero: ' + str(logica.generos()[libro.genero])
    r += ' - Idioma: ' + str(logica.idiomas()[libro.idioma - 1])
    r += ' - Precio: ' + str(libro.precio)

    return r


# Todo lo relativo a la generacion automatica y aleatoria del vector libros:
# Funcion destinada a la generacion de un vector que contiene 9 numeros aleatorios que posteriormente forman
# parte de un ISBN
def generar_9_numeros_isbn():
    vec_nums = []

    for i in range(9):
        vec_nums.append(random.randint(0, 9))

    return vec_nums


# Funcion que recibe por parametro un vector de nueve numeros y en base a este
# determina un digito de control que haga valido al vector segun el metodo modulo 11 y retorna el mismo
# en forma de cadena de caracteres
def determinar_digito_control_isbn(vec_isbn):
    suma = 0
    longitud = len(vec_isbn)

    for i in range(1, longitud + 1):
        suma += vec_isbn[i - 1] * i

    modulo = suma % 11

    if modulo < 10:
        return '-' + str(modulo)
    else:
        if modulo == 11:
            return '-' + '0'
        else:
            return '-x'


# Haciendo uso de las dos funciones anteriores a esta, genera y retorna
# un ISBN (valido segun el metodo modulo 11) en forma de cadena de caracteres
def generar_isbn_cadena_caracteres():
    vec_nums = generar_9_numeros_isbn()
    digito_control = determinar_digito_control_isbn(vec_nums)
    isbn_cadena = ''
    cont_guiones = 0

    while cont_guiones != 2:
        if cont_guiones != 2:
            isbn_cadena = ''
            cont_guiones = 0

        for i in vec_nums:
            isbn_cadena += str(i)

            if random.randint(0, 2) == 0:
                if cont_guiones != 2 and vec_nums[8] != i:
                    isbn_cadena += '-'
                    cont_guiones += 1

    return isbn_cadena + digito_control


# Funcion que elige de una tupla de manera random un titulo y retorna este
def generar_titulo():
    titulos = 'Los endemoniados', 'Los hermanos Karamazov', 'Middlemarch', 'El hombre invisible', 'Medea', \
              'Absalom, Absalom', 'El ruido y la furia', 'Madame Bovary', 'La educación sentimental', \
              'Romancero gitano', 'Cien años de soledad',  'El amor en los tiempos del cólera', 'Fausto', \
              'Almas muertas', 'El tambor de hojalata', 'Gran Sertón: Veredas', 'Hambre', 'El viejo y el mar',\
              'Míada', 'Odisea', 'Casa de muñecas', 'Ulises', 'Relatos cortos', 'Poema de Gilgamesh', \
              'Libro de Job (de la Biblia)', 'Las mil y una noches', 'Saga de NJál', 'Todo se desmorona', \
              'Cuentos infantiles', 'Divina comedia', 'Orgullo y prejuicio', 'Papá Goriot Molloy', 'Malone muere', \
              'El Innombrable', 'Decamerón', 'Ficciones', 'Cumbres Borrascosas', 'El extranjero', 'Poemas', \
              'Viaje al fin de la noche', 'Don Quijote de la Mancha', 'Los cuentos Canterbury', 'Relatos cortos', \
              'Nostromo', 'Grandes Esperanzas', 'Jacques el fatalista', 'Berlin Alexanderplatz', 'Crimen y castigo', \
              'El idiota', 'El proceso', 'El castillo, Shakuntala', 'El sonido de la montaña', 'Zorba, el griego', \
              'Hijos y amantes', 'Gente independiente', 'Poemas', 'El cuaderno dorado', 'Pippi Calzaslargas', \
              'Diario de un loco', 'Hijos de nuestro barrio', 'Los Buddenbrook', 'La montaña mágica', 'Moby-Dick', \
              'Ensayos', 'La historia', 'Beloved', 'Genji Monogatari', 'El hombre sin atributos', 'Lolita', \
              '1984', 'Las metamortosis', 'Libro del desasosiego', 'Cuentos', 'En busca del tiempo perdido'

    titulo = random.choice(titulos)

    return titulo


# funcion para determinar un id de idioma y genero random para cada libro
def generar_genero_e_idioma():
    idioma = random.randint(1, 5)
    genero = random.randint(0, 9)

    return genero, idioma


# Haciendo uso de todas la funciones de generacion aleatoria anteriores a esta genera libros (segun una canitdad
# determinada) y los carga en un vector, para finalmente retornar este
def generar_vec_libros(cantidad):
    vec_libros = []

    for i in range(cantidad):
        isbn = generar_isbn_cadena_caracteres()
        titulo = generar_titulo()
        genero, idioma = generar_genero_e_idioma()
        precio = random.randint(100, 1000)
        libro = Libro(isbn, titulo, genero, idioma, precio)

        vec_libros.append(libro)

    return vec_libros

# Todo lo relativo a la carga manual de un vector de libros:


def carga_isbn_manual():
    isbn = input('Ingrese el ISBN-10 del libro: ')
    # Se hace invocacion de funcion para validar el isbn cargado segun el metodo modulo 11
    isbn = validaciones.validar_isbn(isbn)

    return isbn


def cargar_genero():
    # Variable destinada a ser parametro actual de la funcion armar_menu_de_vec del modulo interfaz
    encabezado_menu = f'\n  {interfaz.determinar_cant_simbolos("generos")}\n' \
           f'  generos\n' \
           f'  {interfaz.determinar_cant_simbolos("generos")}\n' \
           f''
    vec_generos = logica.generos()

    # Apartir del vector generos se genera un menu de opciones
    menu = interfaz.armar_menu_de_vec(vec_generos, encabezado_menu,
                                      'Ingrese de la lista el numero que represente el genero del libro: ')

    numero_de_genero = validaciones.validar_entre(0, 9, menu, 'ERROR, ESA OPCION NO EXISTE')

    return numero_de_genero


def cargar_idioma():
    # Variable destinada a ser parametro actual de la funcion armar_menu_de_vec del modulo interfaz
    encabezado_menu = f'\n {interfaz.determinar_cant_simbolos("idiomas")}\n' \
               f' idiomas\n' \
               f' {interfaz.determinar_cant_simbolos("idiomas")}\n' \
               f''

    vec_idiomas = logica.idiomas()

    # Apartir del vector idiomas se genera un menu de opciones
    menu = interfaz.armar_menu_de_vec(vec_idiomas, encabezado_menu,
                                      'Ingrese de la lista el numero que represente el idioma del libro: ')

    numero_de_idioma = validaciones.validar_entre(1, 5, menu, 'ERROR, ESA OPCION NO EXISTE')

    return numero_de_idioma


# Funcion para la carga manual de n libro.
def cargar_vec_libros(cantidad, vec_libros):
    for i in range(cantidad):
        isbn = carga_isbn_manual()
        titulo = input('Ingrese el titulo del libro: ')
        genero = cargar_genero()
        idioma = cargar_idioma()
        precio = int(input('Ingrese el precio del libro: '))
        libro = Libro(isbn, titulo, genero, idioma, precio)

        vec_libros.append(libro)


if __name__ == '__main__':
    cargar_genero()
    cargar_idioma()
