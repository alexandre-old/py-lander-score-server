# py-lander-server

### About py-lander

Py-lander is a game that is being written in Python with PyGame - check out:
[py-lander](https://github.com/lucasdnd/py-lander)

### What's that?
It's just a simple server to register the players' score.

### The availables routes (for now)

* __/player/new =>__ : A route to get a nickname. Using random number while I'm trying create a nickname db...maybe
using a function to generate random starship names.

* __/player/\<nick\> =>__ : A route to get info about one player (filter by nickname).

* __/player/list =>__ : A route to list all players with detailed info. (score, fuel and etc)

* __/player/save_score =>__ : A route to save the score.

### What you used to write this server?

This app was written using Python3 (3.4.2), Flask, SQLAlchemy (and Flask-SQLAlchemy) and SQLite3. There is a version
deployed on heroku (using gunicorn):

__pylander-score-server.herokuapp.com__

### Can I run my own instance?

* Clone this repo: ```git clone https://github.com/lucasdnd/pylander-score-server```
* Install the dependencies: ```pip install -r pylander-score-server/requirements.txt```
* Execute the run.py: ```python run.py```

Or you can just deploy it on heroku:

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/lucasdnd/pylander-score-server.git)
