import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

MAITO = 1
LEIPA = 2
KULTAHARKKO = 3

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == MAITO:
                return 10
            if tuote_id == KULTAHARKKO:
                return 10
            return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(MAITO, "maito", 5)
            if tuote_id == 2:
                return Tuote(LEIPA, "leipä", 3)
            if tuote_id == 3:
                return Tuote(KULTAHARKKO, "kultaharkko", 1000)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(MAITO)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_asiakkaan_ja_maksun_tiedoilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(MAITO)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_kahden_eri_varastosta_loytyvan_tuotteen_loppusumma_on_yhteishinta(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(MAITO)
        self.kauppa.lisaa_koriin(KULTAHARKKO)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 1005)

    def test_kahden_saman_varastosta_loytyvan_tuotteen_loppusumma_on_yhteishinta(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(MAITO)
        self.kauppa.lisaa_koriin(MAITO)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)

    def test_tuotteet_joita_ei_ole_varastossa_eivat_vaikuta_loppusummaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(MAITO)
        self.kauppa.lisaa_koriin(LEIPA)
        self.kauppa.lisaa_koriin(LEIPA)
        self.kauppa.lisaa_koriin(LEIPA)
        self.kauppa.lisaa_koriin(LEIPA)
        self.kauppa.tilimaksu("pekka", "12345")
    
        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_asioinnin_aloittaminen_nollaa_ostokset(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(MAITO)
        self.kauppa.lisaa_koriin(MAITO)
        self.kauppa.aloita_asiointi()
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että veloitus on 0
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, ANY, ANY, 0)

    def test_joka_tilisiirrolle_luodaan_oma_viite(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.tilimaksu("pekka", "12345")
        self.kauppa.tilimaksu("pekka", "12345")
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että uusi viite on generoitu kolmesti
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 3)
