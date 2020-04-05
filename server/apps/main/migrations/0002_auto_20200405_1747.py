# Generated by Django 3.0.5 on 2020-04-05 17:47

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='color_choices',
        ),
        migrations.AddField(
            model_name='subject',
            name='color',
            field=models.CharField(choices=[('red', 'красный'), ('blue', 'голубой'), ('green', 'зеленый')], default=main.models.default_color, max_length=50),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='type_of_subject',
            field=models.CharField(choices=[('human', 'Человек'), ('goblin', 'гоблин')], default='human', max_length=50),
        ),
        migrations.AlterField(
            model_name='subject',
            name='x_pos',
            field=models.SmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='y_pos',
            field=models.SmallIntegerField(blank=True),
        ),
    ]
