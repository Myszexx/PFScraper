import requests
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.views import APIView

# import .API.core.scraper.ninety_minutes.parsers.ZPNs as zpn
# import .API.core.scraper.utils.utils as utils
from .scraper.ninety_minutes.parsers.ZPNs import get_zpns_list, get_leagues_list, get_league_standings
from .scraper.utils.utils import get_html_from_ninety
import json


# Create your views here.

class Status(APIView):
    permission_class = [AllowAny]
    def get(self,request,*args,**kwargs):
        r = requests.get('http://www.90minut.pl')
        return Response(status=r.status_code)

class ZPNsV(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        soap = get_html_from_ninety('/ligireg.html')
        data = {"data": get_zpns_list(soap).get_all()}
        return Response(data,HTTP_200_OK)


class LeaguesV(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        is_success = True
        data = {}
        try:
            soap = get_html_from_ninety(self.request.query_params.get("url", "/ligireg-11.html"))
            data = {"data": get_leagues_list(soap).get_all()}
        except:
            is_success = False
        if is_success:
            return Response(data,HTTP_200_OK)
        else:
            return Response({"error": "Couldn't scrape this url"},HTTP_404_NOT_FOUND)

class TableV(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        is_success = True
        data = {}
        try:
            soap = get_html_from_ninety(self.request.query_params.get("url", "/liga/1/liga13901.html"))
            data = {"data": get_league_standings(soap).get_json()}
        except:
            is_success = False
        if is_success:
            return Response(data,HTTP_200_OK)
        else:
            return Response({"error": "Couldn't scrape this url"},HTTP_404_NOT_FOUND)