from flask import Flask, render_template
from lib import home

app = Flask(__name__)


@app.route('/')
def index():
    docs = home.get_docs()
    return render_template("index.html", docs=docs)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
