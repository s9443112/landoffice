from django.contrib import admin
from .models import MarkingDepartment
from .models import OwnershipDepartment
from .models import OwnershipDepartment
from .models import OwnershipDepartmentHistory
from .models import OtherShipDepartment
from .models import StartCrawler
from backend_land.lib.main import NewCrawler
from backend_land.lib.main_chunghwa import NewCrawler as chunghwa
from backend_land.lib import parse_txt_excel
from backend_land.lib import parse_pdf
from backend_land.lib import custom_excel
from import_export.admin import ImportExportMixin
from django_object_actions import DjangoObjectActions
from django.http import HttpResponse
import os
# Register your models here.


class MarkingDepartmentAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = (
        'id',
        'sheet1',
        'sheet2',
        'sheet3',
        'sheet4',
        'sheet5',
        'sheet6',
        'sheet7',
        'sheet8',
        'sheet9',
        'sheet10',
        'sheet11',
        'sheet12',
        'sheet13',
        'sheet14',
        'sheet15',
        'sheet16',

        'create_time',
        'update_time'
    )
    search_fields = ['sheet1', 'sheet2', 'sheet3', 'sheet4']


class OwnershipDepartmentAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = (
        'id',
        'sheet1',
        'sheet2',
        'sheet3',
        'sheet4',
        'sheet5',
        'sheet6',
        'sheet7',
        'sheet8',
        'sheet9',
        'sheet10',
        'sheet11',
        'sheet12',
        'sheet13',
        'sheet14',
        'sheet15',
        'sheet16',
        'sheet17',
        'sheet18',
        'create_time',
        'update_time'
    )
    search_fields = ['sheet1', 'sheet2', 'sheet3', 'sheet4']


class OwnershipDepartmentHistoryAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = (
        'id',
        'ownershipdepartment',
        'sheet1',
        'sheet2',
        'sheet3',
        'create_time',
        'update_time'
    )


class OtherShipDepartmentAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = (
        'id',
        'sheet1',
        'sheet2',
        'sheet3',
        'sheet4',
        'sheet5',
        'sheet6',
        'sheet7',
        'sheet8',
        'sheet9',
        'sheet10',
        'sheet11',
        'sheet12',
        'sheet13',
        'sheet14',
        'sheet15',
        'sheet16',
        'sheet17',
        'sheet18',
        'sheet19',
        'sheet20',
        'sheet21',
        'sheet22',
        'sheet23',
        'sheet24',
        'sheet25',
        'sheet26',
        'sheet27',
        'sheet28',
        'sheet29',
        'create_time',
        'update_time'
    )
    search_fields = ['sheet1', 'sheet2', 'sheet3', 'sheet4']


# @admin.action(description='????????????')
# def make_crawler(modeladmin, request, queryset):
#     NewCrawler().main_start()


class StartCrawlerAdmin(DjangoObjectActions, ImportExportMixin, admin.ModelAdmin):
    def chunghwa(modeladmin, request, queryset):
        print("????????????")
        StartCrawler.objects.create()
        chunghwa().main_start()

        start_scheduler = StartCrawler.objects.all().order_by('-id')[:1]

        start_scheduler = StartCrawler.objects.get(id=start_scheduler[0].id)
        start_scheduler.status = True
        start_scheduler.save()

    def make_crawler(modeladmin, request, queryset):
        print("????????????")
        StartCrawler.objects.create()
        NewCrawler().main_start()

        start_scheduler = StartCrawler.objects.all().order_by('-id')[:1]
        # print(start_scheduler)

        start_scheduler = StartCrawler.objects.get(id=start_scheduler[0].id)
        start_scheduler.status = True
        start_scheduler.save()

    def make_excel(modeladmin, request, queryset):
        print('??????excel')
        file_path = parse_txt_excel.StartParseExcel().main()
        print(file_path)
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + \
                os.path.basename(file_path)
            return response

    def make_pdf(modeladmin, request, queryset):
        parse_pdf.StartParsePdf().main()

    def custom_excel(modeladmin, request, queryset):
        print('?????? CUstom excel')
        file_path = custom_excel.CusStartParseExcel().main()
        print(file_path)
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + \
                os.path.basename(file_path)
            return response

    list_display = (
        'id',
        'create_time',
        'status'
    )
    changelist_actions = ('make_crawler', 'make_excel',
                          'custom_excel', 'make_pdf')
    # actions = [make_crawler]


admin.site.site_header = '??????????????? - ?????????????????????'
admin.site.site_title = '??????????????? - ?????????????????????'
admin.site.index_title = '????????????'

admin.site.register(MarkingDepartment, MarkingDepartmentAdmin)
admin.site.register(OwnershipDepartment, OwnershipDepartmentAdmin)
admin.site.register(OwnershipDepartmentHistory,
                    OwnershipDepartmentHistoryAdmin)
admin.site.register(OtherShipDepartment, OtherShipDepartmentAdmin)
admin.site.register(StartCrawler, StartCrawlerAdmin)
