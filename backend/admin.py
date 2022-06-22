from django.contrib import admin
from .models import MarkingDepartment
from .models import MarkingDepartmentDependsLocationNumber
from .models import MarkingDepartmentDependsBuildings
from .models import MarkingDepartmentPublicPart
from .models import OwnershipDepartment
from .models import OtherShipDepartment
from .models import StartCrawler
from backend.lib.main import NewCrawler 
from backend.lib import parse_txt_excel
from backend.lib import parse_pdf
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
        'create_time',
        'update_time'
    )
    search_fields = ['sheet1','sheet2','sheet3','sheet4']


class MarkingDepartmentDependsLocationNumberAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = (
        'id',
        'markingdepartment',
        'sheet1',
        'create_time',
        'update_time'
    )


class MarkingDepartmentDependsBuildingsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = (
        'id',
        'markingdepartment',
        'sheet1',
        'sheet2',
        'create_time',
        'update_time'
    )


class MarkingDepartmentPublicPartAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = (
        'id',
        'markingdepartment',
        'sheet1',
        'sheet2',
        'sheet3',
        'sheet4',
        'sheet5',
        'create_time',
        'update_time'
    )


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
        'create_time',
        'update_time'
    )
    search_fields = ['sheet1','sheet2','sheet3','sheet4']


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
    search_fields = ['sheet1','sheet2','sheet3','sheet4']


# @admin.action(description='開始爬蟲')
# def make_crawler(modeladmin, request, queryset):
#     NewCrawler().main_start()
    

class StartCrawlerAdmin(DjangoObjectActions, ImportExportMixin, admin.ModelAdmin):
    def make_crawler(modeladmin, request, queryset):
        print("開始爬蟲")
        start_scheduler = StartCrawler.objects.create()

        NewCrawler().main_start()
        start_scheduler.update(
            status=True
        )
    def make_excel(modeladmin, request, queryset):
        print('輸出excel')
        file_path = parse_txt_excel.StartParseExcel().main()
        print(file_path)
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    def make_pdf(modeladmin, request, queryset):
        parse_pdf.StartParsePdf().main()

    list_display = (
        'id',
        'create_time',
        'status'
    )
    changelist_actions = ('make_crawler','make_excel','make_pdf' )
    # actions = [make_crawler]

admin.site.site_header = '地政事務所 - 爬蟲資料庫'
admin.site.site_title = '地政事務所 - 爬蟲資料庫'
admin.site.index_title = '功能列表'

admin.site.register(MarkingDepartment, MarkingDepartmentAdmin)
admin.site.register(MarkingDepartmentDependsLocationNumber,
                    MarkingDepartmentDependsLocationNumberAdmin)
admin.site.register(MarkingDepartmentDependsBuildings,
                    MarkingDepartmentDependsBuildingsAdmin)
admin.site.register(MarkingDepartmentPublicPart,
                    MarkingDepartmentPublicPartAdmin)
admin.site.register(OwnershipDepartment, OwnershipDepartmentAdmin)
admin.site.register(OtherShipDepartment, OtherShipDepartmentAdmin)
admin.site.register(StartCrawler, StartCrawlerAdmin)
