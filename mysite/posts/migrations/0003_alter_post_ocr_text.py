# Generated by Django 4.0.6 on 2022-07-23 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_ocr_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ocr_text',
            field=models.TextField(default=''),
        ),
    ]
