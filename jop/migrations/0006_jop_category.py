# Generated by Django 3.1 on 2020-08-06 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='jop',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jop.category'),
            preserve_default=False,
        ),
    ]
