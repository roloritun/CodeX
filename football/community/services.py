from django.conf import settings
import json
import requests
from .serializers import CompetitionSerializer, GameSerializer

url = settings.FOOTBALL_DATA_URL


class FootballData:
    @staticmethod
    def get_competitions():
        endpoint = url + '/v2/competitions'
        headers = {'X-Auth-Token': settings.FOOTBALL_KEY, 'X-Response-Control': 'minified'}
        response = requests.get(endpoint, headers=headers)
        payload = None
        if response.status_code == 200:
            payload = json.loads(response.content.decode('utf-8'))
            # print(payload)
            for des in payload:
                # print(des)
                serializer = CompetitionSerializer(data=des)
                if serializer.is_valid():
                    serializer.save()
        return

    @staticmethod
    def get_games(comp):
        endpoint = url + '/v2/competitions/' + comp + '/fixtures'
        print(endpoint)
        headers = {'X-Auth-Token': settings.FOOTBALL_KEY, 'X-Response-Control': 'minified'}
        response = requests.get(endpoint, headers=headers)
        payload = None
        if response.status_code == 200:
            payload = json.loads(response.content.decode('utf-8'))
            # print(payload)
            for des in payload['fixtures']:
                # print(des['result'])
                for d, v in des.items():
                    print(d, v)

                serializer = GameSerializer(data=des)
                if serializer.is_valid():
                    serializer.save()
        return
