import grpc
from concurrent import futures
import scraper_pb2_grpc
import scraper_pb2
from scraper.ninety_minutes.parsers.TeamPage import get_team_data
from scraper.ninety_minutes.parsers.ZPNs import get_zpns_list, get_leagues_list, get_league_standings, get_fixtures
from bs4 import BeautifulSoup
import requests

class ScraperService(scraper_pb2_grpc.ScraperServiceServicer):
    def GetNinetyZPNs(self, request, context):
        response = scraper_pb2.ScraperResponse()
        url = request.url
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        zpns_list = get_zpns_list(soup)
        response.data = str(zpns_list)
        return response

    def GetNinetyLeagues(self, request, context):
        response = scraper_pb2.ScraperResponse()
        url = request.url
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        leagues_list = get_leagues_list(soup)
        response.data = str(leagues_list)
        return response

    def GetNinetyLeagueStandings(self, request, context):
        response = scraper_pb2.ScraperResponse()
        url = request.url
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        league_standings = get_league_standings(soup)
        response.data = str(league_standings)
        return response

    def GetNinetyFixtures(self, request, context):
        response = scraper_pb2.ScraperResponse()
        url = request.url
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        league_table = get_league_standings(soup)  # Assuming you need the league table for fixtures
        fixtures = get_fixtures(soup, league_table)
        response.data = str(fixtures)
        return response

    def GetNinetyTeams(self, request, context):
        response = scraper_pb2.ScraperResponse()
        url = request.url
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        team = get_team_data(soup, request.name, request.url)
        response.data = str(team)
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    scraper_pb2_grpc.add_ScraperServiceServicer_to_server(ScraperService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()