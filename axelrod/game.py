from typing import Tuple, Union

from axelrod import Action

C, D = Action.C, Action.D

Score = Union[int, float]


class Game(object):
    """Container for the game matrix and scoring logic.

    Attributes
    ----------
    scores: dict
        The numerical score attribute to all combinations of action pairs.
    """

    def __init__(
        self, r: Score = 3, s: Score = 0, t: Score = 5, p: Score = 1, rc: Score = 3, sc: Score = 0, tc: Score = 5, pc: Score = 1
    ) -> None:
        """Create a new game object.

        Parameters
        ----------
        r: int or float
            Score obtained by row players for mutual cooperation.
        s: int or float
            Score obtained by row player for cooperating against column defector.
        t: int or float
            Score obtained by row player for defecting against column cooperator.
        p: int or float
            Score obtained by row player for mutual defection.
        rc: int or float
            Score obtained by column players for mutual cooperation.
        sc: int or float
            Score obtained by column player for cooperating against row defector.
        tc: int or float
            Score obtained by column player for defecting against row cooperator.
        pc: int or float
            Score obtained by column player for mutual defection.    
        """
        self.scores = {
            (C, C): (r, rc),
            (D, D): (p, pc),
            (C, D): (s, tc),
            (D, C): (t, sc),
        }

    def RPST(self) -> Tuple[Score, Score, Score, Score]:
        """Returns game matrix values in Press and Dyson notation."""
        R = self.scores[(C, C)][0]
        P = self.scores[(D, D)][0]
        S = self.scores[(C, D)][0]
        T = self.scores[(D, C)][0]
        return R, P, S, T

    def score(self, pair: Tuple[Action, Action]) -> Tuple[Score, Score]:
        """Returns the appropriate score for a decision pair.

        Parameters
        ----------
        pair: tuple(Action, Action)
            A pair actions for two players, for example (C, C).

        Returns
        -------
        tuple of int or float
            Scores for two player resulting from their actions.
        """
        return self.scores[pair]

    def __repr__(self) -> str:
        return "Axelrod game: (R,P,S,T) = {}".format(self.RPST())

    def __eq__(self, other):
        if not isinstance(other, Game):
            return False
        return self.RPST() == other.RPST()


DefaultGame = Game()
