my_netflix_favs = [
    'Stranger Things', 'House of Cards', 'Orange is the new black',
    'Jessica Jones', 'Narcos', 'Por trece razones'
]

for serie in my_netflix_favs:
    if serie[0].lower() in 'aeiou':
        break
    print(serie)
