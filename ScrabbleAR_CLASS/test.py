class s:
    atril_jugador = {1: 1}
    atril_bot = {2: 2}

    def ya_mismo(self):
        print(1)

    def ahora_mismo(self):
        print(2)

    def mismo(self, cual):
        getattr(self, cual+'_mismo')()

    def var(self, quien):
        print(getattr(self, 'atril_'+quien))


a = s()
a.var('jugador')
