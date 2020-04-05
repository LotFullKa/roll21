# Generated by Django 3.0.5 on 2020-04-03 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('x_pos', models.SmallIntegerField()),
                ('y_pos', models.SmallIntegerField()),
                ('hp', models.SmallIntegerField(default=100)),
                ('is_dead', models.BooleanField(default=False)),
                ('type_of_subject', models.CharField(max_length=50)),
                ('color_choices', models.CharField(choices=[('red', 'красный'), ('blue', 'голубой'), ('green', 'зеленый')], max_length=50)),
            ],
        ),
    ]