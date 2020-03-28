# Generated by Django 2.2.11 on 2020-03-28 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20200328_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectgroup',
            name='user1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projectgroup',
            name='user2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projectgroup',
            name='user3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member3', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projectgroup',
            name='user4',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member4', to=settings.AUTH_USER_MODEL),
        ),
    ]
