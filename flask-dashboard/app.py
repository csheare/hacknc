from flask import Flask, render_template, json, requests
#key=0c02520f1b471cbda395f4f5a96fc8c4
app = Flask(__name__)

@app.route('/')
def main():
    response = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=0c02520f1b471cbda395f4f5a96fc8c4&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres=War")
    # Print the status code of the response.
    print(response.json()['genres'])
    return render_template('index.html')

@app.route('/page2/', methods=['POST'])
def page2():
    return render_template('index2.html')

@app.route('/page3/', methods=['POST'])
def page3():
    return render_template('index3.html')

if __name__ == "__main__":
    app.run(debug = True)
