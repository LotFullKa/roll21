from django.db import models
from django.conf import settings
from random import randint


class Subject(models.Model):

    name = models.CharField(max_length=60)
    x_pos = models.SmallIntegerField()
    y_pos = models.SmallIntegerField()
    hp = models.SmallIntegerField(default=100)
    is_dead = models.BooleanField(default=False)
    type_of_subject = models.CharField(max_length=50)

    COLOR_RED = "red"
    COLOR_BLUE = "blue"
    COLOR_GREEN = "green"

    colors = (
        (COLOR_RED, "красный"),
        (COLOR_BLUE, "голубой"),
        (COLOR_GREEN, "зеленый"),
    )

    color_choices = models.CharField(choices=colors, max_length=50)

    def move(self, new_x, new_y):
        self.x_pos = new_x
        self.y_pos = new_y
        self.save()

    def save(self, **kwargs):
        if self._state.adding:
            self.x_pos, self.y_pos = self.generate_pos()
        super().save(**kwargs)

    @staticmethod
    def generate_pos():
        # TODO: @Kamil control recursion depth
        x = randint(0, settings.FIELD_SIZE)
        y = randint(0, settings.FIELD_SIZE)

        if not Subject.objects.exists(x_pos=x, y_pos=y):
            return x, y
        else:
            return Subject.generate_pos()
