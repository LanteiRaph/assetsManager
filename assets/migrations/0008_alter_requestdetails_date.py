# Generated by Django 4.0 on 2022-01-14 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_alter_requestdetails_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestdetails',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
