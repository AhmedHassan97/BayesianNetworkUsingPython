import random
import numpy as np


def PGivenE(R_variable, evidence={}):
    "The probability distribution for P(variable | evidence), when all parent variables are known (in evidence)."
    row = tuple(evidence[parent] for parent in R_variable.parents)
    return R_variable.cpt[row]


def Normalize(distribution):
    "Normalize distribution so values sum to 1.0."
    sum = 0
    for i in distribution.values():
        sum += i
    for element in distribution:
        distribution[element] = distribution[element] / sum
        assert 0 <= distribution[element] <= 1, "Probabilities is not between 0 and 1."
    return distribution


def Sample(pd):
    "Randomly sample from a probability distribution."
    temp = 0.0
    rand = random.random()
    for i in pd:
        temp += pd[i]
        if rand <= temp:
            return i


def VariableDomain(variable):
    """This function returns the domain of a variable for example in
    our case if the random variable is AB then its domain will be {lose,win,tie}"""
    domain = [i for i in variable.domain]
    return domain


def ChangeEvidence(evidence, variable, value):
    """
    Take the value, and change the Random variable to this value
    take {AB:"win"} returns {AB:lose} for example
    """
    E_New = evidence.copy()
    E_New[variable] = value
    return E_New


def getChildren(var, ei, bn):
    Children = []
    for i in bn.variables:
        if var in i.parents:
            Children = [i]
    for j in Children:
        if j not in ei:
            Children = [j]
    return Children


def product(arr):
    """product([2, 3, 10]) == 60"""
    Multiplication = 1
    for i in arr:
        Multiplication = Multiplication * i
    return Multiplication


def probability(p):
    """Return true with probability p."""
    rand = np.array([random.uniform(0.0, 1.0) for i in range(len(p))])
    rand = rand / sum(rand)
    labels = [k for k in p]
    values = np.array([p[k] for k in labels])
    return labels[np.argmax(values * rand)]


def INT_Casting(e):
    NewE = e.copy()
    for i in NewE:
        try:
            int(NewE[i])
            NewE.update({i: int(NewE[i])})
        except ValueError:
            continue
    return NewE


def removeSpace(string):
    return string.replace(" ", "")
