# Generated by Django 4.0 on 2022-01-17 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0010_rename_requestdetails_requestdetail'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='requestdetail',
            table='request_detail',
        ),
    ]
