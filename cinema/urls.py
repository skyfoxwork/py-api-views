from django.urls import path, include

from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet,
)

cinema_hall_list = CinemaHallViewSet.as_view(actions={
    "get": "list",
    "post": "create"
})

cinema_hall_detail = CinemaHallViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    # path("movies/", movie_list, name="movie-list"),
    # path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("genres/", GenreList.as_view(), name="gener-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="gener-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", cinema_hall_list, name="cinema-hall-list"),
    path(
        "cinema_halls/<int:pk>/",
        cinema_hall_detail,
        name="cinema-hall-detail"
    ),
    path("", include(router.urls))
]

app_name = "cinema"
