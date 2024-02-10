import datetime

from django.core.management.base import BaseCommand
from app_1.models import Author

class Command(BaseCommand):
    help = "Create new user."

    def handle(self, *args, **kwargs):
        for i in range (1,11):
            author = Author(
                name=f'Author {i}',
                last_name = f'Last_name {i}',
                email=f'mail{i}@example.com',
                bio= 'Lorem ipsum',
                birthday = datetime.date(2000,1,1)
            )
            self.stdout.write(self.style.ERROR(f'Author{author} created'))
            author.save()