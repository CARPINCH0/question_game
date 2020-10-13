from django.db import models

class Player(models.Model):
    Name = models.CharField(max_length=200)
    def __str__ (self):
        return "Player Name: " + self.Name

class Question(models.Model):
    Question = models.CharField(max_length=200)
    Option1 = models.CharField(max_length=200)
    Option2 = models.CharField(max_length=200)
    Option3 = models.CharField(max_length=200)
    Option4 = models.CharField(max_length=200)

class Game_History(models.Model):
    Game_Id = models.CharField(max_length=200)
    Round = models.IntegerField()
    Card_Id = models.IntegerField()
    Player_Id = models.IntegerField()
    Player_Vote = models.IntegerField(default = 0)
    Player_Score = models.IntegerField(default = 0)
    def __str__(self):
        return "Game id: " + str(self.Game_Id), "Player id: " + str(self.Player_Id), "Card_Id" + str(self.Card_Id)

class Game_Setup(models.Model):
    Game_Name = models.CharField(max_length=200, unique = True)
    Current_Turn = models.IntegerField(default=0)
    def __str__(self):
        return self.Game_Name