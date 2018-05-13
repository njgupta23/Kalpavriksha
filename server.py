from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.secret_key = "a secret..."

@app.route('/')
def homepage():
    """Displays homepage."""

    return render_template('homepage.html')

@app.route('/shop')
def shop():
    """Displays items to purchase."""

    return render_template('shop.html')



if __name__ == "__main__":
    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
    DebugToolbarExtension(app)
    # connect_to_db(app)
    app.run("0.0.0.0", debug=True)
