my_netflix_favs = []

while True:
    print('1. Mostrar mi Netflix-favs')
    print('2. Añadir una serie')
    print('3. Borrar una serie')
    option = input('Opción: ')
    if option == '1':
        print(my_netflix_favs)
    elif option == '2':
        serie = input('Introduzca la serie a añadir: ')
        if serie not in my_netflix_favs:
            my_netflix_favs.append(serie)
    elif option == '3':
        serie = input('Introduzca la serie a borrar: ')
        if serie in my_netflix_favs:
            my_netflix_favs.remove(serie)
    elif option == ':wq':
        break
