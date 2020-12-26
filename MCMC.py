from NeededFunctions import *
from BayesNetwork import *


def MB_sample(X, e, bn):  # X=BC , e={AB: 'win', AC: 'lose', AQ: '1', BQ: '0', CQ: '3', BC: 'lose'}
    Q = {}
    for xi in VariableDomain(X):
        ei = ChangeEvidence(e, X, xi)
        e_int = INT_Casting(e)
        ei_int = INT_Casting(ei)

        Q[xi] = PGivenE(X, e_int)[xi] * product(PGivenE(Yj, ei_int)[ei_int[Yj]] for Yj in getChildren(X, ei_int, bn))

    return probability(Normalize(Q))


def Gibbs(X, evidence, bn, N):
    ValuesCount = {}
    for x in VariableDomain(X):
        ValuesCount[x] = 0
    Z = [variable for variable in bn.variables if variable not in evidence]
    state = dict(evidence)
    for Zi in Z:
        state[Zi] = random.choice(VariableDomain(Zi))
    for j in range(N):
        for Zi in Z:
            state[Zi] = MB_sample(Zi, state, bn)
            ValuesCount[state[X]] += 1
    return PD(ValuesCount)
