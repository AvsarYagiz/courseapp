# Generated by Django 3.2.9 on 2023-11-07 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20231107_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='isCat3',
            field=models.BooleanField(default=False),
        ),
    ]