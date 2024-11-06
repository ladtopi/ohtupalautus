import requests
from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    nationality = "FIN"
    print("Players from", nationality)

    for player in sorted(
            filter(lambda p: p.nationality == nationality, players),
            key=lambda p: p.goals + p.assists, reverse=True):
        print(player)


if __name__ == "__main__":
    main()
