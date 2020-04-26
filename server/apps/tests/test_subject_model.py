from unittest import mock
from django.test import TestCase

from main.constants import ColorEnum
from main.factories import SubjectFactory
from main.models import Subject, default_color
from utils.enum_helpers import enum_to_key_list


class SubjectTestCase(TestCase):
    def test_subject_str(self):
        subject: Subject = SubjectFactory()
        self.assertEqual(str(subject), subject.name)

    def test_generate_pos(self):
        with mock.patch("main.models.randint", lambda *args: 10):
            subject: Subject = SubjectFactory()

        self.assertEqual(subject.x_pos, 10)
        self.assertEqual(subject.y_pos, 10)

        with mock.patch("main.models.randint", lambda *args: 0):
            x, y = subject.generate_pos()

        self.assertEqual(x, 0)
        self.assertEqual(y, 0)

        with mock.patch("main.models.randint", lambda *args: 10):
            self.assertRaises(RecursionError, subject.generate_pos)

    def test_move(self):
        subject: Subject = SubjectFactory()
        subject.move(0, 0)
        subject = Subject.objects.get(id=subject.id)
        self.assertEqual(subject.y_pos, 0)
        self.assertEqual(subject.x_pos, 0)

    def test_save(self):
        with mock.patch("main.models.randint", lambda *args: 10):
            subject: Subject = SubjectFactory()

        self.assertEqual(subject.x_pos, 10)
        self.assertEqual(subject.y_pos, 10)

        subject.save()

        subject = Subject.objects.get(id=subject.id)

        self.assertEqual(subject.x_pos, 10)
        self.assertEqual(subject.y_pos, 10)

        subject: Subject = SubjectFactory.create(x_pos=5, y_pos=5)

        subject.save()

        subject = Subject.objects.get(id=subject.id)

        self.assertEqual(subject.x_pos, 5)
        self.assertEqual(subject.y_pos, 5)

    def test_default_color(self):
        with mock.patch("main.models.random_enum_key", lambda enum: enum_to_key_list(enum)[0]):
            self.assertEqual(default_color(), enum_to_key_list(ColorEnum)[0])
