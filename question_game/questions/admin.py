from django.contrib import admin
from .models import Player, Question, Game_Setup, Game_History

admin.site.register(Player)
admin.site.register(Question)
admin.site.register(Game_Setup)
admin.site.register(Game_History)