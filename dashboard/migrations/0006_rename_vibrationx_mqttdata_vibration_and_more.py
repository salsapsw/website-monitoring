# Generated by Django 4.2.6 on 2023-12-12 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_rename_vibration_mqttdata_vibrationx_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mqttdata',
            old_name='vibrationx',
            new_name='vibration',
        ),
        migrations.RemoveField(
            model_name='mqttdata',
            name='vibrationy',
        ),
        migrations.RemoveField(
            model_name='mqttdata',
            name='vibrationz',
        ),
    ]
