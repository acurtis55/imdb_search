from flask import Flask, render_template
from forms import IMDBSearchForm

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    search_form = IMDBSearchForm()
    return render_template("index.html", form=search_form)


if __name__ == "__main__":
    app.run()
