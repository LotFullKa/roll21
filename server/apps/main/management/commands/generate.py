from django.core.management import BaseCommand

from main.factories import SubjectFactory

class Command(BaseCommand):
    @staticmethod
    def generate_dots():
        for i in range(3):
            SubjectFactory()


    def handle(self, *args, **kwargs):
        self.generate_dots()
