from . import db, models


class PlayerController():

    """Docstring for PlayerController. """

    nick = ''
    fuel = 0.0
    multiplier = 0.0

    def __init__(self, nick, fuel, multiplier):
        """TODO: Docstring for __init__.

        :nick: TODO
        :fuel: TODO
        :multiplier: TODO
        :returns: TODO

        """
        self.nick = nick
        self.fuel = float(fuel)
        self.multiplier = float(multiplier)

    def _calc_score(self):
        """TODO: Docstring for _calc_score.
        :returns: TODO

        """
        return self.multiplier * self.fuel

    def gen_nick(self):
        """TODO: Docstring for gen_nick.
        :returns: TODO

        """
        return 'It Works!'

    def save_score(self):
        """TODO: Docstring for save_score.
        :returns: TODO

        """
        player = models.Player(
            nick=self.nick,
            fuel=self.fuel,
            multiplier=self.multiplier,
            score=self._calc_score()
        )
        db.session.add(player)
        db.session.commit()

    @classmethod
    def get_all_players(cls):
        """TODO: Docstring for get_all_players.

        :returns: TODO

        """
        return models.Player.query.all() 
