# Generated by Django 2.2.9 on 2020-01-25 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_job_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='last_execution',
            field=models.DateTimeField(null=True),
        ),
    ]