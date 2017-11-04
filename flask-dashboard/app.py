from flask import Flask, render_template, json, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/page2/', methods=['POST'])
def page2():
    return render_template('index2.html')

@app.route('/page3/', methods=['POST'])
def page3():
    return render_template('index3.html')

if __name__ == "__main__":
    app.run(debug = True)
