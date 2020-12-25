import random
import numpy as np

def P(var, evidence={}):
    "The probability distribution for P(variable | evidence), when all parent variables are known (in evidence)."
    row = tuple(evidence[parent] for parent in var.parents)
    return var.cpt[row]


def normalize(dist):
    "Normalize a {key: value} distribution so values sum to 1.0. Mutates dist and returns it."
    total = sum(dist.values())
    for key in dist:
        dist[key] = dist[key] / total
        assert 0 <= dist[key] <= 1, "Probabilities must be between 0 and 1."
    return dist


def sample(probdist):
    "Randomly sample an outcome from a probability distribution."
    r = random.random()  # r is a random point in the probability distribution
    c = 0.0  # c is the cumulative probability of outcomes seen so far
    for outcome in probdist:
        c += probdist[outcome]
        if r <= c:
            return outcome
def globalize(mapping):
    "Given a {name: value} mapping, export all the names to the `globals()` namespace."
    globals().update(mapping)


def variable_values(var):
    a = [k for k in var.domain]
    return a


def prob(var, val, e):
    return P(var, e)[val]


def extend(s, var, val):
    """Copy the substitution s and extend it by setting var to val; return copy."""
    s2 = s.copy()
    s2[var] = val
    return s2


def children(var, ei, bn):
    chldrn = [i for i in bn.variables if var in i.parents]
    chldrn = [i for i in chldrn if i not in ei]
    return chldrn


def product(numbers):
    """Return the product of the numbers, e.g. product([2, 3, 10]) == 60"""
    result = 1
    for x in numbers:
        result *= x
    return result
def probability(p):
    """Return true with probability p."""
    rand = np.array([random.uniform(0.0, 1.0) for i in range(len(p))])
    rand = rand/sum(rand)
    labels = [k for k in p]
    vals = np.array( [p[k] for k in labels])
    return labels[np.argmax(vals*rand)]
# probability({'win':0.34,'lose':0.295,'tie':0.295})
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
def to_int(e):
    e_int = e.copy()
    for i in e_int:
        if RepresentsInt(e_int[i]):
            e_int.update({i:int(e_int[i])})
    return e_int