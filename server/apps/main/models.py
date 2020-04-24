from django.db import models
from django.conf import settings
from random import randint

from main.constants import SubjectTypeEnum, ColorEnum
from utils.enum_helpers import enum_to_choices, random_enum_key


def default_color():
    return random_enum_key(ColorEnum)


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
