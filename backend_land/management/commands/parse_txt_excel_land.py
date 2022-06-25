from django.core.management.base import BaseCommand
from backend_land.lib import parse_txt_excel




class Command(BaseCommand):
    def __init__(self):
        pass
    def handle(self, **options):
        parse_txt_excel.StartParseExcel().main()