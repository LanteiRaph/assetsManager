# Generated by Django 4.0 on 2022-01-13 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_alter_requestdetails_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requestdetails',
            old_name='condition',
            new_name='request_detail',
        ),
    ]
