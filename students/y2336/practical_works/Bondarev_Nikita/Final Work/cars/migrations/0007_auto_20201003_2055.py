# Generated by Django 3.1.2 on 2020-10-03 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_auto_20201003_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientuser',
            name='licence',
        ),
        migrations.AddField(
            model_name='license',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]