# Generated by Django 3.1.2 on 2020-11-19 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trainers', '0005_auto_20201119_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('skill', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=120)),
                ('firstname', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=120)),
            ],
        ),
    ]
