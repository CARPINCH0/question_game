import random
from django.shortcuts import render
from django.http import HttpResponse
from questions.models import Player, Question, Game_History, Game_Setup

game_name = "0"
def welcome(request):
        return render(request, "website/welcome.html",
        {"game_setup" : Game_Setup.objects.all})

def pick_game(request, id):
        game = Game_Setup.objects.get(pk=id)
        return render(request,website/game.html,{"game":game})

def new_game():
        global game_name = "4"
        Game_Setup.objects.create(Game_Name =game_name, Current_Turn = 0)
        game = Game_Setup.objects.values_list('id',flat=True)
        players = Player.objects.values_list('id',flat=True)
        question_list = Question.objects.values_list('id',flat=True)
        question_chosen = random.choice(question_list)
        for player in players:
                Game_History.objects.create(Game_Id=str(max(game)), Round = 0, Card_Id = question_chosen, Player_Id = player, Player_Vote = 0, Player_Score = 0 )

def new_turn()
        Game_History.objects.get()

"""
game_name = "2"
Game_Setup.objects.create(Game_Name =game_name, Current_Turn = 0)
game = Game_Setup.objects.values_list('id',flat=True)
players = Player.objects.values_list('id',flat=True)
question_list = Question.objects.values_list('id',flat=True)
question_chosen = random.choice(question_list)
for player in players:
        Game_History.objects.create(Game_Id=str(max(game)), Turn = 1, Card_Id = question_chosen, Player_Id = player, Player_Vote = 0, Player_Score = 1 )
"""