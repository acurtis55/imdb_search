from wtforms import Form, StringField, SelectField

class IMDBSearchForm(Form):
    choices = [("Title", "Title"), ("Genre", "Genre"), ("Release Year", "Release Year")]
    select = SelectField("Search By: ", choices=choices)
    search = StringField("")
