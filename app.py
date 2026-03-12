from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Movie Data
movies = [
{"title":"Avatar","rating":8.5,"poster":"https://image.tmdb.org/t/p/w500/kyeqWdyUXW608qlYkRqosgbbJyK.jpg"},
{"title":"Avengers: Endgame","rating":8.4,"poster":"https://image.tmdb.org/t/p/w500/or06FN3Dka5tukK1e9sl16pB3iy.jpg"},
{"title":"The Dark Knight","rating":9.1,"poster":"https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg"},
{"title":"Black Panther","rating":7.8,"poster":"https://image.tmdb.org/t/p/w500/uxzzxijgPIY7slzFvMotPv8wjKA.jpg"},
{"title":"Baahubali","rating":8.1,"poster":"https://image.tmdb.org/t/p/w500/9BAjt8nSSms62uOVYn1t3C3dVto.jpg"},
{"title":"RRR","rating":8.3,"poster":"https://image.tmdb.org/t/p/w500/lWLSvQ6s2Qh7W8kZz3n1K6TtJ0y.jpg"},
{"title":"Inception","rating":8.8,"poster":"https://image.tmdb.org/t/p/w500/qmDpIHrmpJINaRKAfWQfftjCdyi.jpg"},
{"title":"Interstellar","rating":8.6,"poster":"https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg"},
{"title":"Joker","rating":8.4,"poster":"https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg"},
{"title":"Titanic","rating":7.9,"poster":"https://image.tmdb.org/t/p/w500/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg"},
{"title":"Spider-Man: No Way Home","rating":8.2,"poster":"https://image.tmdb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg"},
{"title":"Iron Man","rating":7.9,"poster":"https://image.tmdb.org/t/p/w500/78lPtwv72eTNqFW9COBYI0dWDJa.jpg"},
{"title":"Doctor Strange","rating":7.5,"poster":"https://image.tmdb.org/t/p/w500/uGBVj3bEbCoZbDjjl9wTxcygko1.jpg"},
{"title":"Thor: Ragnarok","rating":7.9,"poster":"https://image.tmdb.org/t/p/w500/rzRwTcFvttcN1ZpX2xv4j3tSdJu.jpg"},
{"title":"Captain America: Civil War","rating":7.8,"poster":"https://image.tmdb.org/t/p/w500/rAGiXaUfPzY7CDEyNKUofk3Kw2e.jpg"},
{"title":"Guardians of the Galaxy","rating":8.0,"poster":"https://image.tmdb.org/t/p/w500/r7vmZjiyZw9rpJMQJdXpjgiCOk9.jpg"},
{"title":"Deadpool","rating":8.0,"poster":"https://image.tmdb.org/t/p/w500/3E53WEZJqP6aM84D8CckXx4pIHw.jpg"},
{"title":"The Batman","rating":7.9,"poster":"https://image.tmdb.org/t/p/w500/74xTEgt7R36Fpooo50r9T25onhq.jpg"},
{"title":"Man of Steel","rating":7.1,"poster":"https://image.tmdb.org/t/p/w500/7rIPjn5TUK04O25ZkMyHrGNPgLx.jpg"},
{"title":"Justice League","rating":6.1,"poster":"https://image.tmdb.org/t/p/w500/eifGNCSDuxJeS1loAXil5bIGgvC.jpg"},
{"title":"The Matrix","rating":8.7,"poster":"https://image.tmdb.org/t/p/w500/aOIuZAjPaRIE6CMzbazvcHuHXDc.jpg"},
{"title":"John Wick","rating":7.4,"poster":"https://image.tmdb.org/t/p/w500/fZPSd91yGE9fCcCe6OoQr6E3Bev.jpg"},
{"title":"Fast & Furious 7","rating":7.1,"poster":"https://image.tmdb.org/t/p/w500/dCgm7efXDmiABSdWDHBDBx2jwmn.jpg"},
{"title":"Top Gun: Maverick","rating":8.3,"poster":"https://image.tmdb.org/t/p/w500/62HCnUTziyWcpDaBO2i1DX17ljH.jpg"},
{"title":"Dune","rating":8.0,"poster":"https://image.tmdb.org/t/p/w500/d5NXSklXo0qyIYkgV94XAgMIckC.jpg"},
{"title":"Gladiator","rating":8.5,"poster":"https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg"},
{"title":"The Lion King","rating":8.5,"poster":"https://image.tmdb.org/t/p/w500/sKCr78MXSLixwmZ8DyJLrpMsd15.jpg"},
{"title":"Frozen","rating":7.4,"poster":"https://image.tmdb.org/t/p/w500/kgwjIb2JDHRhNk13lmSxiClFjVk.jpg"},
{"title":"Toy Story","rating":8.3,"poster":"https://image.tmdb.org/t/p/w500/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg"},
{"title":"Harry Potter and the Sorcerer's Stone","rating":7.6,"poster":"https://image.tmdb.org/t/p/w500/wuMc08IPKEatf9rnMNXvIDxqP4W.jpg"}
]

# Trailer Links
trailers = {
"Avatar":"https://www.youtube.com/embed/5PSNL1qE6VY",
"Avengers: Endgame":"https://www.youtube.com/embed/TcMBFSGVi1c",
"The Dark Knight":"https://www.youtube.com/embed/EXeTwQWrcwY",
"Black Panther":"https://www.youtube.com/embed/xjDjIWPwcPU",
"Baahubali":"https://www.youtube.com/embed/sOEg_YZQsTI",
"RRR":"https://www.youtube.com/embed/f_vbAtFSEc0",
"Inception":"https://www.youtube.com/embed/YoHD9XEInc0",
"Interstellar":"https://www.youtube.com/embed/zSWdZVtXT7E",
"Joker":"https://www.youtube.com/embed/zAGVQLHvwOY",
"Titanic":"https://www.youtube.com/embed/kVrqfYjkTdQ",
"Spider-Man: No Way Home":"https://www.youtube.com/embed/JfVOs4VSpmA",
"Iron Man":"https://www.youtube.com/embed/8ugaeA-nMTc",
"Doctor Strange":"https://www.youtube.com/embed/HSzx-zryEgM",
"Thor: Ragnarok":"https://www.youtube.com/embed/ue80QwXMRHg",
"Captain America: Civil War":"https://www.youtube.com/embed/dKrVegVI0Us",
"Guardians of the Galaxy":"https://www.youtube.com/embed/d96cjJhvlMA",
"Deadpool":"https://www.youtube.com/embed/Xithigfg7dA",
"The Batman":"https://www.youtube.com/embed/mqqft2x_Aa4",
"Man of Steel":"https://www.youtube.com/embed/T6DJcgm3wNY",
"Justice League":"https://www.youtube.com/embed/3cxixDgHUYw",
"The Matrix":"https://www.youtube.com/embed/vKQi3bBA1y8",
"John Wick":"https://www.youtube.com/embed/2AUmvWm5ZDQ",
"Fast & Furious 7":"https://www.youtube.com/embed/Skpu5HaVkOc",
"Top Gun: Maverick":"https://www.youtube.com/embed/giXco2jaZ_4",
"Dune":"https://www.youtube.com/embed/8g18jFHCLXk",
"Gladiator":"https://www.youtube.com/embed/owK1qxDselE",
"The Lion King":"https://www.youtube.com/embed/7TavVZMewpY",
"Frozen":"https://www.youtube.com/embed/TbQm5doF_Uc",
"Toy Story":"https://www.youtube.com/embed/KYz2wyBy3kc",
"Harry Potter and the Sorcerer's Stone":"https://www.youtube.com/embed/VyHV0BRtdxo"
}

# Recommendation Function
def recommend(movie):
    results = [m for m in movies if m["title"].lower() != movie.lower()]
    return random.sample(results, 5)

@app.route("/", methods=["GET","POST"])
def home():
    recommended = []

    if request.method == "POST":
        movie = request.form["movie"]
        recommended = recommend(movie)

    return render_template("index.html", recommended=recommended)

@app.route("/suggest")
def suggest():
    q = request.args.get("q","").lower()
    suggestions = [m["title"] for m in movies if q in m["title"].lower()]
    return jsonify(suggestions)

@app.route("/movie/<title>")
def movie_page(title):

    trailer = trailers.get(title,"")

    movie = None
    for m in movies:
        if m["title"] == title:
            movie = m
            break

    return render_template("movie.html", movie=movie, trailer=trailer)

if __name__ == "__main__":
    app.run(debug=True)