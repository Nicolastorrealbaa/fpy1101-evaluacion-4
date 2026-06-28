def validar_titulo(titulo):
    return titulo.strip() != ""
def validar_copias(copias):
    return copias >= 0
def validar_prestamo(prestamo):
    return prestamo > 0
def mostrar_menu():
    print("\n~~~~~~~ MENU PRINCIPAL ~~~~~~~ \n 1. Agregar libro \n 2. Buscar libro \n 3. Eliminar libro \n 4. Actualizar disponibilidad \n 5. Mostrar libros \n 6. Salir \n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
def leer_opcion():
    while True:
        entrada = input("Seleccione una opcion: ")
        try:
            opcion = int(entrada)
        except ValueError:
            print("ERROR. Debe ingresar un numero entero.")
            continue
        if 1 <= opcion <= 6:
            return opcion
        else:
            print("ERROR. Debe ingresar un numero entre 1 y 6.")
def agregar_libro(libros):
    titulo = input("Ingrese el titulo del libro: ")
    if not validar_titulo(titulo):
        print("ERROR. El titulo no puede estar vacio.")
        return
    copias_texto = input("Ingrese la cantidad de copias: ")
    try:
        copias = int(copias_texto)
    except ValueError:
        print("ERROR. Las copias deben ser un numero entero.")
        return
    if not validar_copias(copias):
        print("ERROR. Las copias deben ser mayor o igual a cero.")
        return
    prestamo_texto = input("Ingrese el periodo de prestamo en dias: ")
    try:
        prestamo = int(prestamo_texto)
    except ValueError:
        print("ERROR. El periodo de prestamo debe ser un numero entero.")
        return
    if not validar_prestamo(prestamo):
        print("ERROR. El periodo de prestamo debe ser mayor que cero.")
        return
    nuevo_libro = {
        "titulo": titulo.strip(),
        "copias": copias,
        "prestamo": prestamo,
        "disponible": False
    }
    libros.append(nuevo_libro)
    print(f'Libro "{nuevo_libro["titulo"]}" agregado correctamente.')
def buscar_libro(libros, titulo):
    for indice, libro in enumerate(libros):
        if libro["titulo"] == titulo:
            return indice
    return -1
def eliminar_libro(libros, titulo):
    indice = buscar_libro(libros, titulo)
    if indice != -1:
        libros.pop(indice)
        print(f'Libro "{titulo}" eliminado correctamente.')
    else:
        print(f'El libro "{titulo}" no se encuentra registrado.')
def actualizar_disponibilidad(libros):
    for libro in libros:
        if libro["copias"] >= 1:
            libro["disponible"] = True
        else:
            libro["disponible"] = False
def mostrar_libros(libros):
    actualizar_disponibilidad(libros)
    print("\n ~~~ LISTA DE LIBROS ~~~")
    for libro in libros:
        if libro["disponible"]:
            estado = "DISPONIBLE"
        else:
            estado = "SIN COPIAS"
        print(f'Titulo: {libro["titulo"]}')
        print(f'Copias: {libro["copias"]}')
        print(f'Prestamo: {libro["prestamo"]}')
        print(f'Estado: {estado}')
        print("*" * 45)
def main():
    libros = []
    opcion = 0
    while opcion != 6:
        mostrar_menu()
        opcion = leer_opcion()
        if opcion == 1:
            agregar_libro(libros)
        elif opcion == 2:
            titulo = input("Ingrese el titulo del libro: ")
            indice = buscar_libro(libros, titulo)
            if indice != -1:
                libro = libros[indice]
                print(f"Libro encontrado en la posicion {indice}")
                print(f'Titulo: {libro["titulo"]}')
                print(f'Copias: {libro["copias"]}')
                print(f'Prestamo: {libro["prestamo"]}')
                print(f'Disponible: {libro["disponible"]}')
            else:
                print(f'El libro "{titulo}" no esta registrado.')
        elif opcion == 3:
            titulo = input("Ingrese el titulo del libro a eliminar: ")
            eliminar_libro(libros, titulo)
        elif opcion == 4:
            actualizar_disponibilidad(libros)
            print("Disponibilidad actualizada correctamente.")
        elif opcion == 5:
            mostrar_libros(libros)
        elif opcion == 6:
            print("Gracias por usar el sistema. Vuelva pronto.")
main()    