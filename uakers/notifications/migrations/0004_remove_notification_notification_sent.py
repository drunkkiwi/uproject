# Generated by Django 2.1.5 on 2019-02-09 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_notification_notification_target'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='notification_sent',
        ),
    ]