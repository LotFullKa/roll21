from django.http import Http404
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from main.models import Subject, GameRoom, User
from main.serializers import SubjectSerializer, GameRoomSerializer, UserSerializer


class SubjectViewSet(ModelViewSet):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class GameRoomView(APIView):
    """API View for represent game room."""

    def get(self, request):
        """Get HTTP method for API View."""

        game_room = GameRoom.objects.first()
        if not game_room:
            raise Http404()
        serializer = GameRoomSerializer(instance=game_room)
        return Response(data=serializer.data, status=HTTP_200_OK)


class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
