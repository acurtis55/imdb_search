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
        results = []
        if search_form.data['select'] == 'Title':
            results = imdb_client.searchByTitle(search_form.data['search'])
        elif search_form.data['select'] == 'Genre':
            results = imdb_client.searchByGenre(search_form.data['search'])
        elif search_form.data['select'] == 'Release Year':
            results = imdb_client.searchByReleaseYear(search_form.data['search'])

        return render_template("results.html", form=search_form, movies=results)
    return render_template("index.html", form=search_form)

if __name__ == "__main__":
    app.run()
