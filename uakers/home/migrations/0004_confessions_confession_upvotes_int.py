# Generated by Django 2.1.4 on 2019-01-03 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190103_0331'),
    ]

    operations = [
        migrations.AddField(
            model_name='confessions',
            name='confession_upvotes_int',
            field=models.IntegerField(default=0),
        ),
    ]