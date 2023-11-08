from recommenders import data_movies, data_ratings
import pandas as pd


def recommend_popular_movies():

    ######################################################################################################
# merge-11
    movie_ratings = pd.merge(data_movies, data_ratings, on = 'movieId')
# calculate movie rating-2,3,4
    movie_ratings = movie_ratings.groupby('title')['rating'].mean().sort_values(ascending = False).head(20)
# 5
    movie_ratings = movie_ratings.to_dict()
    #######################################################################################################
    response = []

    for movie in movie_ratings:
        movie_record = data_movies[data_movies.title == movie].iloc[0]

        response.append({
            "movieId": int(movie_record.movieId),
            "title": str(movie),
            "genres": str(movie_record.genres).split("|"),
            "average_rating": movie_ratings[movie]
        })

# 6
    return {"status": True, "data": {"message": "Here are some of the popular recommendations.", "results" : response}}
