my_netflix_favs = [
    'Stranger Things', 'House of Cards', 'Orange is the new black',
    'Jessica Jones', 'Narcos', 'Por trece razones'
]

friend_netflix_favs = [
    'Alexa & Katie', 'El imperio romano', 'En pocas palabras', 'Dinastía'
]
friend_netflix_favs_pos = [2, 4, 5, 7]

for i, friend_serie in enumerate(friend_netflix_favs):
    pos = friend_netflix_favs_pos[i]
    my_netflix_favs.insert(pos, friend_serie)

print(my_netflix_favs)
