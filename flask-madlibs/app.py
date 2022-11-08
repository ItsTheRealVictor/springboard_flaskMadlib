from flask import Flask, request, render_template
from random import choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)

app.config['SECRET_KEY'] = "farts"
debug = DebugToolbarExtension(app)

first_example_prompts = ['place', 'verb', 'adjective', 'noun1', 'noun2']
first_example_story = 'Yesterday in the {place}, {noun1} had to {verb} their really {adjective} {noun2}'
first_example = Story(first_example_prompts, first_example_story)



@app.route('/')
def main_page():
    return render_template('home.html', example_prompts=first_example.prompts)

@app.route('/story')
def show_story():

    # had to look at the solution for this line
    words = first_example.generate(request.args)


    return render_template('story.html', words=words)



if __name__ == '__main__':
    app.run(debug=True)