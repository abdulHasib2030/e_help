# Generated by Django 5.0 on 2023-12-09 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='pincode',
            field=models.CharField(max_length=100),
        ),
    ]
