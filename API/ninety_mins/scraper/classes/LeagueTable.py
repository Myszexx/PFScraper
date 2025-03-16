from .LinksList import LinksList
from .Team import Team


class LeagueTable:
    def __init__(self):
        self.data = []

    def add(self, team: str, standing: int, points: int, wins: int, loses: int, draws: int, goals_shot: int, goals_conceded: int, url: str):
        self.data.append({
            'team': Team(team.strip(), url,LinksList()),
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
        data = self.data

        return data

    def get_team_at(self, index):
        return self.data[index-1]

    def show_team_at(self, index):
        team = self.data[index-1]
        return f'{team["standing"]}: {team["team"].team_name()}; {team["points"]} pts; wins: {team["wins"]}; loses: {team["loses"]}; draws: {team["draws"]}; goals conceded: {team["goals_conceded"]}; goals shot: {team["goals_shot"]}'

    def print(self):
        for i in range(len(self.data)):
            row = self.data[i]
            print(f'{row['standing']}: {row['team']}')

    def get_json(self):
        ret = []
        for item in self.data:
            itm = {}
            for key in item:
                if key != 'team':
                    itm[key] = item[key]
                else:
                    tmp = item[key].get_all()
                    itm['name'] = tmp['name']
                    itm['url'] = tmp['url']
            ret.append(itm)
        return ret

    def is_team_in_league(self, team_name):
        for team in self.data:
            if team_name.strip().__contains__(team['team'].team_name()):
                return True
        print(f'Team {team_name} not found in league')
        return False