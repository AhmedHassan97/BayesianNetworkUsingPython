from BayesNetwork import *
from MCMC import *
from Exact import Exact
from NeededFunctions import *

CPTable = {}
NumberOfTeams = input("Please Enter the number of the teams:")
NumberOfTeams=removeSpace(NumberOfTeams)
while True:
    try:
        int(NumberOfTeams)
        break
    except ValueError:
        NumberOfTeams = input("Please Enter a valid Number:\t")

for Q1 in range(4):
    for Q2 in range(4):
        if Q1 > Q2:
            CPTable.update(
                {(Q1, Q2): {"win": (1 / int(NumberOfTeams)) + (Q1 - Q2) * 0.1,
                            "tie": (1 / int(NumberOfTeams)) - (Q1 - Q2) * 0.05,
                            "lose": (1 / int(NumberOfTeams)) - (Q1 - Q2) * 0.05}})
        else:
            CPTable.update({(Q1, Q2): {"win": (1 / int(NumberOfTeams)) + (Q1 - Q2) * 0.05,
                                       "tie": (1 / int(NumberOfTeams)) + (Q1 - Q2) * 0.05,
                                       "lose": (1 / int(NumberOfTeams)) - (Q1 - Q2) * 0.1}})

# Enter the Team Qualites
BN = BayesNetwork()
StartTeam = ord("A")
for i in range(int(NumberOfTeams)):
    name = chr(StartTeam + i) + "Q"
    BN.add(name, [], PD({'0': 0.25, '1': 0.25, '2': 0.25, '3': 0.25}))

StartTeam = ord("A")
NumberOfMatches = 0

for i in range(int(NumberOfTeams)):
    for j in range(i + 1, int(NumberOfTeams), 1):
        name = chr(StartTeam + i) + chr(StartTeam + j)
        Q1 = chr(StartTeam + i) + "Q"
        Q2 = chr(StartTeam + j) + "Q"
        BN.add(name, [Q1, Q2], CPTable)
        NumberOfMatches += 1

StartTeam = ord("A")
e = {}

count = 0
# --------------------------------------------Take the matches results------------------------------------
for i in range(int(NumberOfTeams)):
    for j in range(i + 1, int(NumberOfTeams), 1):
        if count == NumberOfMatches - 1:
            break
        result = input("Enter the results of the " + str(count + 1) + " match : \t")
        result = removeSpace(result)
        while result != "win" and result != "lose" and result != "tie":
            result = input("Only enter win or lose tie: \t")
            result = removeSpace(result)
        name = chr(StartTeam + i) + chr(StartTeam + j)
        count += 1

        for l in BN.variables:
            if str(l) == name:
                e[l] = result

print(e)

Exact_OR_MCMC = input("Enter 0 for Exact and 1 for MCMC ")
Exact_OR_MCMC=removeSpace(Exact_OR_MCMC)
while Exact_OR_MCMC != "0" and Exact_OR_MCMC != "1":
    print("Only 0 or 1")
    Exact_OR_MCMC = input("Enter 0 for Exact and 1 for MCMC ")
    Exact_OR_MCMC = removeSpace(Exact_OR_MCMC)

if Exact_OR_MCMC == "0":  # exact
    if int(NumberOfTeams) > 3:
        print("Only Calculate the exact for 3 teams")
    else:
        Exact(BN, e)
else:
    N = input("choose the number of iterations: \t")
    print(Gibbs(BN.variables[-1], e, BN, int(N)))
