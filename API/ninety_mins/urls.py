from django.urls import path
from .views import ZPNsV, LeaguesV, TableV, Status

urlpatterns = [
    path('',Status.as_view(),name='Status'),
    path('scrape/zpns/',ZPNsV.as_view(),name='ZPNs'),
    path('scrape/leagues/',LeaguesV.as_view(),name='Leagues'),
    path('scrape/tables/',TableV.as_view(),name='Table'),
]