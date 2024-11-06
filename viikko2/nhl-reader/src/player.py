class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']

    # property getter for points
    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:24} {self.team:5} {self.goals:2d} + {self.assists:2d} = {self.points:3d}"
