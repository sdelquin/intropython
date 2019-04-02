my_netflix_favs = [
    'Stranger Things', 'House of Cards', 'Orange is the new black',
    'Jessica Jones', 'Narcos', 'Por trece razones'
]

while True:
    target_serie = input('Introduzca la serie que quiere buscar: ')
    if target_serie == ':wq':
        break
    if target_serie in my_netflix_favs:
        pos = my_netflix_favs.index(target_serie)
        print(f'La serie indicada ocupa la posición {pos}')
    else:
        my_netflix_favs.append(target_serie)
        print('Serie añadida a sus Netflix-favs')
