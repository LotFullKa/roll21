from random import randint

from django.conf import settings
from django.db import models

from main.constants import ColorEnum, SubjectTypeEnum
from main.exceptions import DistanceError
from main.weapon import Weapons
from utils.enum_helpers import random_enum_key, enum_to_choices


def default_color():
    return random_enum_key(ColorEnum)


class Subject(models.Model):
    """Subject model."""

    name = models.CharField(max_length=60, unique=True)
    x_pos = models.SmallIntegerField(blank=True)
    y_pos = models.SmallIntegerField(blank=True)
    hp = models.SmallIntegerField(default=100)
    is_dead = models.BooleanField(default=False)
    move_speed = models.SmallIntegerField(default=5)

    weapon = models.CharField(max_length=255, choices=enum_to_choices(Weapons), default="short sword")

    type_of_subject = models.CharField(
        max_length=50,
        choices=enum_to_choices(SubjectTypeEnum),
        default=SubjectTypeEnum.HUMAN,
    )
    color = models.CharField(
        choices=enum_to_choices(ColorEnum), max_length=50, default=default_color
    )
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )

    def distance(self, subject: "Subject") -> int:
        return (subject.x_pos - self.x_pos)**2 + (subject.y_pos - self.y_pos)**2

    def move(self, new_x: int, new_y: int) -> None:
        if (self.x_pos - new_x)**2 + (self.x_pos - new_y)**2 < self.move_speed:
            self.x_pos = new_x
            self.y_pos = new_y
            self.save()
        else:
            raise DistanceError()

    def take_damage(self, damage: int) -> None:
        if self.hp - damage <= 0:
            self.hp = 0
            self.is_dead = True
            self.save()
        else:
            self.hp = self.hp - damage
            self.save()

    def attack(self, subject: "Subject") -> None:
        weapon = Weapons.get_by_name(self.weapon)
        if self.distance(subject) < weapon.distance:
            subject.take_damage(weapon.damage)
        else:
            raise DistanceError()
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
