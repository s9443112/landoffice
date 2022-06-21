from rest_framework import serializers
from .models import MarkingDepartment
from .models import MarkingDepartmentDependsLocationNumber
from .models import MarkingDepartmentDependsBuildings
from .models import MarkingDepartmentPublicPart
from .models import OwnershipDepartment
from .models import OtherShipDepartment


class MarkingDepartmentSeializer(serializers.ModelSerializer):
    class Meta:
        model = MarkingDepartment
        fields = (
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


class MarkingDepartmentDependsLocationNumberSeializer(serializers.ModelSerializer):
    class Meta:
        model = MarkingDepartmentDependsLocationNumber
        fields = (
            'id',
            'sheet1',
        )


class MarkingDepartmentDependsBuildingsSeializer(serializers.ModelSerializer):
    class Meta:
        model = MarkingDepartmentDependsBuildings
        fields = (
            'id',
            'sheet1',
            'sheet2',
           
        )


class MarkingDepartmentPublicPartSeializer(serializers.ModelSerializer):
    class Meta:
        model = MarkingDepartmentPublicPart
        fields = (
            'id',
            'sheet1',
            'sheet2',
            'sheet3',
            'sheet4',
            'sheet5',
        )


class OwnershipDepartmentSeializer(serializers.ModelSerializer):
    class Meta:
        model = OwnershipDepartment
        fields = (
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


class OtherShipDepartmentSeializer(serializers.ModelSerializer):
    class Meta:
        model = OtherShipDepartment
        fields = (
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
