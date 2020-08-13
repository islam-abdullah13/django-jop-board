# Generated by Django 3.1 on 2020-08-13 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jop', '0011_auto_20200812_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='jop',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='job_owner', to='auth.user'),
            preserve_default=False,
        ),
    ]
