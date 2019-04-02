my_netflix_favs = [
    'Stranger Things', 'House of Cards', 'Orange is the new black',
    'Jessica Jones', 'Narcos', 'Por trece razones'
]

for i, serie in enumerate(my_netflix_favs):
    if serie[0].lower() in 'aeiou':
        my_netflix_favs[i] = my_netflix_favs[i].upper()
    else:
        my_netflix_favs[i] = my_netflix_favs[i].lower()

print(my_netflix_favs)
