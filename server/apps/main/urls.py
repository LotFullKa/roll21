from django.urls import path
from rest_framework import routers

from main.apps import MainConfig
from main.viewsets import SubjectViewSet, UserViewSet, GameRoomView

router = routers.DefaultRouter()
router.register(r'subjects', SubjectViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls + [
    path('game-room', GameRoomView.as_view(), name="game-room")
]

app_name = MainConfig.name