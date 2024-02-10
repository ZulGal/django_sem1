import datetime

from django.core.management.base import BaseCommand
from app_1.models import Author, Post

class Command(BaseCommand):
    help = "Creates postts to fill db"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of posts to create per author')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        authors = Author.objects.all()
        for author in authors:
            for i in range(count):
                post = Post(
                    title=f'Title {i}',
                    content=f'Content {i}',
                    author = author,
                )
                self.stdout.write(self.style.SUCCESS(f'Created {post}'))
                post.save()
