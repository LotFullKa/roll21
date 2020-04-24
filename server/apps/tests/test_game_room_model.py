from django.test import TestCase

from main.factories import GameRoomFactory, UserFactory
from main.models import GameRoom


class GameRoomCase(TestCase):

    def test_game_room_str(self):
        game_room: GameRoom = GameRoomFactory()
        self.assertEqual(str(game_room), game_room.name)

    def test_next_turn(self):
        user1 = UserFactory()
        user2 = UserFactory()
        game_room: GameRoom = GameRoomFactory.create(players=(user1, user2), now_player=user1)
        self.assertEqual(game_room.now_player, user1)
        game_room.next_turn()

        game_room = GameRoom.objects.get(id=game_room.id)

        self.assertEqual(game_room.now_player, user2)
