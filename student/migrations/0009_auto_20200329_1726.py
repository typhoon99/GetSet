# Generated by Django 2.2.11 on 2020-03-29 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20200328_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectgroup',
            name='guide',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Guide'),
        ),
    ]
