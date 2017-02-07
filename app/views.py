from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = { "nickname": "koalatea" }
    drinks = [
        {
            'drink_name' : 'Godfather',
            'ingredients' : [ 'half ameretto', 'half scotch whiskey' ]
        },
        {
            'drink_name' : 'temp test',
            'ingredients' : [ 'nothing', 'more nothing' ]
        }
    ]
    return render_template('index.html', title='Home', user=user, drinks=drinks)
