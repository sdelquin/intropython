my_netflix_favs = {}

path = '../../resources/my-netflix-favs.csv'
with open(path) as f:
    for line in f:
        serie, premiere_year = line.strip().split(',')
        my_netflix_favs[serie] = int(premiere_year)

print(my_netflix_favs)
