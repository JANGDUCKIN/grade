# Generated by Django 2.1.5 on 2019-02-13 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0006_grep'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='file',
            name='ui',
        ),
        migrations.RemoveField(
            model_name='grep',
            name='ui',
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='GREP',
        ),
        migrations.DeleteModel(
            name='UI',
        ),
    ]
