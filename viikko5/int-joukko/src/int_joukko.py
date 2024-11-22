OLETUSKAPASITEETTI = 5
OLETUSKASVATUS = 5


def assert_natural_number(n, msg):
    assert isinstance(n, int), msg
    assert n >= 0, msg

class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=OLETUSKAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        assert_natural_number(kapasiteetti, f"Virheellinen kapasiteetti: {kapasiteetti}")
        assert_natural_number(kasvatuskoko, f"Virheellinen kasvatuskoko: {kasvatuskoko}")
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.muisti = self._luo_lista(self.kapasiteetti)
        self.koko = 0

    def kuuluu(self, n):
        for i in range(self.koko):
            if n == self.muisti[i]:
                return True
        return False

    def lisaa(self, n):
        if self.kuuluu(n):
            return False
        if self._taynna():
            self._laajenna()
        self.muisti[self.koko] = n
        self.koko += 1
        return True

    def poista(self, n):
        if not self.kuuluu(n):
            return False
        self.koko -= 1
        for i in range(self.muisti.index(n), self.koko):
            self.muisti[i] = self.muisti[i+1]
        return True
    
    def mahtavuus(self):
        return self.koko

    def lista(self):
        return list(self)
    
    def _taynna(self):
        return self.koko == self.kapasiteetti
    
    def _laajenna(self):
        vanha_muisti = self.muisti
        self.kapasiteetti += self.kasvatuskoko
        self.muisti = self._luo_lista(self.kapasiteetti)
        self._kopioi_lista(vanha_muisti, self.muisti, self.koko)

    def _kopioi_lista(self, a, b, n):
        for i in range(n):
            b[i] = a[i]
    
    def __iter__(self):
        self._iter_index = 0
        return self
    
    def __next__(self):
        if self._iter_index == self.koko:
            raise StopIteration
        self._iter_index += 1
        return self.muisti[self._iter_index - 1]
    
    def __str__(self):
        return "{" + ", ".join(str(x) for x in self) + "}"

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()
        for x in a:
            tulos.lisaa(x)
        for x in b:
            tulos.lisaa(x)
        return tulos

    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()
        yhdiste = IntJoukko.yhdiste(a, b)
        for x in yhdiste:
            if a.kuuluu(x) and b.kuuluu(x):
                tulos.lisaa(x)
        return tulos

    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()
        for x in a:
            if not b.kuuluu(x):
                tulos.lisaa(x)
        return tulos
