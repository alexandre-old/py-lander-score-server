from . import db, models


class PlayerController():

    """Docstring for PlayerController. """

    self.nick = ''
    self.fuel = 0.0
    self.multiplier = 0.0

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
            score=self._calc_score
        )
        db.session.add(player)
        db.session.commit()
