# Generated by Django 3.2.4 on 2023-09-21 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_batchtiming_mylecturs_studentbatch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mylecturs',
            name='video_batch',
        ),
        migrations.RemoveField(
            model_name='mylecturs',
            name='video_category',
        ),
        migrations.DeleteModel(
            name='batchtiming',
        ),
        migrations.DeleteModel(
            name='category',
        ),
        migrations.DeleteModel(
            name='mylecturs',
        ),
        migrations.DeleteModel(
            name='studentbatch',
        ),
    ]
