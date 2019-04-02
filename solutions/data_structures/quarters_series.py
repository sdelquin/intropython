my_netflix_favs = [
    'Stranger Things', 'House of Cards', 'Orange is the new black',
    'Jessica Jones', 'Narcos', 'Por trece razones', 'La ley secreta',
    'Altered Carbon'
]

i = 0
num_series = len(my_netflix_favs)
quarter_size = num_series // 4

while i < num_series:
    print(my_netflix_favs[i:i + quarter_size])
    i += quarter_size
