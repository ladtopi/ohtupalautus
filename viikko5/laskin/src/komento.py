class Komento:
    def __init__(self, logiikka, lue_operandi=None):
        self._logiikka = logiikka
        self._lue_operandi = lue_operandi

    def suorita(self):
        self._arvo_ennen = self._logiikka.arvo()
        self.operaatio()

    def kumoa(self):
        self._logiikka.aseta_arvo(self._arvo_ennen)

    def operaatio(self):
        raise NotImplementedError

class Summa(Komento):
    def operaatio(self):
        self._logiikka.plus(self._lue_operandi())

class Erotus(Komento):
    def operaatio(self):
        self._logiikka.miinus(self._lue_operandi())

class Nollaa(Komento):
    def operaatio(self):
        self._logiikka.nollaa()

class Kumoa(Komento):
    def operaatio(self):
        self._lue_operandi().kumoa()
