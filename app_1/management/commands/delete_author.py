from django.core.management.base import BaseCommand
from app_1.models import Author

class Command(BaseCommand):
    help = "Deletes author by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID to delete')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        author = Author.objects.filter(pk=pk).first()св
        if author is not None:
            author.delete()
            self.stdout.write(self.style.ERROR(f'Deleted author: {author}'))
            #  ERROR: Сообщение Deleted author - красного цвета, SUCCESS - зеленого