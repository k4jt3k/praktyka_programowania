#zmiany w pliku:
#-usuniecie zakodowanych nazw użytkowników 
#-zastąpienie pętli wyświetlającej napis 
#-dodano słownik mapujący wynik
#-podzielono na dwie metody (remisu i zakończenia gry)
#-użyto wartości bezwzględnej zamiast odczytywac wartosci -1 i 1 osobno 

class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_points = 0  
        self.p2_points = 0
        self.score_names = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1_points += 1
        else:
            self.p2_points += 1

    def score(self):
        if self.p1_points == self.p2_points:
            return self._get_equal_score()
        
        if self.p1_points >= 4 or self.p2_points >= 4:
            return self._get_end_game_score()
        
        return f"{self.score_names[self.p1_points]}-{self.score_names[self.p2_points]}"
    
    def _get_equal_score(self): 
        equal_score = {0: "Love-All", 1: "Fifteen-All", 2: "Thirty-All"}
        return equal_score.get(self.p1_points, "Deuce")

    def _get_end_game_score(self): 
        points_diff = self.p1_points - self.p2_points 
        lead_player = self.player1_name if points_diff > 0 else self.player2_name

        if abs(points_diff) == 1:
            return "Advantage " + lead_player
        return "Win for " + lead_player