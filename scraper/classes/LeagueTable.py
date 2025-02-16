import json

from scraper.classes.LinksList import LinksList
from scraper.classes.Team import Team


class LeagueTable:
    def __init__(self):
        self.data = []

    def add(self, team: str, standing: int, points: int, wins: int, loses: int, draws: int, goals_shot: int, goals_conceded: int, url: str):
        self.data.append({
            'team': Team(team, url,LinksList()),
            'standing': int(standing),
            'matches': wins + loses + draws,
            'points': int(points),
            'wins': int(wins),
            'loses': int(loses),
            'draws': int(draws),
            'goals_conceded': int(goals_conceded),
            'goals_shot': int(goals_shot),
            'url': url
        })
        self.data.sort(key=lambda x: x['standing'])

    def get_all(self):
        return self.data

    def get_team_at(self, index):
        return self.data[index-1]

    def show_team_at(self, index):
        team = self.data[index-1]
        return f'{team["standing"]}: {team["team"].team_name()}; {team["points"]} pts; wins: {team["wins"]}; loses: {team["loses"]}; draws: {team["draws"]}; goals conceded: {team["goals_conceded"]}; goals shot: {team["goals_shot"]}'

    def print(self):
        for i in range(len(self.data)):
            print(f'{self.data[i]['standing']}: {self.data[i]['team']}')

    def get_json(self):
        return json.dumps(self.data)

    def is_team_in_league(self, team_name):
        for team in self.data:
            if team['team'] == team_name.strip():
                return True
        print(f'Team {team_name} not found in league')
        return False