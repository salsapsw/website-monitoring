# Generated by Django 4.2.3 on 2023-10-11 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0002_alter_monitoringupperandlower_current_upper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoringupperandlower',
            name='current_upper',
            field=models.IntegerField(default=1000),
        ),
    ]
