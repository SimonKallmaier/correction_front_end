# Generated by Django 4.0.6 on 2022-07-23 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ocr_text',
            field=models.TextField(default=None),
        ),
    ]
