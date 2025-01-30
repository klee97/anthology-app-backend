import csv
from django.core.management.base import BaseCommand
from stories.models import Story

# python manage.py import_stories stories.csv
class Command(BaseCommand):
    help = 'Import stories from CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_path = options['csv_file']
        
        with open(csv_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Story.objects.create(
                    title=row['title'],
                    author=row['author'],
                    link=row.get('link', '')
                )
                self.stdout.write(self.style.SUCCESS(f'Imported: {row["title"]}'))