# Generated by Django 5.0 on 2023-12-09 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_useraccount_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='image',
            field=models.ImageField(default='images/account/profile.jpg', upload_to='images/account/'),
        ),
    ]
