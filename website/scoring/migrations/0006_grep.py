# Generated by Django 2.2 on 2019-02-11 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0005_auto_20190203_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='GREP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf', models.FileField(upload_to='')),
                ('ui', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoring.UI')),
            ],
        ),
    ]