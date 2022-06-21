from django.core.management.base import BaseCommand
from backend.lib import crawler



class Command(BaseCommand):
    def __init__(self):
        pass
    def handle(self, **options):
        crawler.StartCrawler().main()