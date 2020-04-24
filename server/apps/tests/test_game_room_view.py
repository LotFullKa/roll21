import json

from django.test import TestCase
from django.urls import reverse
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.test import APIClient, APISimpleTestCase, APITestCase


class GameRoomViewTestCase(APITestCase):
    def test_get(self):
        response = self.client.get(reverse("api:game-room"))
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "id": 1,
                "name": "Roll 21",
                "turn_number": 0,
                "now_player": None,
                "players": [],
            },
        )
