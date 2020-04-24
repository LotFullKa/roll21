from django.test import TestCase

# Create your tests here.
from main.factories import SubjectFactory


class SubjectTestCase(TestCase):
    def setUp(self) -> None:
        self.subject = SubjectFactory()

    def test_subject_str(self):
        self.assertEqual(str(self.subject), self.subject.name)
