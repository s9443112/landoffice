from django.core.management.base import BaseCommand
from backend.lib import parse_text



class Command(BaseCommand):
    def __init__(self):
        pass
    def handle(self, **options):
        parse_text.StartParseText().main()