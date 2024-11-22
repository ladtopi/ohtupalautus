MAP_SCORE = dict(zip(range(5), ["Love", "Fifteen", "Thirty", "Forty", "Game"]))

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player_1_name = player1_name
        self.player_2_name = player2_name
        self.player_1_points = 0
        self.player_2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player_1_points = self.player_1_points + 1
        else:
            self.player_2_points = self.player_2_points + 1

    def get_score(self):
        if self._even():
            return self._even_score()
        if self._win():
            return self._win_score()
        if self._advantage():
            return self._advantage_score()
        return self._normal_score()
    
    def _even(self):
        return self.player_1_points == self.player_2_points

    def _even_score(self):
        if self.player_1_points >= 3:
            return "Deuce"
        return f"{MAP_SCORE[self.player_1_points]}-All"

    def _advantage(self):
        return self.player_1_points >= 4 or self.player_2_points >= 4
    
    def _player_ahead(self):
        if self.player_1_points > self.player_2_points:
            return self.player_1_name
        return self.player_2_name

    def _advantage_score(self):
        return f"Advantage {self._player_ahead()}"

    def _win(self):
        max_pts = max(self.player_1_points, self.player_2_points)
        diff = abs(self.player_1_points - self.player_2_points)
        return max_pts >= 4 and diff >= 2

    def _win_score(self):
        return f"Win for {self._player_ahead()}"
    
    def _normal_score(self):
        return f"{MAP_SCORE[self.player_1_points]}-{MAP_SCORE[self.player_2_points]}"

