from django.urls import path
from .views import Home, BaseballList, BaseballDetail, GameListCreate, GameDetail, PlayerList, PlayerDetail, AddPlayerToBaseball, RemovePlayerFromBaseball

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('baseballs/', BaseballList.as_view(), name='baseball-list'),
    path('baseballs/<int:id>/', BaseballDetail.as_view(), name='baseball-detail'),
    path('baseballs/<int:baseball_id>/games/', GameListCreate.as_view(), name='game-list-create'),
    path('baseballs/<int:baseball_id>/games/<int:id>/', GameDetail.as_view(), name='game-detail'),
    path('players/', PlayerList.as_view(), name='player-list'),
    path('players/<int:id>/', PlayerDetail.as_view(), name='player-detail'),
    path('baseballs/<int:baseball_id>/add_baseball/<int:baseball_id>/', AddPlayerToBaseball.as_view(), name='add-player-to-baseball'),
    path('baseballs/<int:baseball_id>/remove_player/<int:player_id>/', RemovePlayerFromBaseball.as_view(), name='remove-player-from-baseball'),

]
