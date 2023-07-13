# Generated by Django 3.2.12 on 2023-06-08 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_post_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
