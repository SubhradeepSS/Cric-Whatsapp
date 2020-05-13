from flask import Flask, render_template, request
from score import get_Score

app = Flask(__name__)


@app.route('/')
def initial():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def final():
    if request.method == 'POST':
        country = request.form['country']
        obj_score = get_Score(country)
        message = obj_score.get_unique_id()
        return render_template('index.html', message = message)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)