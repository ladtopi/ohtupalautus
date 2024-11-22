class Komento:
    def __init__(self, logiikka, arvopino, lue_operandi=None):
        self._logiikka = logiikka
        self._lue_operandi = lue_operandi
        self._arvopino = arvopino

    def suorita(self):
        raise NotImplementedError

class Summa(Komento):
    def suorita(self):
        self._arvopino.append(self._logiikka.arvo())
        self._logiikka.plus(self._lue_operandi())

class Erotus(Komento):
    def suorita(self):
        self._arvopino.append(self._logiikka.arvo())
        self._logiikka.miinus(self._lue_operandi())

class Nollaa(Komento):
    def suorita(self):
        self._arvopino.append(self._logiikka.arvo())
        self._logiikka.nollaa()

class Kumoa(Komento):
    def suorita(self):
        self._logiikka.aseta_arvo(self._arvopino.pop())
