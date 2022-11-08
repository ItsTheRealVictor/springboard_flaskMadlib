from flask import Flask, request, render_template
from random import choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)

app.config['SECRET_KEY'] = "farts"
debug = DebugToolbarExtension(app)


@app.route('/')
def main_page():
    return render_template('home.html')

@app.route('/story')
def show_story():
    return 'its a story'

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

if __name__ == '__main__':
    app.run(debug=True)