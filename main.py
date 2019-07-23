from flask import Flask, render_template, request
from forms import IMDBSearchForm
from IMDBClient import IMDBClient

app = Flask(__name__)
app.secret_key = "my secret key"
imdb_client = IMDBClient()

@app.route('/', methods=['GET', 'POST'])
def index():
    search_form = IMDBSearchForm(request.form)
    if request.method == "POST":
        print(search_form.data['search'])
        results = imdb_client.searchByReleaseYear('2012')
        return render_template("results.html", form=search_form, movies=results)
    return render_template("index.html", form=search_form)

if __name__ == "__main__":
    app.run()
