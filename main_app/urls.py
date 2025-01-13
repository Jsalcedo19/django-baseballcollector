from django.urls import path
from .views import Home, BaseballList, BaseballDetail

urlpatterns = [
  path('', Home.as_view(), name='home'),
 path('baseballs/', BaseballList.as_view(), name='baseball-list'),
  path('baseballs/<int:id>/', BaseballDetail.as_view(), name='baseball-detail'),
]
