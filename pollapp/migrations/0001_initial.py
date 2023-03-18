# Generated by Django 4.1.6 on 2023-03-11 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('op1', models.CharField(max_length=40)),
                ('op2', models.CharField(max_length=40)),
                ('op3', models.CharField(max_length=40)),
                ('op1c', models.IntegerField(default=0)),
                ('op2c', models.IntegerField(default=0)),
                ('op3c', models.IntegerField(default=0)),
            ],
        ),
    ]
