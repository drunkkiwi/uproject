# Generated by Django 2.1.4 on 2019-01-25 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_userprofile_profile_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_nickname',
            field=models.CharField(max_length=250),
        ),
    ]