from datetime import datetime
import json

class MatchEvents:
    def __init__(self):
        self.data = []

    def add_event(self,type: str,player: str, sub: str,time: int):
        self.data.append({'type':type,'player':player,'sub':sub,'time':time})

    def add_events(self, events):
        self.data+=events.data

    def to_dict(self):
        return {"events": self.data}

class Match:
    def __init__(self,was_played: bool, hteam: str, ateam: str,dt: datetime,hgoals: int,agoals: int,hevents: MatchEvents,aevents: MatchEvents):
        self.was_played = was_played
        self.home_team = hteam
        self.away_team = ateam
        if dt:
            self.date = dt.date()
            self.time = dt.time()
        else:
            self.date = None
            self.time = None
        self.home_goals = hgoals
        self.away_goals = agoals
        self.home_events = hevents
        self.away_events = aevents

    def add_event(self, event: MatchEvents, is_home: bool):
        try:
            if is_home:
                self.home_events.add_events(event)
            else:
                self.away_events.add_events(event)
        except:
            pass

    def get_match(self):
        return self.home_team + ' ' + self.away_team

    def to_dict(self):
        return {
            "was_played": self.was_played,
            "home_team": self.home_team,
            "away_team": self.away_team,
            "date": self.date.isoformat() if self.date else None,
            "time": self.time.isoformat() if self.time else None,
            "home_goals": self.home_goals,
            "away_goals": self.away_goals,
            "home_events": self.home_events.to_dict(),
            "away_events": self.away_events.to_dict(),
        }


class Fixture:
    def __init__(self, rn: int):
        self.data = []
        self.round_number = rn

    def add_match(self, match: Match):
        self.data.append(match)

    def matches_count(self):
        return len(self.data)

    def get_all(self):
        return self.data

    def to_dict(self):
        return {
            "round_number": self.round_number,
            "matches": [match.to_dict() for match in self.data],
        }

class FixtureCollection:
    def __init__(self):
        self.data = []

    def add_fixture(self, fixture: Fixture):
        self.data.append(fixture)

    def rounds_count(self):
        return len(self.data)

    def get_all(self):
        return self.data

    def get_json(self):
        return json.dumps([fixture.to_dict() for fixture in self.data])