import unittest
from enum import Enum
from unittest import mock

from utils.enum_helpers import enum_to_choices, enum_to_key_list, random_enum_key


class EnumHelpersTestCase(unittest.TestCase):
    class TestEnum(Enum):
        key1 = "key1"
        key2 = "key2"

    def test_enum_to_choices(self):
        choices = enum_to_choices(self.TestEnum)

        self.assertEqual(choices[0], (self.TestEnum.key1.name, self.TestEnum.key1.value))
        self.assertEqual(choices[1], (self.TestEnum.key2.name, self.TestEnum.key2.value))

    def test_enum_to_key_list(self):
        key_list = enum_to_key_list(self.TestEnum)
        self.assertEqual(key_list, [self.TestEnum.key1.name, self.TestEnum.key2.name])

    def test_random_enum_key(self):
        with mock.patch('utils.enum_helpers.random.choice', lambda choices: choices[0]):
            self.assertEqual(random_enum_key(self.TestEnum), self.TestEnum.key1.name)
