# Generated by Django 3.2.11 on 2022-03-08 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0009_rename_fund_fund_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.FloatField(default=500),
        ),
        migrations.DeleteModel(
            name='Fund',
        ),
    ]
