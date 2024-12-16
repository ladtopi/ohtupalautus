from tuomari import Tuomari


class KPS():
    def pelaa(self):
        tuomari = Tuomari()

        peli_kaynnissa = True

        while peli_kaynnissa:
            pelaajan_siirto = self._pelaajan_siirto()
            vastustajan_siirto = self._vastustajan_siirto()
            if self._onko_ok_siirto(pelaajan_siirto) and self._onko_ok_siirto(vastustajan_siirto):
                tuomari.kirjaa_siirto(pelaajan_siirto, vastustajan_siirto)
                print(tuomari)
                self._siirron_jalkeen(pelaajan_siirto)
            else:
                peli_kaynnissa = False

        print("Kiitos!")
        print(tuomari)

    def _pelaajan_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _siirron_jalkeen(self, pelaajan_siirto):
        pass

    def _vastustajan_siirto(self):
        return input("Toisen pelaajan siirto: ")

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
