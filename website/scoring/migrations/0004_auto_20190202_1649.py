# Generated by Django 2.1.5 on 2019-02-02 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0003_file_is_ok'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ui',
            name='img',
            field=models.FileField(upload_to=''),
        ),
    ]
