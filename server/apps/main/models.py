from typing import List

from django.db import models
from django.conf import settings
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager
from django.utils.translation import ugettext_lazy as _
from random import randint

from main.constants import SubjectTypeEnum, ColorEnum
from utils.enum_helpers import enum_to_choices, random_enum_key


def default_color():
    return random_enum_key(ColorEnum)


class User(AbstractBaseUser):
    username = models.CharField(max_length=60)

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _("users")


class Subject(models.Model):
    name = models.CharField(max_length=60, unique=True)
    x_pos = models.SmallIntegerField(blank=True)
    y_pos = models.SmallIntegerField(blank=True)
    hp = models.SmallIntegerField(default=100)
    is_dead = models.BooleanField(default=False)
    type_of_subject = models.CharField(
        max_length=50,
        choices=enum_to_choices(SubjectTypeEnum),
        default=SubjectTypeEnum.HUMAN,
    )
    color = models.CharField(
        choices=enum_to_choices(ColorEnum), max_length=50, default=default_color
    )
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        null=True,
    )

    def move(self, new_x, new_y):
        self.x_pos = new_x
        self.y_pos = new_y
        self.save()

    def save(self, **kwargs):
        if self._state.adding:
            if not (self.x_pos and self.y_pos):
                self.x_pos, self.y_pos = self.generate_pos()
        super().save(**kwargs)

    def generate_pos(self):
        # TODO: @ProKam control recursion depth
        x = randint(0, settings.FIELD_SIZE)
        y = randint(0, settings.FIELD_SIZE)

        if not Subject.objects.filter(x_pos=x, y_pos=y).exists():
            return x, y
        else:
            return self.generate_pos()

    def __str__(self):
        return self.name


class GameRoom(models.Model):
    name = models.CharField(max_length=60,  unique=True)
    players = models.ManyToManyField(User)
    turn_number = models.IntegerField(default=0)
    now_player = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='now_player',
        null=True,
    )

    def next_turn(self):
        self.turn_number += 1
        players_list: List[User] = list(self.players.all())
        index = players_list.index(self.now_player)
        next_index = (index + 1) % len(players_list)

        self.now_player = players_list[next_index]

        self.save()

    def __str__(self):
        return self.name
