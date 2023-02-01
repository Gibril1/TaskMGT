# Generated by Django 4.1.5 on 2023-02-01 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_workersdepartment_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='progress',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
