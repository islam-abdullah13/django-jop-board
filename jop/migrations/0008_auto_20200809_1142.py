# Generated by Django 3.1 on 2020-08-09 09:42

from django.db import migrations, models
import jop.models


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0007_jop_jop_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jop',
            name='jop_image',
            field=models.ImageField(default='', upload_to=jop.models.image_upload),
        ),
    ]