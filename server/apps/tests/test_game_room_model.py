from django.test import TestCase

from main.factories import GameRoomFactory, SubjectFactory
from main.models import GameRoom


class GameRoomCase(TestCase):

    def test_game_room_str(self):
        game_room: GameRoom = GameRoomFactory()
        self.assertEqual(str(game_room), game_room.name)

    def test_next_turn(self):
        subject1 = SubjectFactory()
        subject2 = SubjectFactory()
        game_room: GameRoom = GameRoomFactory.create(players=(subject1, subject2), now_player=subject1)
        self.assertEqual(game_room.now_player, subject1)
        game_room.next_turn()

        game_room = GameRoom.objects.get(id=game_room.id)

        self.assertEqual(game_room.now_player, subject2)
