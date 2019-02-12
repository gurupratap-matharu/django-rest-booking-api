from django.urls import include, path
from api.models import Match, Market, Selection, Sport
from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient, URLPatternsTestCase

class MatchTests(APITestCase):

    def test_create_match(self):
        """
        Ensure we can create a new match object.
        """
        url = ('http://127.0.0.1:8000/api/match/')
        data = {
                 "id": 8661032861909884224,
                 "message_type": "NewEvent",
                 "event": {
                     "id": 994839351740,
                     "name": "Real Madrid vs Barcelona",
                     "startTime": "2018-06-20 10:30:00",
                     "sport": {
                         "id": 221,
                         "name": "Football"
                     },
                     "markets": [
                         {
                         "id": 385086549360973392,
                         "name": "Winner",
                         "selections": [
                             {
                             "id": 8243901714083343527,
                             "name": "Real Madrid",
                             "odds": 1.01
                             },
                             {
                             "id": 5737666888266680774,
                             "name": "Barcelona",
                             "odds": 1.01
                             }
                            ]
                        }
                     ]
                    }
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Match.objects.count(), 1)
        self.assertEqual(Match.objects.get().name, 'Real Madrid vs Barcelona')

    def test_update_odds(self):
        """
        Ensure we can update odds on a created match object.
        """
        url = ('http://127.0.0.1:8000/api/match/')

        # first we create a match
        create_match = {
                 "id": 8661032861909884224,
                 "message_type": "NewEvent",
                 "event": {
                     "id": 994839351740,
                     "name": "Real Madrid vs Barcelona",
                     "startTime": "2018-06-20 10:30:00",
                     "sport": {
                         "id": 221,
                         "name": "Football"
                     },
                     "markets": [
                         {
                         "id": 385086549360973392,
                         "name": "Winner",
                         "selections": [
                             {
                             "id": 8243901714083343527,
                             "name": "Real Madrid",
                             "odds": 1.01
                             },
                             {
                             "id": 5737666888266680774,
                             "name": "Barcelona",
                             "odds": 1.01
                             }
                            ]
                        }
                     ]
                    }
                }
        response = self.client.post(url, create_match, format='json')

        # now we update the odds on the same match
        update_odds = {
                 "id": 8661032861909884224,
                 "message_type": "UpdateOdds",
                 "event": {
                     "id": 994839351740,
                     "name": "Real Madrid vs Barcelona",
                     "startTime": "2018-06-20 10:30:00",
                     "sport": {
                         "id": 221,
                         "name": "Football"
                     },
                     "markets": [
                         {
                         "id": 385086549360973392,
                         "name": "Winner",
                         "selections": [
                             {
                             "id": 8243901714083343527,
                             "name": "Real Madrid",
                             "odds": 0.5
                             },
                             {
                             "id": 5737666888266680774,
                             "name": "Barcelona",
                             "odds": 1.5
                             }
                            ]
                        }
                     ]
                    }
                }
        response = self.client.post(url, update_odds, format='json')
        self.assertEqual([1.5, 0.5], [s.odds for s in Selection.objects.all()])
        self.assertEqual(Match.objects.get().name, 'Real Madrid vs Barcelona')
