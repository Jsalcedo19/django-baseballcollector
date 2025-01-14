from django.urls import path
from .views import Home, BaseballList, BaseballDetail, GameListCreate, GameDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('baseballs/', BaseballList.as_view(), name='baseball-list'),
    path('baseballs/<int:id>/', BaseballDetail.as_view(), name='baseball-detail'),
    path('baseballs/<int:baseball_id>/games/', GameListCreate.as_view(), name='game-list-create'),
    path('baseballs/<int:baseball_id>/games/<int:id>/', GameDetail.as_view(), name='game-detail'),

]
