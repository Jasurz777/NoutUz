# Generated by Django 4.1 on 2022-08-17 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tg_Nout_uz', '0013_remove_product_logo_remove_tguser_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='savat',
            name='priceproduct',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
