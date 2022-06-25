from django.core.management.base import BaseCommand
from backend_land.lib import crawler_land



class Command(BaseCommand):
    def __init__(self):
        pass
    def handle(self, **options):
        crawler_land.StartLandCrawler().main()