from BayesNet import *
from MCMC import *
from Exact import Exact
from NeededFunctions import *

CPT = {}
for Q1 in range(4):
    for Q2 in range(4):
        if Q1 > Q2:
            CPT.update(
                {(Q1, Q2): {"win": 1 / 3 + (Q1 - Q2) * 0.2,
                            "tie": 1 / 3 - (Q1 - Q2) * 0.1,
                            "lose": 1 / 3 - (Q1 - Q2) * 0.1}})
        else:
            CPT.update({(Q1, Q2): {"win": 1 / 3 + (Q1 - Q2) * 0.1,
                                   "tie": 1 / 3 + (Q1 - Q2) * 0.1,
                                   "lose": 1 / 3 - (Q1 - Q2) * 0.2}})

NumberOfTeams = input("Please Enter the number of the teams:")
# Enter the Team Qualites
BN = BayesNet()
StartTeam = ord("A")
for i in range(int(NumberOfTeams)):
    name = chr(StartTeam + i) + "Q"
    BN.add(name, [], ProbDist({'0': 0.25, '1': 0.25, '2': 0.25, '3': 0.25}))

print(BN.variables)

StartTeam = ord("A")
NumberOfMatches = 0
lastmatch = ""
for i in range(int(NumberOfTeams)):
    for j in range(i + 1, int(NumberOfTeams), 1):
        name = chr(StartTeam + i) + chr(StartTeam + j)
        Q1 = chr(StartTeam + i) + "Q"
        Q2 = chr(StartTeam + j) + "Q"
        BN.add(name, [Q1, Q2], CPT)
        NumberOfMatches += 1

StartTeam = ord("A")
e = {}

print(e)
count = 0
# --------------------------------------------Take the matches results------------------------------------
for i in range(int(NumberOfTeams)):
    for j in range(i + 1, int(NumberOfTeams), 1):
        if count == NumberOfMatches - 1:
            break
        result = input("Enter the results of the " + str(count + 1) + " match : \t")

        while result != "win" and result != "lose" and result != "tie":
            result = input("Only enter win or lose tie: \t")
        name = chr(StartTeam + i) + chr(StartTeam + j)
        count += 1

        for l in BN.variables:
            if str(l) == name:
                e[l] = result

print(e)

Exact_OR_MCMC = input("Enter 0 for Exact and 1 for MCMC ")

while Exact_OR_MCMC != "0" and Exact_OR_MCMC != "1":
    print("Only 0 or 1")
    Exact_OR_MCMC = input("Enter 0 for Exact and 1 for MCMC ")

if Exact_OR_MCMC == "0":  # exact
    if int(NumberOfTeams) > 3:
        print("Only Calculate the exact for 3 teams")
    else:
        Exact(BN)
else:
    N = input("choose the number of iterations: \t")
    print(Gibbs(BN.variables[-1], e, BN, int(N)))
