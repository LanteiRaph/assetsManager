# Generated by Django 4.0 on 2022-01-14 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_rename_condition_requestdetails_request_detail'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='requestdetails',
            unique_together={('equipment', 'date')},
        ),
    ]