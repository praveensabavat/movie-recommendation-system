from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Movie Data
movies = [
    {
        "title": "Avatar",
        "rating": 8.5,
        "poster": "https://upload.wikimedia.org/wikipedia/en/d/d6/Avatar_%282009_film%29_poster.jpg"
    },
    {
        "title": "Avengers",
        "rating": 8.7,
        "poster": "https://upload.wikimedia.org/wikipedia/en/0/0d/Avengers_Endgame_poster.jpg"
    },
    {
        "title": "The Dark Knight",
        "rating": 9.1,
        "poster": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg"
    },
    {
        "title": "Black Panther",
        "rating": 7.8,
        "poster": "https://upload.wikimedia.org/wikipedia/en/d/d6/Black_Panther_%28film%29_poster.jpg"
    },
    {
        "title": "Baahubali",
        "rating": 8.1,
        "poster": "https://upload.wikimedia.org/wikipedia/en/5/5f/Baahubali_The_Beginning_poster.jpg"
    },
    {
        "title": "RRR",
        "rating": 8.3,
        "poster": "https://upload.wikimedia.org/wikipedia/en/d/d7/RRR_Poster.jpg"
    }
]

# Trailer Links
trailers = {
    "Avatar": "https://www.youtube.com/embed/5PSNL1qE6VY",
    "Avengers": "https://www.youtube.com/embed/TcMBFSGVi1c",
    "The Dark Knight": "https://www.youtube.com/embed/EXeTwQWrcwY",
    "Black Panther": "https://www.youtube.com/embed/xjDjIWPwcPU",
    "Baahubali": "https://www.youtube.com/embed/sOEg_YZQsTI",
    "RRR": "https://www.youtube.com/embed/f_vbAtFSEc0"
}

# Recommendation function
def recommend(movie):
    results = []
    for m in movies:
        if m["title"].lower() != movie.lower():
            results.append(m)
    return results[:5]


@app.route("/", methods=["GET", "POST"])
def home():
    recommended = []

    if request.method == "POST":
        movie = request.form["movie"]
        recommended = recommend(movie)

    return render_template("index.html", recommended=recommended)


@app.route("/suggest")
def suggest():
    q = request.args.get("q", "").lower()
    suggestions = [m["title"] for m in movies if q in m["title"].lower()]
    return jsonify(suggestions)


@app.route("/movie/<title>")
def movie_page(title):

    trailer = trailers.get(title, "")

    movie = None
    for m in movies:
        if m["title"] == title:
            movie = m
            break

    return render_template("movie.html", movie=movie, trailer=trailer)


if __name__ == "__main__":
    app.run(debug=True)