# Generated by Django 2.2.11 on 2020-03-29 13:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20200329_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='createdOn',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
