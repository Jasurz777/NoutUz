# Generated by Django 4.1 on 2022-08-17 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tg_Nout_uz', '0014_savat_priceproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='savat',
            name='name',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
