# Generated by Django 2.2.7 on 2020-08-17 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gzjj', '0002_gzjj_stat'),
    ]

    operations = [
        migrations.AddField(
            model_name='gzjj',
            name='beizhu',
            field=models.TextField(blank=True, max_length=128, null=True, verbose_name='备注'),
        ),
    ]
