# Generated by Django 3.1 on 2020-08-06 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0003_jop_jop_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='jop',
            name='experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='jop',
            name='published_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='jop',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jop',
            name='vacancy',
            field=models.IntegerField(default=1),
        ),
    ]