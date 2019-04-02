raw_ratings = '87;43;11;67;99;29;65;25;15'

ratings = [int(rating) for rating in raw_ratings.split(';')]
avg_rating = sum(ratings) / len(ratings)
print(avg_rating)
