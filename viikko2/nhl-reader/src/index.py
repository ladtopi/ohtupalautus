from reader import PlayerReader
from stats import PlayerStats


def main():
    reader = PlayerReader(
        "https://studies.cs.helsinki.fi/nhlstats/2023-24/players")
    players = reader.get_players()
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
