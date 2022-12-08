from django.urls import path
from .views import PlayerListView, PlayerDetailView, PlayerCreateView, PlayerUpdateView, PlayerDeleteView

urlpatterns = [
    path('', PlayerListView.as_view(), name='home'),
    path('<int:pk>/', PlayerDetailView.as_view(), name='player_detail'),
    path('create/', PlayerCreateView.as_view(), name='player_create'),
    path('<int:pk>/update/', PlayerUpdateView.as_view(), name='player_update'),
    path('<int:pk>/delete/', PlayerDeleteView.as_view(), name='player_delete'),
]