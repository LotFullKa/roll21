from django.db import models
from django.conf import settings
from random import randint, choice
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager
from django.utils.translation import ugettext_lazy as _


def default_color():
    return choice(Subject.COLORS_CHOICES)[0]


class User(AbstractBaseUser):
    username = models.CharField(max_length=60)

    object = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _("users")


class Subject(models.Model):
    COLOR_RED = "red"
    COLOR_BLUE = "blue"
    COLOR_GREEN = "green"

    COLORS_CHOICES = (
        (COLOR_RED, "красный"),
        (COLOR_BLUE, "голубой"),
        (COLOR_GREEN, "зеленый"),
    )

    SUBJECT_TYPE_HUMAN = "human"
    SUBJECT_TYPE_GOBLIN = "goblin"

    SUBJECT_TYPE_CHOICES = (
        (SUBJECT_TYPE_HUMAN, "Человек"),
        (SUBJECT_TYPE_GOBLIN, "гоблин"),
    )

    name = models.CharField(max_length=60, unique=True)
    x_pos = models.SmallIntegerField(blank=True)
    y_pos = models.SmallIntegerField(blank=True)
    hp = models.SmallIntegerField(default=100)
    is_dead = models.BooleanField(default=False)
    type_of_subject = models.CharField(max_length=50, choices=SUBJECT_TYPE_CHOICES, default=SUBJECT_TYPE_HUMAN)
    color = models.CharField(choices=COLORS_CHOICES, max_length=50, default=default_color)
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


class Game_room(models.Model):
    name = models.CharField(max_length=60,  unique=True)
    players = models.ManyToManyField(User)
    turn_number = models.IntegerField()
    now_player = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='now_player',
        null=True,
    )

    def next_turn(self):
        self.turn_number = (self.turn_number + 1) % len(self.players)
        self.save()
