from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, Serializer, IntegerField
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


class SubjectMoveSerializer(Serializer):
    x_pos = IntegerField()
    y_pos = IntegerField()

    def validate(self, attrs):
        if Subject.objects.filter(x_pos=attrs['x_pos'], y_pos=attrs['y_pos']).exists():
            raise ValidationError('Cell already in use')
        return attrs
