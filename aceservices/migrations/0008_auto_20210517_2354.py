# Generated by Django 3.1.7 on 2021-05-17 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aceservices', '0007_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add',
            name='city',
        ),
        migrations.RemoveField(
            model_name='add',
            name='street',
        ),
        migrations.AlterField(
            model_name='add',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
    ]