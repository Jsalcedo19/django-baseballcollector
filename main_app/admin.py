from django.contrib import admin

# Register your models here.
from .models import Baseball, Games, Player

# Register your models here
admin.site.register(Baseball)
admin.site.register(Games)
admin.site.register(Player)
