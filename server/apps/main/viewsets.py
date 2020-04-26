from django.http import Http404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from main.models import Subject, GameRoom, User
from main.serializers import (
    SubjectSerializer,
    GameRoomSerializer,
    UserSerializer,
    SubjectMoveSerializer,
)


class SubjectViewSet(ModelViewSet):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    @action(detail=True, methods=["post"])
    def move(self, request, pk=None):
        subject: Subject = self.get_object()
        serializer = SubjectMoveSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            subject.move(
                serializer.validated_data["x_pos"], serializer.validated_data["y_pos"]
            )
            return Response(status=HTTP_200_OK, data=SubjectSerializer(instance=subject).data)


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
