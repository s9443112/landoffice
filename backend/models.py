from django.db import models
from datetime import datetime
# Create your models here.


class DateTimeWithoutTZField(models.DateTimeField):
    def db_type(self, connection):
        return 'timestamp'


class MarkingDepartment(models.Model):
    class Meta:
        verbose_name = '標示部'
        verbose_name_plural = '標示部'

    sheet1 = models.CharField('縣市',  max_length=50, default=None, null=True, blank=True)
    sheet2 = models.CharField('鄉鎮市區',  max_length=50, default=None, null=True, blank=True)
    sheet3 = models.CharField('地段',  max_length=50, default=None, null=True, blank=True)
    sheet4 = models.CharField('建號',  max_length=50, default=None, null=True, blank=True)
    sheet5 = models.CharField('登記日期',  max_length=50, default=None, null=True, blank=True)
    sheet6 = models.CharField('登記原因',  max_length=50, default=None, null=True, blank=True)
    sheet7 = models.CharField('建物門牌',  max_length=50, default=None, null=True, blank=True)
    sheet8 = models.CharField('主要用途',  max_length=50, default=None, null=True, blank=True)
    sheet9 = models.CharField('主要建材',  max_length=50, default=None, null=True, blank=True)
    sheet10 = models.CharField('層數',  max_length=50, default=None, null=True, blank=True)
    sheet11 = models.CharField('總面積',  max_length=50, default=None, null=True, blank=True)
    sheet12 = models.CharField('層次',  max_length=50, default=None, null=True, blank=True)
    sheet13 = models.CharField('層次面積',  max_length=50, default=None, null=True, blank=True)
    sheet14 = models.CharField('建築完成日期',  max_length=50, default=None, null=True, blank=True)

    sheet15 = models.CharField('其他登記事項', max_length=50, default=None, null=True, blank=True)
    create_time = DateTimeWithoutTZField('建立日期', default=datetime.now)
    update_time = DateTimeWithoutTZField('更新日期', default=datetime.now)

    def __str__(self):
        return self.sheet3 +' / ' +self.sheet4


class MarkingDepartmentDependsLocationNumber(models.Model):
    class Meta:
        verbose_name = '標示部-建物坐落地號'
        verbose_name_plural = '標示部-建物坐落地號'

    markingdepartment = models.ForeignKey(
        MarkingDepartment, on_delete=models.CASCADE)
    sheet1 = models.CharField('建物坐落地號',  max_length=50, default=None, null=True, blank=True)
    create_time = DateTimeWithoutTZField('建立日期', default=datetime.now)
    update_time = DateTimeWithoutTZField('更新日期', default=datetime.now)


class MarkingDepartmentDependsBuildings(models.Model):
    class Meta:
        verbose_name = '標示部-附屬建物'
        verbose_name_plural = '標示部-附屬建物'

    markingdepartment = models.ForeignKey(
        MarkingDepartment, on_delete=models.CASCADE)

    sheet1 = models.CharField('附屬建物用途',  max_length=50, default=None, null=True, blank=True)
    sheet2 = models.CharField('面積',  max_length=50, default=None, null=True, blank=True)
    create_time = DateTimeWithoutTZField('建立日期', default=datetime.now)
    update_time = DateTimeWithoutTZField('更新日期', default=datetime.now)


class MarkingDepartmentPublicPart(models.Model):
    class Meta:
        verbose_name = '標示部-共有部分'
        verbose_name_plural = '標示部-共有部分'

    markingdepartment = models.ForeignKey(
        MarkingDepartment, on_delete=models.CASCADE)
    sheet1 = models.CharField('共有部分',  max_length=50, default=None, null=True, blank=True)
    sheet2 = models.CharField('權利範圍',  max_length=50, default=None, null=True, blank=True)
    sheet3 = models.CharField('面積',  max_length=50, default=None, null=True, blank=True)
    sheet4 = models.CharField('其他登記事項',  max_length=255, default=None, null=True, blank=True)
    sheet5 = models.CharField('含停車位',  max_length=50, default=None, null=True, blank=True)
    create_time = DateTimeWithoutTZField('建立日期', default=datetime.now)
    update_time = DateTimeWithoutTZField('更新日期', default=datetime.now)


class OwnershipDepartment(models.Model):
    class Meta:
        verbose_name = '所有權部'
        verbose_name_plural = '所有權部'

    sheet1 = models.CharField('縣市名稱',  max_length=50, default=None, null=True, blank=True)
    sheet2 = models.CharField('鄉鎮市區',  max_length=50, default=None, null=True, blank=True)
    sheet3 = models.CharField('地段',  max_length=50, default=None, null=True, blank=True)
    sheet4 = models.CharField('建號',  max_length=50, default=None, null=True, blank=True)
    sheet5 = models.CharField('登記次序',  max_length=50, default=None, null=True, blank=True)
    sheet6 = models.CharField('登記日期',  max_length=50, default=None, null=True, blank=True)
    sheet7 = models.CharField('登記原因',  max_length=50, default=None, null=True, blank=True)
    sheet8 = models.CharField('原因發生日期',  max_length=50, default=None, null=True, blank=True)
    sheet9 = models.CharField('所有權人姓名',  max_length=50, default=None, null=True, blank=True)
    sheet10 = models.CharField('統一編號',  max_length=50, default=None, null=True, blank=True)
    sheet11 = models.CharField('住址',  max_length=50, default=None, null=True, blank=True)
    sheet12 = models.CharField('權利範圍',  max_length=50, default=None, null=True, blank=True)
    sheet13 = models.CharField('權狀字號',  max_length=50, default=None, null=True, blank=True)
    sheet14 = models.CharField('相關他項登記次序',  max_length=50, default=None, null=True, blank=True)
    sheet15 = models.CharField('其他登記事項',  max_length=50, default=None, null=True, blank=True)
    create_time = DateTimeWithoutTZField('建立日期', default=datetime.now)
    update_time = DateTimeWithoutTZField('更新日期', default=datetime.now)


class OtherShipDepartment(models.Model):
    class Meta:
        verbose_name = '他項權利部'
        verbose_name_plural = '他項權利部'
    sheet1 = models.CharField('縣市名稱',  max_length=50, default=None, null=True, blank=True)
    sheet2 = models.CharField('鄉鎮市區',  max_length=50, default=None, null=True, blank=True)
    sheet3 = models.CharField('地段',  max_length=50, default=None, null=True, blank=True)
    sheet4 = models.CharField('建號',  max_length=50, default=None, null=True, blank=True)
    sheet5 = models.CharField('登記次序',  max_length=50, default=None, null=True, blank=True)
    sheet6 = models.CharField('權利種類',  max_length=50, default=None, null=True, blank=True)
    sheet7 = models.CharField('收件年期',  max_length=50, default=None, null=True, blank=True)
    sheet8 = models.CharField('收件字號',  max_length=50, default=None, null=True, blank=True)
    sheet9 = models.CharField('登記日期',  max_length=50, default=None, null=True, blank=True)
    sheet10 = models.CharField('登記原因',  max_length=50, default=None, null=True, blank=True)
    sheet11 = models.CharField('權利人姓名',  max_length=50, default=None, null=True, blank=True)
    sheet12 = models.CharField('權利人統一編號',  max_length=50, default=None, null=True, blank=True)
    sheet13 = models.CharField('住址',  max_length=50, default=None, null=True, blank=True)
    sheet14 = models.CharField('債權額比例',  max_length=50, default=None, null=True, blank=True)
    sheet15 = models.CharField('擔保債權總金額',  max_length=50, default=None, null=True, blank=True)
    sheet16 = models.CharField('擔保債權確定期日',  max_length=50, default=None, null=True, blank=True)
    sheet17 = models.CharField('存續期間',  max_length=50, default=None, null=True, blank=True)
    sheet18 = models.CharField('清償日期',  max_length=50, default=None, null=True, blank=True)
    sheet19 = models.CharField('利息(率)或地租',  max_length=50, default=None, null=True, blank=True)
    sheet20 = models.CharField('遲延利息(率)',  max_length=50, default=None, null=True, blank=True)
    sheet21 = models.CharField('違約金',  max_length=50, default=None, null=True, blank=True)
    sheet22 = models.CharField('權利標的',  max_length=50, default=None, null=True, blank=True)
    sheet23 = models.CharField('標的登記次序',  max_length=50, default=None, null=True, blank=True)
    sheet24 = models.CharField('設定權利範圍',  max_length=50, default=None, null=True, blank=True)
    sheet25 = models.CharField('證明書字號',  max_length=50, default=None, null=True, blank=True)
    sheet26 = models.CharField('共同擔保地號',  max_length=50, default=None, null=True, blank=True)
    sheet27 = models.CharField('共同擔保建號',  max_length=50, default=None, null=True, blank=True)
    sheet28 = models.CharField('其他登記事項',  max_length=50, default=None, null=True, blank=True)
    sheet29 = models.CharField('擔保債權種類及範圍',  max_length=250, default=None, null=True, blank=True)
    create_time = DateTimeWithoutTZField('建立日期', default=datetime.now)
    update_time = DateTimeWithoutTZField('更新日期', default=datetime.now)


class StartCrawler(models.Model):
    class Meta:
        verbose_name = '爬蟲紀錄'
        verbose_name_plural = '爬蟲紀錄'

    create_time = DateTimeWithoutTZField('建立日期', default=datetime.now)


    