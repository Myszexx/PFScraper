from scraper.classes.LinksList import LinksList


class Team:
    def __init__(self, name: str, url:str, seasons:LinksList):
        self.name = name
        self.url = url
        self.seasons = seasons

    def get_all(self):
        return {'name': self.name, 'url': self.url, 'seasons': self.seasons.get_all()}

    def append_season(self, season):
        self.seasons.add(season['name'], season['url'])

    def print(self):
        print(f'{self.name}({self.url})')
        print('Sezony:')
        self.seasons.print()

    def team_name(self):
        return self.name