import csv

movies = []

with open('movie_metadata.csv', encoding="utf8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        movies.append(row)
print(f'Imported {len(movies)} movies.')

# Question 1
print("\nHow many BW movies?")

bw_movies = [movie for movie in movies if movie["color"].strip() == "Black and White"]
color_movies = [movie for movie in movies if movie["color"] == "Color"]

print(f"There's {len(bw_movies)} black and white movies, and {len(color_movies)} color movies.")

# Question 2
print("\nHow many movies for each director?")

directors = {}

for movie in movies:
    director = movie["director_name"]
    if director in directors:
        directors[director] += 1
    else:
        directors[director] = 1

print(directors)

# Question 3
print("\nWhat are the 10 least criticised movies?")
movies_critics = [(movie["movie_title"].strip(), int(movie["num_critic_for_reviews"]) if len(movie["num_critic_for_reviews"]) > 0 else 0) for movie in movies]
movies_critics_sorted = sorted(movies_critics, key=lambda kv: kv[1])

print(movies_critics_sorted[:10])

# Question 4
print("\nWhat are 20 longest movies?")


def movies_sorted_by_property(_movies, property_name, order="asc"):
    if order != "asc" and order != "desc":
      raise Exception("Invalid order")

    movies_by_property = [(movie["movie_title"].strip(), int(movie[property_name]) if len(movie[property_name]) > 0 else 0) for movie in _movies]
    sorted_movies = sorted(movies_by_property, key=lambda kv: kv[1])

    if order == "desc":
        sorted_movies.reverse()

    return sorted_movies


longest_movies = movies_sorted_by_property(movies, property_name="duration", order="desc")

print(longest_movies[:20])

# Question 5
print("\nWhat are the 5 top grossing movies?")

top_grossing_movies = movies_sorted_by_property(movies, property_name="gross", order="desc")

print(top_grossing_movies[:5])

# Question 6
print("\nWhat are the 5 least grossing movies?")

least_grossing_movies = movies_sorted_by_property(movies, property_name="gross", order="asc")

print(least_grossing_movies[:5])

# Question 7
print("\nWhat are the 3 most expensive movies?")

most_expensive_movies = movies_sorted_by_property(movies, property_name="budget", order="desc")

print(most_expensive_movies[:3])

# Question 8
print("\nWhat are the 3 least expensive movies?")

least_expensive_movies = movies_sorted_by_property(movies, property_name="budget", order="asc")

print(least_expensive_movies[:3])

# Question 9
print("\nIn what year were the most movies premiered?")


def group_movies_by_property(_movies, property_name):

    grouped_movies = {}

    for movie in _movies:
        prop = movie[property_name]
        if prop in grouped_movies:
            grouped_movies[prop] += 1
        else:
            grouped_movies[prop] = 1

    return grouped_movies


movies_grouped_by_year = group_movies_by_property(movies, "title_year")
sorted_movies = sorted(movies_grouped_by_year.items(), key=lambda kv: kv[1])
sorted_movies.reverse()

print(sorted_movies[0])

# Question 10
print("\nIn what year were the least movies premiered?")

movies_grouped_by_year = group_movies_by_property(movies, "title_year")
sorted_movies = sorted(movies_grouped_by_year.items(), key=lambda kv: kv[1])

print(sorted_movies[0])

# Question 11
print("\nActor ranking")


def str_to_int(str):
    if len(str) > 0:
        return int(str)
    else:
        return 0


actor_data = {}

for movie in movies:
    actors = {"actor_1_name": movie["actor_1_name"], "actor_2_name": movie["actor_2_name"], "actor_3_name": movie["actor_3_name"]}

    for actor_key in actors:
        if actors[actor_key] in actor_data:
            actor_data[actors[actor_key]]["movies"] += 1
            actor_data[actors[actor_key]]["facebook_likes"] += str_to_int(movie[actor_key.replace("name","facebook_likes")])
        else:
            actor_data[actors[actor_key]] = {"movies": 1, "facebook_likes": str_to_int(movie[actor_key.replace("name","facebook_likes")])}

sorted_actor_data = sorted(actor_data.items(), key=lambda kv: kv[1]["movies"])
sorted_actor_data.reverse()

print(sorted_actor_data)

# Question 12
print("\nKeywords")

keywords = {}

for movie in movies:
    movie_keywords = movie["plot_keywords"].split("|")

    for keyword in movie_keywords:
        if keyword in keywords:
            keywords[keyword] += 1
        else:
            keywords[keyword] = 1

sorted_keywords = sorted(keywords.items(), key=lambda kv: kv[1])
sorted_keywords.reverse()

print(sorted_keywords)

# Question 13
print("\nWhat genre was the highest grossing for each year?")

years = {}

for movie in movies:
    year = movie["title_year"]
    genres = movie["genres"].split("|")
    if year in years:
        for genre in genres:
            if genre in years[year]:
                years[year][genre] += str_to_int(movie["gross"])
            else:
                years[year][genre] = str_to_int(movie["gross"])
    else:
        years[year] = {}
        for genre in genres:
            years[year][genre] = str_to_int(movie["gross"])

years_best_genre = {}

for year in years:
    sorted_genres = sorted(years[year].items(), key=lambda kv: kv[1])
    sorted_genres.reverse()
    years_best_genre[year] = sorted_genres[0]

print(years_best_genre)

# Question 14
print("\nWhat genre was the lowest grossing for each year?")

years = {}

for movie in movies:
    year = movie["title_year"]
    genres = movie["genres"].split("|")
    if year in years:
        for genre in genres:
            if genre in years[year]:
                years[year][genre] += str_to_int(movie["gross"])
            else:
                years[year][genre] = str_to_int(movie["gross"])
    else:
        years[year] = {}
        for genre in genres:
            years[year][genre] = str_to_int(movie["gross"])

years_worst_genre = {}

for year in years:
    sorted_genres = sorted(years[year].items(), key=lambda kv: kv[1])
    years_worst_genre[year] = sorted_genres[0]

print(years_worst_genre)

# Question 16
print("\nWhat is the most liked genre?")

genres_likes = {}

for movie in movies:
    genres = movie["genres"].split("|")
    for genre in genres:
        if genre in genres_likes:
            genres_likes[genre] += str_to_int(movie["movie_facebook_likes"])
        else:
            genres_likes[genre] = str_to_int(movie["movie_facebook_likes"])


sorted_genres_likes = sorted(genres_likes.items(), key=lambda kv: kv[1])
sorted_genres_likes.reverse()

print(sorted_genres_likes[0][0])

# Question 17
print("\nWhat are the 5 directors with the best reputation?")

directors_likes = {}

for movie in movies:
    director = movie["director_name"]
    if director in directors_likes:
        directors_likes[director] += str_to_int(movie["director_facebook_likes"])
    else:
        directors_likes[director] = str_to_int(movie["director_facebook_likes"])


sorted_directors_likes = sorted(directors_likes.items(), key=lambda kv: kv[1])
sorted_directors_likes.reverse()

print(sorted_directors_likes[:5])