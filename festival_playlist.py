nombres = []
artistas = []
duraciones = []
popularidades = []


def agregar_canciones():
    cantidad = int(input("¿Cuántas canciones quieres agregar? "))

    for _ in range(cantidad):
        print("\nNueva Canción")
        nombre = input("Nombre de la canción: ")
        artista = input("Artista: ")
        duracion = float(input("Duración en minutos: "))
        popularidad = int(input("Popularidad (1-100): "))

        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)

    print("Canciones agregadas.\n")


def ver_reportes():
    if not nombres:
        print("No hay canciones registradas.")
        return

    total = len(nombres)
    duracion_total = sum(duraciones)

    max_pop = max(popularidades)
    min_pop = min(popularidades)
    promedio_pop = sum(popularidades) / total

    idx_max = popularidades.index(max_pop)
    idx_min = popularidades.index(min_pop)

    print("\nREPORTES DEL FESTIVAL")
    print(f"Total de canciones: {total}")
    print(f"Duración total: {duracion_total:.2f} minutos")
    print(f"Canción más popular: {nombres[idx_max]} ({max_pop})")
    print(f"Canción menos popular: {nombres[idx_min]} ({min_pop})")
    print(f"Promedio de popularidad: {promedio_pop:.2f}")
    print()


def buscar_canciones():
    if not nombres:
        print("No hay canciones registradas.")
        return

    print("\nBuscar por:")
    print("1. Artista")
    print("2. Rango de popularidad")
    opcion = input("Opción: ")

    if opcion == '1':
        artista_buscar = input("Nombre del artista: ")
        print("\nResultados")
        encontrado = False

        for i in range(len(nombres)):
            if artistas[i].lower() == artista_buscar.lower():
                print(f"{nombres[i]} - {artistas[i]} ({popularidades[i]})")
                encontrado = True

        if not encontrado:
            print("No se encontraron canciones de ese artista.")

    elif opcion == '2':
        minimo = int(input("Popularidad mínima: "))
        maximo = int(input("Popularidad máxima: "))

        print("\nResultados")
        encontrado = False

        for i in range(len(nombres)):
            if minimo <= popularidades[i] <= maximo:
                print(f"{nombres[i]} - {artistas[i]} ({popularidades[i]})")
                encontrado = True

        if not encontrado:
            print("No hay canciones dentro de ese rango.")
    else:
        print("Opción inválida.")



def playlist_recomendada():
    if not nombres:
        print("No hay canciones registradas.")
        return

    promedio = sum(popularidades) / len(popularidades)

    print("\nPLAYLIST RECOMENDADA")
    encontrado = False

    for i in range(len(nombres)):
        if popularidades[i] > promedio:
            print(f"{nombres[i]} - {artistas[i]} ({popularidades[i]})")
            encontrado = True

    if not encontrado:
        print("No hay canciones que superen el promedio.")



def main():
    while True:
        print("\nMENÚ DEL FESTIVAL")
        print("1. Agregar canciones")
        print("2. Ver reportes")
        print("3. Buscar canciones")
        print("4. Playlist recomendada")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_canciones()
        elif opcion == '2':
            ver_reportes()
        elif opcion == '3':
            buscar_canciones()
        elif opcion == '4':
            playlist_recomendada()
        elif opcion == '5':
            print("Hasta luego.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
