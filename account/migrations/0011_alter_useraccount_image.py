# Generated by Django 5.0 on 2023-12-09 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_useraccount_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='image',
            field=models.FileField(default='images/account/profile.jpg', upload_to='images/account/'),
        ),
    ]
