# Generated by Django 2.2.3 on 2019-07-21 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vk_api_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paramsmodel',
            name='group_id',
            field=models.IntegerField(verbose_name='Group_id'),
        ),
    ]
