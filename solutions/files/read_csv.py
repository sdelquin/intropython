# cambie las rutas a los ficheros para que funcione correctamente la
# solución desde Jupyter Notebook
path = '../../resources/files/my-netflix-favs.csv'

my_netflix_favs = {}

with open(path) as f:
    for line in f:
        serie, premiere_year = line.strip().split(',')
        my_netflix_favs[serie] = int(premiere_year)

print(my_netflix_favs)
