import grpc
from concurrent import futures
import scraper_pb2
import scraper_pb2_grpc
from bs4 import BeautifulSoup
import requests
import time
import scraper.utils.utils as su #ScrapperUtils
from scraper.classes.LeagueTable import LeagueTable
from scraper.ninety_minutes.parsers import ZPNs

# Cache dictionary to store the scraped data
cache = {}
cache_duration = 60*60*12  # Cache duration in seconds (e.g., 5 minutes)


class ScraperService(scraper_pb2_grpc.ScraperServiceServicer):
    def get_cached_data(self, url):
        current_time = time.time()
        if url in cache and current_time - cache[url]['timestamp'] < cache_duration:
            return cache[url]['data']
        return None

    def set_cache_data(self, url, data):
        cache[url] = {
            'data': data,
            'timestamp': time.time()
        }

    def GetLeagueStandings(self, request, context):
        url = request.url
        cached_data = self.get_cached_data(url)
        if cached_data:
            return scraper_pb2.ScraperResponse(data=cached_data)

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        standings = ZPNs.get_league_standings(soup,)
        data = standings.to_dict()
        self.set_cache_data(url, data)
        return scraper_pb2.ScraperResponse(data=data)

    def GetFixtures(self, request, context):
        url = request.url
        cached_data = self.get_cached_data(url)
        if cached_data:
            return scraper_pb2.ScraperResponse(data=cached_data)

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        league = ZPNs.get_league_standings(soup)
        fixtures = ZPNs.get_fixtures(soup, league)
        data = fixtures.get_json()
        self.set_cache_data(url, data)
        return scraper_pb2.ScraperResponse(data=data)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    scraper_pb2_grpc.add_ScraperServiceServicer_to_server(ScraperService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()