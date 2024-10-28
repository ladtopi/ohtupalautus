import unittest

from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = StatisticsService(PlayerReaderStub())

    def test_search_existing(self):
        self.assertEqual(self.statistics.search("Semenko").name, "Semenko")

    def test_search_nonexisting(self):
        self.assertEqual(self.statistics.search("awkefoija"), None)

    def test_team(self):
        self.assertEqual([p.name for p in self.statistics.team("EDM")], ["Semenko", "Kurri", "Gretzky"])

    def test_top(self):
        self.assertEqual([p.name for p in self.statistics.top(2)], ["Gretzky", "Lemieux"])
