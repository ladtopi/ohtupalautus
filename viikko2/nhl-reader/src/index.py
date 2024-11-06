from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from reader import PlayerReader
from stats import PlayerStats


SEASONS = [
    "2020-21",
    "2021-22",
    "2022-23",
    "2023-24",
    "2024-25",
]

def main():
    console = Console()
    prompt = Prompt()
    console.print("NHL statistics by nationality", style="bold cyan")

    season = prompt.ask("Select season", choices=SEASONS, default=SEASONS[-1])

    while True:
        nationality = prompt.ask("Select nationality", default="FIN")

        reader = PlayerReader(
            f"https://studies.cs.helsinki.fi/nhlstats/{season}/players")
        players = reader.get_players()
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(nationality)

        table = Table(title=f"Top scorers of {nationality} season {season}")
        table.add_column("Player", style="cyan")
        table.add_column("Team", style="yellow")
        table.add_column("Goals", style="green")
        table.add_column("Assists", style="green")
        table.add_column("Points", style="magenta")

        for player in players:
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(player.points),
            )

        console.print(table)


if __name__ == "__main__":
    main()
