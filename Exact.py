from BayesNet import *


def Exact(BN):
    POut = {}
    win = 0
    tie = 0
    lose = 0

    AB_P = 0
    AC_P = 0
    for a in range(4):
        for b in range(4):
            AB_P += \
                P(BN.variables[3], {BN.variables[0]: a, BN.variables[1]: b})[
                    'win']
            for c in range(4):
                AC_P += \
                    P(BN.variables[4],
                      {BN.variables[0]: a, BN.variables[2]: c})[
                        'tie']
    alpha_inv = AB_P * AC_P

    PAB_Win = 0
    PBC_Win = 0
    PBC_Tie = 0
    PBC_Lose = 0
    PAQ = 0
    PBQ = 0
    PCQ = 0

    PAC_Tie_SUM = 0
    for a in range(4):
        PAQ = P(BN.variables[0])[str(a)]
        for b in range(4):
            PBQ = P(BN.variables[1])[str(b)]
            PAB_Win = \
                P(BN.variables[3], {BN.variables[0]: a, BN.variables[1]: b})[
                    'win']
            for c in range(4):
                PCQ = P(BN.variables[2])[str(c)]
                PAC_Tie = \
                    P(BN.variables[4],
                      {BN.variables[0]: a, BN.variables[2]: c})[
                        'tie']
                PBC_Win = \
                    P(BN.variables[5],
                      {BN.variables[1]: b, BN.variables[2]: c})[
                        'win']
                PBC_Tie = \
                    P(BN.variables[5],
                      {BN.variables[1]: b, BN.variables[2]: c})[
                        'tie']
                PBC_Lose = \
                    P(BN.variables[5],
                      {BN.variables[1]: b, BN.variables[2]: c})[
                        'lose']
                factor = PAQ * PBQ * PCQ
                win += PAB_Win * PBC_Win * PAC_Tie * factor
                lose += PAB_Win * PBC_Lose * PAC_Tie * factor
                tie += PAB_Win * PBC_Tie * PAC_Tie * factor

    print(win / (win + tie + lose), lose / (win + tie + lose), tie / (win + tie + lose))
