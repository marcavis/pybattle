import random
def showStat(stat):
    return '{:02d}'.format(stat[0]) + "/" + '{:02d}'.format(stat[1])

def weaponFactor(entity):
    return 0.75 + random.random() / 2

class Character:
    def __init__(self, name, pv, ph, at, df, ag, control):
        self.name = name
        self.pv = (pv, pv) #vida
        self.ph = (ph, ph) #magia
        self.at = (at, at) #ataque
        self.df = (df, df) #defesa
        self.ag = (ag, ag) #agilidade
        self.control = control #diz se é controlado pelo jogador
        self.progress = 0 #quão próximo está da prox. rodada
        self.alive = True

    def attack(self, target):
        print(self.name + " atacou " + target.name)
        target.attacked(self)

    def attacked(self, origin):
        self.damage((origin.at[0] - self.df[0]) * weaponFactor(origin))

    def damage(self, amount):
        amount = round(amount)
        if(amount > 0):
            self.pv = (self.pv[0] - amount, self.pv[1])
            print(self.name + " sofreu " + str(amount) + " pontos de dano.")
        if(self.pv[0] < 1):
            self.alive = False

    def act(self):
        self.progress -= 1000
        if(self.control):
            print("O que você vai fazer?")

    def __str__(self):
        return '{:>16}'.format(self.name) + \
        ": PV:" + showStat(self.pv) + ", PH:" + showStat(self.ph) + \
         ", AT:" + showStat(self.at) + ", DF:" + showStat(self.df) + \
         ", AG:" + showStat(self.ag) + ", PTR:" + str(self.progress) + "/1000"
