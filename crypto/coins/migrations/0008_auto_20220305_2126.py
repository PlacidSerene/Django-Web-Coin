# Generated by Django 3.2.11 on 2022-03-06 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0007_auto_20220302_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='fund',
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund', models.FloatField(default=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fund', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
