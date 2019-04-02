netflix_favs = {
    'Narcos': {
        'premiere_year': 2015,
        'total_seasons': 3,
        'rating': 5,
        'age_limit': '16+'
    },
    'The Good Place': {
        'premiere_year': 2016,
        'total_seasons': 3,
        'rating': 4,
        'age_limit': '13+'
    },
    'Sense8': {
        'premiere_year': 2015,
        'total_seasons': 2,
        'rating': 3,
        'age_limit': '16+'
    },
    'La niebla': {
        'premiere_year': 2017,
        'total_seasons': 1,
        'rating': 5,
        'age_limit': '16+'
    },
}

premiere_years = []

for features in netflix_favs.values():
    premiere_year = features['premiere_year']
    premiere_years.append(premiere_year)

avg_premiere_years = sum(premiere_years) // len(premiere_years)

print(avg_premiere_years)
