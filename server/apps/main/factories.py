import factory

from main.constants import SubjectTypeEnum, ColorEnum
from main.models import Subject, GameRoom, User
from utils.enum_helpers import enum_to_key_list
from mimesis_factory import MimesisField


class SubjectFactory(factory.DjangoModelFactory):
    name = MimesisField('username')
    type_of_subject = factory.Faker('random_element', elements=enum_to_key_list(SubjectTypeEnum))
    color = factory.Faker('random_element', elements=enum_to_key_list(ColorEnum))

    class Meta:
        model = Subject


class UserFactory(factory.DjangoModelFactory):
    username = MimesisField('username')

    class Meta:
        model = User


class GameRoomFactory(factory.DjangoModelFactory):
    name = MimesisField('username')
    now_player = factory.SubFactory(SubjectFactory)

    @factory.post_generation
    def players(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for user in extracted:
                self.players.add(user)

    class Meta:
        model = GameRoom
