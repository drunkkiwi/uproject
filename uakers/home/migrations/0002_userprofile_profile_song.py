# Generated by Django 2.1.4 on 2019-01-14 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_song',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
