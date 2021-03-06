# Generated by Django 3.1 on 2020-09-08 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_game_setup_current_turn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game_history',
            old_name='Turn',
            new_name='Round',
        ),
        migrations.AlterField(
            model_name='game_history',
            name='Player_Score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='game_history',
            name='Player_Vote',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='game_setup',
            name='Current_Turn',
            field=models.IntegerField(default=0),
        ),
    ]
