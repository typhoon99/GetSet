# Generated by Django 2.2.11 on 2020-03-28 11:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20200328_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectgroup',
            name='createdOn',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
