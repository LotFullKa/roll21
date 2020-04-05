from rest_framework.viewsets import ModelViewSet
from main.models import Subject
from main.serialzizers import SubjectSerializer


class SubjectViewSet(ModelViewSet):

    queryset = Subject.objects.all()

    serializer_class = SubjectSerializer
