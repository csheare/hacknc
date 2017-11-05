from flask import Flask, render_template, json, request
import requests, random

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

app = Flask(__name__)

with open('./static/files/genres.json') as data_file:
    genres = json.load(data_file)

def sentiment_text(text):
    """Detects sentiment in the text."""
    client = language.LanguageServiceClient()
    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects sentiment in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    sentiment = client.analyze_sentiment(document).document_sentiment
    return sentiment.score

movie_dict = dict()
image_dict = dict()
errorMessage = ""

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/page2/', methods=['POST','GET'])
def page2():
    year = request.form.get('year')
    genre = request.form.get('genre')
    genre_id = genres[genre]
    response = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=0c02520f1b471cbda395f4f5a96fc8c4&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres="+str(genre_id)+"&primary_release_year="+year)
    # Print the status code of the response.
    num_results = len(response.json()['results'])
    if(num_results >= 5 ):
        img1="http://image.tmdb.org/t/p/w185/" + response.json()['results'][0]["poster_path"]
        movie_dict[str(response.json()['results'][0]["original_title"])] = response.json()['results'][0]["overview"]
        image_dict[str(response.json()['results'][0]["original_title"])] = img1
        t1=response.json()['results'][0]["original_title"]
        img2="http://image.tmdb.org/t/p/w185/" + response.json()['results'][1]["poster_path"]
        movie_dict[str(response.json()['results'][1]["original_title"])] = response.json()['results'][1]["overview"]
        image_dict[str(response.json()['results'][1]["original_title"])] = img2
        t2=response.json()['results'][1]["original_title"]
        img3="http://image.tmdb.org/t/p/w185/" + response.json()['results'][2]["poster_path"]
        movie_dict[str(response.json()['results'][2]["original_title"])] = response.json()['results'][2]["overview"]
        image_dict[str(response.json()['results'][2]["original_title"])] = img3
        t3=response.json()['results'][2]["original_title"]
        img4="http://image.tmdb.org/t/p/w185/" + response.json()['results'][3]["poster_path"]
        movie_dict[str(response.json()['results'][3]["original_title"])] = response.json()['results'][3]["overview"]
        image_dict[str(response.json()['results'][3]["original_title"])] = img4
        t4=response.json()['results'][3]["original_title"]
        img5="http://image.tmdb.org/t/p/w185/" + response.json()['results'][4]["poster_path"]
        movie_dict[str(response.json()['results'][4]["original_title"])] = response.json()['results'][4]["overview"]
        image_dict[str(response.json()['results'][4]["original_title"])] = img5
        t5=response.json()['results'][4]["original_title"]
    else:
        errorMessage = "Not Enough Movies, Select Again"

    return render_template('index2.html',**locals())

@app.route('/page3/', methods=['POST','GET'])
def page3():

    m1 = request.form.get('m1')
    m2 = request.form.get('m2')
    i1 = image_dict[str(m1)]
    i2 = image_dict[str(m2)]
    print(movie_dict)
    ov1 = movie_dict[str(m1)]
    score1 = sentiment_text(ov1)
    ov2 = movie_dict[str(m2)]
    score2 = sentiment_text(ov2)
    if max(score1,score2) == score2 :
        winner = m2
    else:
        winner = m1

    return render_template('index3.html',**locals())

if __name__ == "__main__":
    app.run(debug = True)
