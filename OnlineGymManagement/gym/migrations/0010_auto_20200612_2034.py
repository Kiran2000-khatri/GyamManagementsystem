# Generated by Django 2.2.6 on 2020-06-12 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0009_auto_20200612_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='batch',
        ),
        migrations.AddField(
            model_name='attendance',
            name='activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Activity'),
        ),
    ]
