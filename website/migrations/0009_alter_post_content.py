# Generated by Django 3.2.12 on 2023-07-07 02:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20230705_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, max_length=8000),
        ),
    ]
