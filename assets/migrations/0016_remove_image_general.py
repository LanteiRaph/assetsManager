# Generated by Django 4.0 on 2022-01-20 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0015_situation_delete_condtition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='general',
        ),
    ]
