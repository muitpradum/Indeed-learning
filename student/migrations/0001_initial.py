# Generated by Django 3.2.4 on 2023-09-17 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mysoftware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('software_title', models.CharField(max_length=100, null=True)),
                ('software_description', models.TextField(null=True)),
                ('software_picture', models.ImageField(null=True, upload_to='static/softwarepic/')),
                ('software_date', models.DateField()),
            ],
        ),
    ]
