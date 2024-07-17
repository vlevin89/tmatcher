from Player import Player
from collections import defaultdict

class Matcher:

    def __init__(self, players: [Player]):
        self.all_players = players
        self.players_by_level = defaultdict(list)
        self.players_by_days = defaultdict(list)
        self.matched_players = []
        self.unmatched_players = []

    def match(self):
        for player in self.all_players:
            self.players_by_level[float(player.level)].append(player)

        for level in [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]:
            players_at_level = self.players_by_level[level]
            players_at_level += self.unmatched_players
            self.unmatched_players = []
            while len(players_at_level) > 1:
                player1 = players_at_level.pop()
                player2 = players_at_level.pop()
                self.matched_players.append((player1, player2))
            if players_at_level:
                self.unmatched_players.append(players_at_level[0])





