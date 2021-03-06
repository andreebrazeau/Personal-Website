__author__ = 'abrazeau'


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home(name=None):
    return render_template('index.html', name=name)

@app.route("/portfolio")
def portfolio(name=None):
    return render_template('portfolio.html', name=name)

@app.route("/about")
def about(name=None):
    return render_template('about.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)