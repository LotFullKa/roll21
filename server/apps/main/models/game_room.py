from typing import List

from django.db import models

from main.models.subject import Subject


class GameRoom(models.Model):
    """Game Room model."""

    name = models.CharField(max_length=60, unique=True)
    players = models.ManyToManyField("main.Subject")
    turn_number = models.IntegerField(default=0)
    now_player = models.ForeignKey(
        "main.Subject",
        on_delete=models.SET_NULL,
        related_name='now_player',
        null=True,
    )

    def next_turn(self):
        self.turn_number += 1
        players_list: List[Subject] = list(self.players.all())
        index = players_list.index(self.now_player)
        next_index = (index + 1) % len(players_list)

        self.now_player = players_list[next_index]

        self.save()

    def __str__(self):
        return self.name
