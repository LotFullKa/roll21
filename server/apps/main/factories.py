import factory

from main.constants import SubjectTypeEnum, ColorEnum
from main.models import Subject
from utils.enum_helpers import enum_to_key_list


class SubjectFactory(factory.DjangoModelFactory):
    name = factory.Faker('name')
    type_of_subject = factory.Faker('random_element', elements=enum_to_key_list(SubjectTypeEnum))
    color = factory.Faker('random_element', elements=enum_to_key_list(ColorEnum))

    class Meta:
        model = Subject
