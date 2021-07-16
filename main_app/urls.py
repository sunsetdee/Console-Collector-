from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('consoles/', views.consoles_index, name='index'),
    path('consoles/<int:console_id>/', views.consoles_detail, name='detail'),
    path('consoles/create/', views.ConsoleCreate.as_view(), name='consoles_create'),
    path('consoles/<int:pk>/update/', views.ConsoleUpdate.as_view(), name='consoles_update'),
    path('consoles/<int:pk>/delete/', views.ConsoleDelete.as_view(), name='consoles_delete'),
    path('consoles/<int:console_id>/add_accessory/', views.add_accessory, name='add_accessory'),
    path('games/', views.GameList.as_view(), name='games_index'),
    path('games/<int:pk>/', views.GameDetail.as_view(), name='games_detail'),
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
]