# Generated by Django 2.1.4 on 2019-01-30 04:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0010_auto_20190130_0438'),
    ]

    operations = [
        migrations.AddField(
            model_name='loantermnotification',
            name='loan_term',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='loan_term_notifications', to='loan.LoanTerm'),
            preserve_default=False,
        ),
    ]
