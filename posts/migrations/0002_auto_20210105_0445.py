# Generated by Django 3.1.4 on 2021-01-04 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set(),
        ),
    ]
