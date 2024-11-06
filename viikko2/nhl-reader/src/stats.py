class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        return list(
            sorted(
                filter(lambda p: p.nationality == nationality, players),
                key=lambda p: p.goals + p.assists, reverse=True))
