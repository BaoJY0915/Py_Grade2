import random
def Guiding():
    prA = eval(input('先发A的能力：'))
    prB = eval(input('后发B的能力：'))
    n = eval(input('场次：'))
    return prA,prB,n
    
def Ngame(prA,prB,n):
    winA = 0
    winB = 0
    for i in range(n):
        scoreA,scoreB = OneGame(prA,prB)
        if scoreA > scoreB:
            winA += 1
        else:
            winB += 1
    return winA,winB

def OneGame(prA,prB):
    scoreA = scoreB = 0
    serving = 'A'
    while not GameOver(scoreA,scoreB):
        if serving == 'A':
            if random.random() < prA/(prA + prB):
                scoreA += 1
            else:
                serving = 'B'
        else:
            if random.random() < prB/(prA + prB):
                scoreB += 1
            else:
                serving = 'A'
    return scoreA,scoreB

def GameOver(sa,sb):
    if sa == 15 or sb == 15:
        return True
    return False

def Shuchu(winA,winB):
    n = winA + winB
    print('共{}场比赛\n选手A获胜{}场，选手B获胜{}场'.format(n,winA,winB))
    print('A胜率为{:.2%}，B胜率为{:.2%}'.format(winA/n,winB/n))

def main():
    prA,prB,n = Guiding()
    winA,winB = Ngame(prA,prB,n)
    Shuchu(winA,winB)

main()    
