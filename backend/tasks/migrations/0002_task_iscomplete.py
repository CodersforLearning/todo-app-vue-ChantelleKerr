# Generated by Django 3.2.9 on 2021-11-26 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='isComplete',
            field=models.BooleanField(default=False),
        ),
    ]