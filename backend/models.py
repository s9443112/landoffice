from django.db import models

# Create your models here.
class DateTimeWithoutTZField(models.DateTimeField):
    def db_type(self, connection):
        return 'timestamp'

class MarkingDepartment(models.Model):
    class Meta:
        verbose_name = '標示部'
        verbose_name_plural = '標示部'

    city = models.CharField('縣市', max_length=50)
    city = models.CharField('鄉鎮市區', max_length=50)
    city = models.CharField('地段', max_length=50)
    city = models.CharField('建號', max_length=50)
    city = models.CharField('登記日期', max_length=50)
    city = models.CharField('登記原因', max_length=50)
    city = models.CharField('建物門牌', max_length=50)

    # Multi column
    # city = models.CharField('建物坐落地號', max_length=50) 
     
    city = models.CharField('主要用途', max_length=50)
    city = models.CharField('主要建材', max_length=50)
    city = models.CharField('層數', max_length=50)
    city = models.CharField('總面積', max_length=50)
    city = models.CharField('層次', max_length=50)
    city = models.CharField('層次面積', max_length=50)
    city = models.CharField('建築完成日期', max_length=50)

    city = models.CharField('其他登記事項', max_length=50)

class MarkingDepartmentDependsBuildings(models.Model):
    class Meta:
        verbose_name = '標示部-附屬建物'
        verbose_name_plural = '標示部-附屬建物'

    name = models.CharField('附屬建物用途', max_length=50)
    name = models.CharField('面積', max_length=50)

class MarkingDepartmentPublicPart(models.Model):
    class Meta:
        verbose_name = '標示部-共有部分'
        verbose_name_plural = '標示部-共有部分'

    name = models.CharField('共有部分', max_length=50)
    name = models.CharField('權利範圍', max_length=50)
    name = models.CharField('面積', max_length=50)
    name = models.CharField('其他登記事項', max_length=50)