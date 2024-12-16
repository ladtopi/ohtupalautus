from kps import KPS

class KPSTekoaly(KPS):
    def __init__(self, tekoaly):
        self._tekoaly = tekoaly

    def _vastustajan_siirto(self):
        siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto

    def _siirron_jalkeen(self, pelaajan_siirto):
        self._tekoaly.aseta_siirto(pelaajan_siirto)
