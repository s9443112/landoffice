# Generated by Django 4.0.5 on 2022-06-21 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarkingDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet1', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='縣市')),
                ('sheet2', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='鄉鎮市區')),
                ('sheet3', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='地段')),
                ('sheet4', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='建號')),
                ('sheet5', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='登記日期')),
                ('sheet6', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='登記原因')),
                ('sheet7', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='建物門牌')),
                ('sheet8', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='主要用途')),
                ('sheet9', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='主要建材')),
                ('sheet10', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='層數')),
                ('sheet11', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='總面積')),
                ('sheet12', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='層次')),
                ('sheet13', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='層次面積')),
                ('sheet14', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='建築完成日期')),
                ('sheet15', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='其他登記事項')),
            ],
            options={
                'verbose_name': '標示部',
                'verbose_name_plural': '標示部',
            },
        ),
        migrations.CreateModel(
            name='OtherShipDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet1', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='縣市名稱')),
                ('sheet2', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='鄉鎮市區')),
                ('sheet3', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='地段')),
                ('sheet4', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='建號')),
                ('sheet5', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='登記次序')),
                ('sheet6', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='權利種類')),
                ('sheet7', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='收件年期')),
                ('sheet8', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='收件字號')),
                ('sheet9', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='登記日期')),
                ('sheet10', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='登記原因')),
                ('sheet11', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='權利人姓名')),
                ('sheet12', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='權利人統一編號')),
                ('sheet13', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='住址')),
                ('sheet14', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='債權額比例')),
                ('sheet15', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='擔保債權總金額')),
                ('sheet16', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='擔保債權確定期日')),
                ('sheet17', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='存續期間')),
                ('sheet18', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='清償日期')),
                ('sheet19', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='利息(率)或地租')),
                ('sheet20', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='遲延利息(率)')),
                ('sheet21', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='違約金')),
                ('sheet22', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='權利標的')),
                ('sheet23', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='標的登記次序')),
                ('sheet24', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='設定權利範圍')),
                ('sheet25', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='證明書字號')),
                ('sheet26', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='共同擔保地號')),
                ('sheet27', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='共同擔保建號')),
                ('sheet28', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='其他登記事項')),
                ('sheet29', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='擔保債權種類及範圍')),
            ],
            options={
                'verbose_name': '他項權利部',
                'verbose_name_plural': '他項權利部',
            },
        ),
        migrations.CreateModel(
            name='OwnershipDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet1', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='縣市名稱')),
                ('sheet2', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='鄉鎮市區')),
                ('sheet3', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='地段')),
                ('sheet4', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='建號')),
                ('sheet5', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='登記次序')),
                ('sheet6', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='登記日期')),
                ('sheet7', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='登記原因')),
                ('sheet8', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='原因發生日期')),
                ('sheet9', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='所有權人姓名')),
                ('sheet10', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='統一編號')),
                ('sheet11', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='住址')),
                ('sheet12', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='權利範圍')),
                ('sheet13', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='權狀字號')),
                ('sheet14', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='相關他項登記次序')),
                ('sheet15', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='其他登記事項')),
            ],
            options={
                'verbose_name': '所有權部',
                'verbose_name_plural': '所有權部',
            },
        ),
        migrations.CreateModel(
            name='MarkingDepartmentPublicPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet1', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='共有部分')),
                ('sheet2', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='權利範圍')),
                ('sheet3', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='面積')),
                ('sheet4', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='其他登記事項')),
                ('sheet5', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='含停車位')),
                ('markingdepartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.markingdepartment')),
            ],
            options={
                'verbose_name': '標示部-共有部分',
                'verbose_name_plural': '標示部-共有部分',
            },
        ),
        migrations.CreateModel(
            name='MarkingDepartmentDependsLocationNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet1', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='建物坐落地號')),
                ('markingdepartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.markingdepartment')),
            ],
            options={
                'verbose_name': '標示部-建物坐落地號',
                'verbose_name_plural': '標示部-建物坐落地號',
            },
        ),
        migrations.CreateModel(
            name='MarkingDepartmentDependsBuildings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet1', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='附屬建物用途')),
                ('sheet2', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='面積')),
                ('markingdepartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.markingdepartment')),
            ],
            options={
                'verbose_name': '標示部-附屬建物',
                'verbose_name_plural': '標示部-附屬建物',
            },
        ),
    ]
