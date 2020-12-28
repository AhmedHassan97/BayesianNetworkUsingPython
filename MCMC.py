from NeededFunctions import *
from BayesNetwork import *


def MB_sample(X, e, bn):
    Prob = {}
    for variable in VariableDomain(X):
        ei = ChangeEvidence(e, X, variable)
        e_int = INT_Casting(e)
        ei_int = INT_Casting(ei)
        product = 1.0
        for child in getChildren(X, ei_int, bn):
            product *= PGivenE(child, ei_int)[ei_int[child]]
        Prob[variable] = (PGivenE(X, e_int)[variable]) * product

    return probability(Normalize(Prob))


def Gibbs(X, given, bn, N):
    """This is the implementation of Gibbs fn in the book,it take the X which is the probability
    i want to calculate, then i initialize each value in its domain by zero,then i store in Z each
    random variable that does not exist in the Given Dictionary, and pick for each random variable
     a random value using random.choice, then pass the state to markov blanket and according to
     return if its a win i increase the win in the values count by 1 and make this an N times
     then i make a probability distribution for these counts. and the one with highest probability
      would be the final value. for example if values count{lose:50 , Win:60, tie:20} it will be a win"""
    ValuesCount = {}
    for x in VariableDomain(X):
        ValuesCount[x] = 0
    Z = [variable for variable in bn.variables if variable not in given]
    state = dict(given)
    for Zi in Z:
        state[Zi] = random.choice(VariableDomain(Zi))
    for j in range(N):
        for Zi in Z:
            state[Zi] = MB_sample(Zi, state, bn)
            ValuesCount[state[X]] += 1
    return PD(ValuesCount)
