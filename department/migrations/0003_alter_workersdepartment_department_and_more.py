# Generated by Django 4.1.5 on 2023-02-03 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_hodprofile_dob_alter_workersprofile_dob'),
        ('department', '0002_alter_workersdepartment_worker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workersdepartment',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
        migrations.AlterField(
            model_name='workersdepartment',
            name='worker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.workersprofile'),
        ),
    ]
