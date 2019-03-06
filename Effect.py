from EffectType import *
class Effect():
    def __init__(self, parent, type, args=[]):
        self.type = type
        self.parent = parent
        self.args = args
        self.expiry = -1
        self.inactive = False

    def apply(self):
        if self.type == EffectType.GUARD:
            print(self.parent.name + " está se defendendo contra ataques.")
            self.expiry = 1
            input()

    def handleTurn(self):
        self.expiry -= 1 #diminuir em 1 rodada a validade do efeito
        #if self.type == EffectType.GUARD:
        if self.expiry == 0:
            self.inactive = True

    def handleAttacked(self):
        if self.type == EffectType.GUARD:
            #TODO
            pass
