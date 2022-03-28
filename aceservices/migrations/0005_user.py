# Generated by Django 3.1.7 on 2021-05-16 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aceservices', '0004_auto_20210516_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=30)),
                ('phoneno', models.CharField(default='', max_length=10)),
                ('password', models.CharField(default='', max_length=20)),
                ('cpassword', models.CharField(default='', max_length=20)),
            ],
        ),
    ]