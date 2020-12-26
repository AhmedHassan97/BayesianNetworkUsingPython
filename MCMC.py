from NeededFunctions import *
from BayesNet import *


def markov_blanket_sample(X, e, bn):  # X=BC , e={AB: 'win', AC: 'lose', AQ: '1', BQ: '0', CQ: '3', BC: 'lose'}
    """Return a sample from P(X | mb) where mb denotes that the
    variables in the Markov blanket of X take their values from event
    e (which must assign a value to each). The Markov blanket of X is
    X's parents, children, and children's parents."""
    Xnode = X
    Q = {}
    for xi in variable_values(X):
        ei = extend(e, X, xi)

        e_int = to_int(e)
        ei_int = to_int(ei)
        Q[xi] = P(Xnode, e_int)[xi] * product(P(Yj, ei_int)[ei_int[Yj]] for Yj in children(Xnode, ei_int, bn))
    return probability(normalize(Q))


def Gibbs(X, e, bn, N):
    counts = {}
    for x in variable_values(X):
        counts[x] = 0
    Z = [var for var in bn.variables if var not in e]
    state = dict(e)
    for Zi in Z:
        state[Zi] = random.choice(variable_values(Zi))
    for j in range(N):
        for Zi in Z:
            state[Zi] = markov_blanket_sample(Zi, state, bn)
            counts[state[X]] += 1
    return ProbDist(counts)
