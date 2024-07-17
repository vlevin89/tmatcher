import csv
from datetime import datetime
from Matcher import Matcher
from Player import Player

if __name__ == "__main__":

    # use to filter out people who signed up before this date
    start_year = 2024
    start_month = 7
    start_day = 6

    players = []
    with open('TMATCHSurvey_v4.tsv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        first_row = next(reader)

        for row in reader:
            try:
                date = datetime.strptime(row[0], '%m/%d/%Y %H:%M:%S')
            except ValueError:
                continue
            name = row[1]
            level = row[3]
            days = row[6]
            email = row[8]
            player = Player(date, name, level, days, email)

            if date > datetime(start_year, start_month, start_day):
                players.append(player)
    player_names = set()
    unique_players = []
    for player in players:
        if player.name not in player_names:
            player_names.add(player.name)
            unique_players.append(player)

    matcher = Matcher(players)
    matcher.match()
    with open('matched.csv', 'w', newline='') as csvfile:
        for player1, player2 in matcher.matched_players:
            writer = csv.writer(csvfile)
            writer.writerow([player1.name, player1.level, '', player2.level, player2.name])
        for player in matcher.unmatched_players:
            writer.writerow([player.name, player.level])
