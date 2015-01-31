from . import db
import json


class Player(db.Model):

    """Docstring for Player. """

    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(255))
    fuel = db.Column(db.Float)
    multiplier = db.Column(db.Float)
    score = db.Column(db.Float)

    def __init__(self, nick, fuel, multiplier, score):
        """TODO: Docstring for __init__.

        :nick: TODO
        :fuel: TODO
        :multiplier: TODO
        :score: TODO
        :returns: TODO

        """
        self.nick = nick
        self.fuel = fuel
        self.multiplier = multiplier
        self.score = score

    def __repr__(self):
        """TODO: Docstring for __repr__.
        :returns: TODO

        """
        return '<Player %r>' % self.nick

    def to_json(self):
        """TODO: Docstring for to_json.
        :returns: TODO

        """
        return json.dumps({
            'nick': self.nick,
            'fuel': self.fuel,
            'multiplier': self.multiplier,
            'score': self.score
        })
