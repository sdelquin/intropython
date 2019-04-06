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

ratings = []

for features in netflix_favs.values():
    rating = features.get('rating', 0)
    ratings.append(rating)

avg_ratings = sum(ratings) / len(ratings)

print(avg_ratings)
