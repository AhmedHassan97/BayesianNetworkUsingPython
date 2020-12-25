from BayesNet import *
from MCMC import *

CPT = {}
for i in range(4):
    for j in range(4):
        if i > j:
            CPT.update(
                {(i, j): {"win": 1 / 3 + (i - j) * 0.1,
                          "tie": 1 / 3 - (i - j) * 0.05,
                          "lose": 1 / 3 - (i - j) * 0.05}})
        else:
            CPT.update({(i, j): {"win": 1 / 3 + (i - j) * 0.05,
                                 "tie": 1 / 3 + (i - j) * 0.05,
                                 "lose": 1 / 3 - (i - j) * 0.1}})
# Champions_League = (BayesNet()
#       .add('AQ', [], ProbDist({'0': 0.25, '1': 0.25, '2': 0.25, '3': 0.25}))
#       .add('BQ', [], ProbDist({'0': 0.25, '1': 0.25, '2': 0.25, '3': 0.25}))
#       .add('CQ', [], ProbDist({'0': 0.25, '1': 0.25, '2': 0.25, '3': 0.25}))
#       .add('AB', ['AQ', 'BQ'], CPT)
#       .add('AC', ['AQ', 'CQ'], CPT)
#       .add('BC', ['BQ', 'CQ'], CPT))

# e = {Champions_League.variables[3]:'win', Champions_League.variables[4]:'tie'}
# bn = Champions_League
# X=Champions_League.variables[5]
# N=2000
# Approx=Gibbs(X,e,bn,N);
# print(Approx)

NumberOfTeams = input("Please Enter the number of the teams:")
# Enter the Team Qualites
BN = BayesNet()
StartTeam = ord("A")

for i in range(int(NumberOfTeams)):
    name = chr(StartTeam + i) + "Q"
    BN.add(name, [], ProbDist({'0': 0.25, '1': 0.25, '2': 0.25, '3': 0.25}))

StartTeam = ord("A")
for i in range(int(NumberOfTeams)):
    for j in range(i + 1, int(NumberOfTeams), 1):
        name = chr(StartTeam + i) + chr(StartTeam + j)
        Q1 = chr(StartTeam + i) + "Q"
        Q2 = chr(StartTeam + j) + "Q"
        BN.add(name, [Q1, Q2], ProbDist({'0': 0.25, '1': 0.25, '2': 0.25, '3': 0.25}))
print(BN.variables)




