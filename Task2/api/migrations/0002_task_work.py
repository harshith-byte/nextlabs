# Generated by Django 3.2.16 on 2023-03-09 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='work',
            field=models.CharField(choices=[('pending', 'pending'), ('completed', 'completed')], default='pending', max_length=10),
        ),
    ]
