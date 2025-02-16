from scraper.classes.LinksList import LinksList


class Team:
    def __init__(self, name: str, URL:str, seasons:LinksList):
        self.name = name
        self.URL = URL
        self.seasons = seasons

    def get_all(self):
        return {'name': self.name, 'URL': self.URL, 'seasons': self.seasons.get_all()}

    def append_season(self, season):
        self.seasons.add(season['to'], season['link'])

    def print(self):
        print(f'{self.name}({self.URL})')
        print('Sezony:')
        self.seasons.print()

    def team_name(self):
        return self.name