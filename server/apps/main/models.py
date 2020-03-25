from django.db import models


class Subject(models.Model):

    name = models.CharField(max_length=60)
    x_pos = models.SmallIntegerField()
    y_pos = models.SmallIntegerField()
    hp = models.SmallIntegerField(default=100)
    is_dead = models.BooleanField(default=False)
    type_of_subject = models.CharField()

    COLOR_RED = "red"
    COLOR_BLUE = "blue"
    COLOR_GREEN = "green"

    colors = (
        (COLOR_RED, "красный"),
        (COLOR_BLUE, "голубой"),
        (COLOR_GREEN, "зеленый"),
    )

    color_choices = models.CharField(choices=colors)

    def move(self, new_x, new_y):
        self.x_pos = new_x
        self.y_pos = new_y
        self.save()
