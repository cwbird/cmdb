# Generated by Django 2.2.7 on 2020-08-13 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assets', '0003_auto_20200813_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='单位名称')),
                ('region', models.SmallIntegerField(choices=[(0, '市级直属'), (1, '青羊区'), (2, '锦江区'), (3, '金牛区'), (4, '武侯区'), (5, '高新区'), (6, '天府新区'), (7, '成华区'), (8, '新都区'), (9, '温江区'), (10, '龙泉驿区'), (11, '青白江区'), (12, '金堂县'), (13, '双流区'), (14, '双流区'), (15, '新津区')], default=0, verbose_name='所属地区')),
                ('describe', models.TextField(blank=True, max_length=128, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name_plural': '所属单位',
            },
        ),
        migrations.CreateModel(
            name='Sysname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='系统名称')),
                ('yz_contact', models.CharField(blank=True, max_length=16, null=True, verbose_name='业主联系人')),
                ('yz_phone', models.CharField(blank=True, max_length=32, null=True, verbose_name='业主联系电话')),
                ('cjdw', models.CharField(blank=True, max_length=16, null=True, verbose_name='承建单位')),
                ('cj_contact', models.CharField(blank=True, max_length=16, null=True, verbose_name='承建联系人')),
                ('cj_phone', models.CharField(blank=True, max_length=32, null=True, verbose_name='承建联系电话')),
                ('describe', models.TextField(blank=True, max_length=128, null=True, verbose_name='备注')),
                ('entity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.Entity', verbose_name='所属单位')),
            ],
            options={
                'verbose_name_plural': '系统',
            },
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=64, unique=True, verbose_name='主机名')),
                ('ipadd', models.CharField(blank=True, max_length=32, null=True, unique=True, verbose_name='IP地址')),
                ('asset_type', models.CharField(choices=[('cloud_host', '云主机'), ('server', '物理机')], default='virtual_machine', max_length=64, verbose_name='资产类型')),
                ('status', models.SmallIntegerField(choices=[(0, '激活'), (1, '停用'), (2, '故障')], default=0, verbose_name='设备状态')),
                ('area', models.SmallIntegerField(choices=[(0, '互联网'), (1, '电子政务外网')], default=0, verbose_name='所属区域')),
                ('internet_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='互联网IP')),
                ('affairs_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='电子政务外网IP')),
                ('cpu', models.CharField(blank=True, max_length=60, null=True)),
                ('sys', models.CharField(blank=True, max_length=60, null=True, verbose_name='操作系统')),
                ('sys_disk', models.CharField(blank=True, max_length=60, null=True, verbose_name='系统盘')),
                ('Cloud_disk', models.CharField(blank=True, max_length=60, null=True, verbose_name='云盘')),
                ('memory', models.CharField(blank=True, max_length=60, null=True, verbose_name='内存')),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('utime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('comment', models.TextField(blank=True, default='', max_length=128, verbose_name='备注')),
                ('entity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.Entity', verbose_name='所属单位')),
                ('sysname', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.Sysname', verbose_name='系统名称')),
            ],
            options={
                'verbose_name_plural': '资产信息',
                'ordering': ['-ctime'],
            },
        ),
    ]