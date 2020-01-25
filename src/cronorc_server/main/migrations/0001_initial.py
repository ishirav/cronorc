# Generated by Django 3.0.2 on 2020-01-24 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(db_index=True, max_length=255)),
                ('ip', models.GenericIPAddressField()),
                ('command', models.TextField(db_index=True)),
            ],
            options={
                'unique_together': {('hostname', 'ip', 'command')},
            },
        ),
        migrations.CreateModel(
            name='Execution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('elapsed', models.BigIntegerField()),
                ('exit_code', models.IntegerField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Job')),
            ],
        ),
    ]
