# Generated by Django 3.2.12 on 2023-07-01 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20230624_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, max_length=8000),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
