from django.urls import path, include
from watchlist_app.api.views import MoviesList, MovieDetail

urlpatterns = [
    path('list/', MoviesList.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetail.as_view(), name='movie-detail'),
]
