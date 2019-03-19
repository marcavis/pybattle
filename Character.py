import random
import Effect
from EffectType import *

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
        self.entities = [] #cópia da informação de unidades na batalha
        self.effects = [] #efeitos que modificam o personagem

        #special modifiers
        self.damageResist = 0.0

    def attack(self, target):
        print(self.name + " atacou " + target.name)
        target.attacked(self)

    def attacked(self, origin):
        self.damage((origin.at[0] - self.df[0]) * weaponFactor(origin) * (1 - self.damageResist))

    def damage(self, amount):
        amount = round(amount)
        if(amount < 1):
            amount = 1
        self.pv = (self.pv[0] - amount, self.pv[1])
        print(self.name + " sofreu " + str(amount) + " pontos de dano.")
        input()
        if(self.pv[0] < 1):
            self.alive = False

    def validAttackTargets(self):
        if(self.control):
            return [x for x in self.entities if x.alive and not x.control]
        else:
            return [x for x in self.entities if x.alive and x.control]

    def act(self):
        for effect in self.effects:
            effect.handleTurn()
        self.effects = [x for x in self.effects if not x.inactive] #excluir efeitos vencidos
        if(self.control):
            reset = False
            print("1 - Atacar / 2 - Habilidades / 3 - Itens / 4 - Proteger-se")
            op = "0"
            while op not in ["1", "2", "3", "4"]:
                op = input("O que você vai fazer, " + self.name + "? ")
            if op == "1" and not reset:
                i = 1
                targets = self.validAttackTargets()
                for v in targets:
                    print(i, v)
                    i += 1
                target = ""
                while target not in ["0"] + [str(x+1) for x in range(len(targets))]:
                    target = input("Quem será atacado? 0 - Cancelar. ")
                if target == "0":
                    reset = True #vamos pular todo o resto do menu e recomeçar
                else:
                    self.attack(targets[int(target)-1])
            if op == "2" and not reset:
                print("Habilidades")
                input()
                #reset = True
            if op == "3" and not reset:
                print("Inventário")
                input()
                #reset = True
            if op == "4" and not reset:
                self.applyEffect(EffectType.GUARD)
            if reset == True:
                self.act()
        else:
            target = random.choice(self.validAttackTargets())
            self.attack(target)


    def applyEffect(self, effectType, args=[]):
        newEffect = Effect.Effect(self, effectType, args)
        self.effects.append(newEffect)
        newEffect.apply()

    def __str__(self):
        return '{:>14}'.format(self.name) + \
        ": PV:" + showStat(self.pv) + ", PH:" + showStat(self.ph) + \
         ", AT:" + showStat(self.at) + ", DF:" + showStat(self.df) + \
         ", AG:" + showStat(self.ag) + ", PTR:" + str(self.progress) + "/1000"
