# Generated by Django 4.1.6 on 2023-03-15 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0002_poll_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='creator',
        ),
    ]