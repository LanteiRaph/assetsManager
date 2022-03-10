# Generated by Django 4.0 on 2022-01-10 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assets', '0001_initial'),
        ('onboarding', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestlist',
            name='user',
            field=models.ForeignKey(blank=True, db_column='user', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='onboarding.user'),
        ),
        migrations.AddField(
            model_name='image',
            name='equipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.equipment'),
        ),
        migrations.AddField(
            model_name='image',
            name='general',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.general'),
        ),
        migrations.AddField(
            model_name='general',
            name='make',
            field=models.ForeignKey(db_column='make', on_delete=django.db.models.deletion.DO_NOTHING, to='assets.make'),
        ),
        migrations.AddField(
            model_name='general',
            name='request',
            field=models.ForeignKey(blank=True, db_column='request', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='assets.requestlist'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='make',
            field=models.ForeignKey(db_column='make', on_delete=django.db.models.deletion.DO_NOTHING, to='assets.make'),
        ),
        migrations.AddField(
            model_name='condition',
            name='equipment',
            field=models.ForeignKey(blank=True, db_column='equipment', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='assets.equipment'),
        ),
        migrations.AddField(
            model_name='condition',
            name='request',
            field=models.ForeignKey(blank=True, db_column='request', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='assets.requestlist'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='department',
            field=models.ForeignKey(blank=True, db_column='department', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='onboarding.department'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='equipment',
            field=models.ForeignKey(blank=True, db_column='equipment', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='assets.equipment'),
        ),
        migrations.AlterUniqueTogether(
            name='state',
            unique_together={('date', 'taken')},
        ),
        migrations.AlterUniqueTogether(
            name='requestlist',
            unique_together={('date_out', 'date_in')},
        ),
        migrations.AlterUniqueTogether(
            name='general',
            unique_together={('name', 'make')},
        ),
        migrations.AlterUniqueTogether(
            name='equipment',
            unique_together={('serial_num', 'make')},
        ),
        migrations.AlterUniqueTogether(
            name='condition',
            unique_together={('request', 'date')},
        ),
        migrations.AlterUniqueTogether(
            name='assignment',
            unique_together={('is_valid', 'department', 'equipment')},
        ),
    ]