# Generated by Django 2.0.13 on 2020-11-16 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0011_auto_20201111_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsorship',
            name='for_modified_package',
            field=models.BooleanField(default=False),
        ),
    ]
