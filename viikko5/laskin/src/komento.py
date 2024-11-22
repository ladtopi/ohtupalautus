class Komento:
    def __init__(self, logiikka, lue_operandi=None):
        self._logiikka = logiikka
        self._lue = lue_operandi

class Summa(Komento):
    def suorita(self):
        self._logiikka.plus(self._lue())

class Erotus(Komento):
    def suorita(self):
        self._logiikka.miinus(self._lue())

class Nollaa(Komento):
    def suorita(self):
        self._logiikka.nollaa()

class Kumoa(Komento):
    def suorita(self):
        pass
