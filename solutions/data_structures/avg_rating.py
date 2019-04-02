raw_ratings = '87;43;11;67;99;29;65;25;15'

ratings = raw_ratings.split(';')
total_ratings = 0
for rating in ratings:
    total_ratings += int(rating)

avg_rating = total_ratings / len(ratings)
print(avg_rating)
