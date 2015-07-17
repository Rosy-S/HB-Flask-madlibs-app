from random import choice, sample

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return render_template("hello.html")

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.form.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html", person=player, compliments=compliments)

@app.route('/game', methods=["POST", "GET"])
def show_game_form():
    if request.method == "GET": 
        response = request.args.get("game")
        if response == "yes":
            return render_template("game.html")
        else:
            return render_template("goodbye.html")
    else: 
        response = request.form.get("game")
        if response == "yes":
            return render_template("game.html")
        else:
            return render_template("goodbye.html")


@app.route('/madlib', methods=["POST", "GET"])
def show_madlib():
    if request.method == "POST":
        player = request.form.get("person")
        colors = request.form.get('color')
        nouns = request.form.get('noun')
        adjectives = request.form.get('adjective')
        verbs = request.form.get('verb')
    else: 
        player = request.args.get("person")
        colors = request.args.get('color')
        nouns = request.args.get('noun')
        adjectives = request.args.get('adjective')
        verbs = request.args.get('verb')

    templates = ['madlib.html', 'madlib2.html', 'madlib3.html']
    template = templates[choice(range(3))]
    return render_template(template, person_entry=player , color_entry=colors , noun_entry=nouns , adjective_entry=adjectives, verb_entry=verbs)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
