# Generated by Django 2.1.5 on 2019-05-13 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_remove_notification_notification_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notification_recieved',
            field=models.BooleanField(default=False),
        ),
    ]