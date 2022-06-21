from django.contrib import admin
from .models import MarkingDepartment
from .models import MarkingDepartmentDependsLocationNumber
from .models import MarkingDepartmentDependsBuildings
from .models import MarkingDepartmentPublicPart
from .models import OwnershipDepartment
from .models import OtherShipDepartment
# Register your models here.


class MarkingDepartmentAdmin(admin.ModelAdmin):
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
        'sheet15'
    )


class MarkingDepartmentDependsLocationNumberAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'markingdepartment',
        'sheet1',
    )


class MarkingDepartmentDependsBuildingsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'markingdepartment',
        'sheet1',
        'sheet2',
    )


class MarkingDepartmentPublicPartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'markingdepartment',
        'sheet1',
        'sheet2',
        'sheet3',
        'sheet4',
        'sheet5',
    )


class OwnershipDepartmentAdmin(admin.ModelAdmin):
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
        'sheet15'
    )


class OtherShipDepartmentAdmin(admin.ModelAdmin):
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
    )


admin.site.register(MarkingDepartment, MarkingDepartmentAdmin)
admin.site.register(MarkingDepartmentDependsLocationNumber,
                    MarkingDepartmentDependsLocationNumberAdmin)
admin.site.register(MarkingDepartmentDependsBuildings,
                    MarkingDepartmentDependsBuildingsAdmin)
admin.site.register(MarkingDepartmentPublicPart,
                    MarkingDepartmentPublicPartAdmin)
admin.site.register(OwnershipDepartment, OwnershipDepartmentAdmin)
admin.site.register(OtherShipDepartment, OtherShipDepartmentAdmin)
