"""BONUS QUESTION:
Abigail and Benson are playing Rock, Paper, Scissors.
Each game is represented by an array of length 2, where the first element 
represents what Abigail played and the second element represents what Benson
played.
Given a sequence of games, determine who wins the most number of matches. If they tie, output "Tie".
R stands for Rock
P stands for Paper
S stands for Scissors"""


def calculate_score(alist):
    # print(alist)
    winList = []
    for i in alist:
        # print(i)
        # print(i[0])
        if i[0] == i[-1]:
            print('Draw')
            winList.append('Draw')
        elif (i[0] == 'R') and (i[-1] == 'P'):
            print("Paper beats Rock")
            winList.append('Right')
        elif (i[0] == 'R') and (i[-1] == 'S'):
            print("Rock beats Scissors")
            winList.append('Left')
        elif (i[0] == 'S') and (i[-1] == 'P'):
            print("Scissors beat Paper")
            winList.append('Left')
        elif (i[0] == 'S') and (i[-1] == 'R'):
            print("Rock beats Scissors")
            winList.append("Right")
    print('')
    abiwins = winList.count('Left')
    benwins = winList.count('Right')
    draw = winList.count('draw')
    print(abiwins)
    print(benwins)
    print(winList)
calculate_score([["R", "R"], ["S", "S"]])
calculate_score([["R", "P"], ["R", "S"], ["S", "P"]])
calculate_score([["S", "R"], ["R", "S"], ["R", "R"]])