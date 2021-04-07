
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='page-home'),
    path('season/<str:serie>/<int:number>', views.season, name='page-season'),
    path('episode/<int:episode_id>', views.episode, name='page-episode'),
    path('character/<str:char_name>', views.character, name='page-character'),
    path('search_result/<str:char_name>', views.search_result, name='page-search_result'),
]
