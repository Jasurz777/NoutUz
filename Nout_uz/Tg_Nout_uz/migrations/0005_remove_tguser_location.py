# Generated by Django 4.1 on 2022-08-15 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tg_Nout_uz', '0004_tguser_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tguser',
            name='location',
        ),
    ]
