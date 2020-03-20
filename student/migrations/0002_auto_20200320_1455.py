# Generated by Django 2.2.11 on 2020-03-20 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(default='NotFilled', max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='cgpa',
            field=models.IntegerField(default=0),
        ),
    ]
