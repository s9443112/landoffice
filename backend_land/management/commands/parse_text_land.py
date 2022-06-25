from django.core.management.base import BaseCommand
from backend_land.lib import parse_text_land



class Command(BaseCommand):
    def __init__(self):
        pass
    def handle(self, **options):
        parse_text_land.StartParseText().main()