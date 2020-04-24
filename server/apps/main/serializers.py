from rest_framework.serializers import ModelSerializer
from main.models import Subject, GameRoom, User


class SubjectSerializer(ModelSerializer):

    class Meta:
        model = Subject
        fields = "__all__"


class GameRoomSerializer(ModelSerializer):

    class Meta:
        model = GameRoom
        fields = "__all__"


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username']
