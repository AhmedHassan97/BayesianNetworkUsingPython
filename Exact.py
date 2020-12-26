from BayesNetwork import *


def Exact(BN, e):
    POut = {}
    win = 0
    tie = 0
    lose = 0

    AB_P = 0
    AC_P = 0
    FirstMatchResult = e[BN.variables[3]]
    SecondMatchResult = e[BN.variables[4]]

    for a in range(4):
        for b in range(4):
            AB_P += \
                PGivenE(BN.variables[3], {BN.variables[0]: a, BN.variables[1]: b})[FirstMatchResult]
            for c in range(4):
                AC_P += \
                    PGivenE(BN.variables[4],
                            {BN.variables[0]: a, BN.variables[2]: c})[SecondMatchResult]
    alpha_inv = AB_P * AC_P
    for a in range(4):
        PAQ = PGivenE(BN.variables[0])[str(a)]
        for b in range(4):
            PBQ = PGivenE(BN.variables[1])[str(b)]
            PAB_Win = \
                PGivenE(BN.variables[3], {BN.variables[0]: a, BN.variables[1]: b})[
                    FirstMatchResult]
            for c in range(4):
                PCQ = PGivenE(BN.variables[2])[str(c)]
                PAC_Tie = \
                    PGivenE(BN.variables[4],
                            {BN.variables[0]: a, BN.variables[2]: c})[
                        SecondMatchResult]
                PBC_Win = \
                    PGivenE(BN.variables[5],
                            {BN.variables[1]: b, BN.variables[2]: c})[
                        'win']
                PBC_Tie = \
                    PGivenE(BN.variables[5],
                            {BN.variables[1]: b, BN.variables[2]: c})[
                        'tie']
                PBC_Lose = \
                    PGivenE(BN.variables[5],
                            {BN.variables[1]: b, BN.variables[2]: c})[
                        'lose']
                factor = PAQ * PBQ * PCQ
                win += PAB_Win * PBC_Win * PAC_Tie * factor
                lose += PAB_Win * PBC_Lose * PAC_Tie * factor
                tie += PAB_Win * PBC_Tie * PAC_Tie * factor
    sum = (win / ((win + tie + lose)*alpha_inv)) + (lose / ((win + tie + lose)*alpha_inv))+(tie / ((win + tie + lose)*alpha_inv))

    print('Win', (win / ((win + tie + lose)*alpha_inv))/sum, 'Lose', (lose / ((win + tie + lose)*alpha_inv))/sum, 'Tie', (tie / ((win + tie + lose)*alpha_inv))/sum)
