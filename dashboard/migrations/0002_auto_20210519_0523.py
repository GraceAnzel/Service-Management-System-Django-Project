# Generated by Django 3.1.7 on 2021-05-18 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Mobiles', 'Mobiles'), ('Computers', 'Computers'), ('AC', 'AC')], max_length=50, null=True),
        ),
    ]
