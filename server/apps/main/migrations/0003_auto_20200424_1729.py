# Generated by Django 3.0.5 on 2020-04-24 17:29

from django.db import migrations, models
import main.constants
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200405_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='color',
            field=models.CharField(choices=[(main.constants.ColorEnum['RED'], 'red'), (main.constants.ColorEnum['BLUE'], 'blue'), (main.constants.ColorEnum['GREEN'], 'green')], default=main.models.default_color, max_length=50),
        ),
        migrations.AlterField(
            model_name='subject',
            name='type_of_subject',
            field=models.CharField(choices=[(main.constants.SubjectTypeEnum['HUMAN'], 'human'), (main.constants.SubjectTypeEnum['GOBLIN'], 'goblin')], default=main.constants.SubjectTypeEnum['HUMAN'], max_length=50),
        ),
    ]