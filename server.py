"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
    <html>Hi! This is the home page.
    Let's begin by asking <a href='/hello'>your name</a>!
    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <br>
          Choose a compliment:
          <select name="compliment">
          <option value="terrific">terrific</option>
          <option value="fantastic">fantastic</option>
          <option value="fantabulous">fantabulous</option>
          </select>
          <input type="submit" value="Submit">
        </form>
        <br>
        <form action="/diss" method="POST">
        Or an insult:
        <select name="insult">
        <option value="awful">bad choice</option>
        <option value="bad at Python">sadistic choice</option>
        <option value="lazy">tame choice</option>
        <br>
        <input type="submit" value="Oh no">
        </form>
      </body>
    </html>
    """


@app.route('/diss', methods=["POST"])
def diss_person():
    """Insults user >:("""

    insult = request.form.get("insult")

    return """
    <!doctype html>
      <html>
        <head>
          <title>An Insult</title>
        </head>
        <body>
          Wow... I think you're {insult}!
        </body>
      </html>
      """.format(insult=insult)   


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
