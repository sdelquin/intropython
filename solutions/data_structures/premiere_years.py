my_netflix_favs = {
    'Titanes': 2018,
    'Las muñecas de la Mafia': 2009,
    'Las chicas del cable': 2017,
    'El Imperio romano': 2016,
    'A ciegas': 2018
}

premiere_years = my_netflix_favs.values()
min_premiere_year = min(premiere_years)
max_premiere_year = max(premiere_years)

print(f'Menor año de lanzamiento: {min_premiere_year}')
print(f'Mayor año de lanzamiento: {max_premiere_year}')
