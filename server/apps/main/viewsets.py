from rest_framework.viewsets import ModelViewSet
from main.models import Subject, GameRoom, User
from main.serializers import SubjectSerializer, GameRoomSerializer, UserSerializer


class SubjectViewSet(ModelViewSet):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class GameRoomViewSet(ModelViewSet):

    queryset = GameRoom.objects.all()
    serializer_class = GameRoomSerializer


class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
