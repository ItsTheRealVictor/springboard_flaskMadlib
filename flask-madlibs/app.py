from flask import Flask, request, render_template
from random import choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)

app.config['SECRET_KEY'] = "farts"
debug = DebugToolbarExtension(app)

example_prompts = ['place', 'verb', 'adjective', 'noun1', 'noun2']
example_story = 'Yesterday in the {place}, {noun1} had to {verb} their really {adjective} {noun2}'

@app.route('/')
def main_page():
    return render_template('home.html', example_prompts=example_prompts)

@app.route('/story')
def show_story():
    return 'its a story'



if __name__ == '__main__':
    app.run(debug=True)