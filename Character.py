def showStat(stat):
    return '{:02d}'.format(stat[0]) + "/" + '{:02d}'.format(stat[1])


class Character:
    def __init__(self, name, pv, ph, at, df, ag):
        self.name = name
        self.pv = (pv, pv)
        self.ph = (ph, ph)
        self.at = (at, at)
        self.df = (df, df)
        self.ag = (ag, ag)

    def __str__(self):
        return '{:>16}'.format(self.name) + \
        ": PV:" + showStat(self.pv) + ", PH:" + showStat(self.ph) + \
         ", AT:" + showStat(self.at) + ", DF:" + showStat(self.df) + \
         ", AG:" + showStat(self.ag)
