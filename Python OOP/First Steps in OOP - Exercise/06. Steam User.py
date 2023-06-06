class SteamUser:
    played_hours = 0

    def __init__(self, username, games):
        self.username = username
        self.games = games
    
    
    def play(self, game, hours):
        if game in self.games:
            self.played_hours += hours
            return f"{self.username} is playing {game}"
        return f"{game} is not in library"

    def buy_game(self, game):
        if game in self.games:
            return f"{game} is already in your library"
        self.games.append(game)
        return f"{self.username} bought {game}"
        
        
    def status(self):
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"
