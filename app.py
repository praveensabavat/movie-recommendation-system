from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load movie dataset
movies = pd.read_csv("movies.csv")


def recommend(movie):

    if movie not in movies["title"].values:
        return []

    movie_genre = movies[movies["title"] == movie]["genre"].values[0]

    similar = movies[movies["genre"] == movie_genre]
    similar = similar[similar["title"] != movie]

    recommendations = []

    for index, row in similar.head(6).iterrows():
        recommendations.append({
            "title": row["title"],
            "poster": row["poster"],
            "trailer": row["trailer"]
        })

    return recommendations


@app.route("/", methods=["GET", "POST"])
def home():

    recommended_movies = []

    if request.method == "POST":
        selected_movie = request.form["movie"]
        recommended_movies = recommend(selected_movie)

    return render_template("index.html", movies=movies["title"].values, recommended=recommended_movies)


if __name__ == "__main__":
    app.run(debug=True)