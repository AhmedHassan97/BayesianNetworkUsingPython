import itertools
from NeededFunctions import *


class BayesNetwork(object):
    "Bayesian network: class used to build the network and include the method add that adds the nodes to the network "

    def __init__(self):
        self.variables = []
        self.lookup = {}

    def add(self, name, Pnames, cpt):
        """Adds a new Random Variable to the Network , it take the name of the random
          variable and its parents and the Parent names must have been added previously."""
        parents = [self.lookup[name] for name in Pnames]
        var = Variable(name, cpt, parents)
        self.variables.append(var)
        self.lookup[name] = var
        return self


class Variable(object):
    "A discrete random variable"

    def __init__(self, name, cptable, parents=()):
        "A variable has a name, list of parent variables, and a Conditional Probability Table."
        self.__name__ = name
        self.parents = parents
        self.cpt = CPTable(cptable, parents)
        self.domain = set(itertools.chain(*self.cpt.values()))  # the domain of each variable

    def __repr__(self): return self.__name__


class Factor(dict): ""


class PD(Factor):
    """A Probability Distribution is an {outcome: probability} mapping.
    The values are normalized to sum to 1.
    ProbDist(0.75) is an abbreviation for ProbDist({T: 0.75, F: 0.25})."""

    def __init__(self, mapping=(), **kwargs):
        self.update(mapping, **kwargs)
        Normalize(self)


class Given(dict):
    "for example  {AB: 'win' } , this is the given and we know"


class CPTable(dict):
    "A mapping of {row: PD, ...} where each row is a tuple of values of the parent variables."

    def __init__(self, mapping, parents=()):
        if len(parents) == 0 and not (isinstance(mapping, dict) and set(mapping.keys()) == {()}):
            mapping = {(): mapping}
        for (row, dist) in mapping.items():
            if len(parents) == 1 and not isinstance(row, tuple):
                row = (row,)
            self[row] = PD(dist)

