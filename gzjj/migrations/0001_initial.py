# Generated by Django 2.2.7 on 2020-08-17 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gzjj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='交接人员')),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('utime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('text', models.TextField(blank=True, max_length=128, null=True, verbose_name='交接内容')),
            ],
            options={
                'verbose_name_plural': '工作交接',
            },
        ),
    ]
