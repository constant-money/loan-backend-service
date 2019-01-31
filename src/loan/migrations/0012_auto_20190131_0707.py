# Generated by Django 2.1.4 on 2019-01-31 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0011_loantermnotification_loan_term'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanTermBusiness',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('loan.loanterm',),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('pending', 'Pending'), ('processing', 'Processing'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('cancelled', 'Cancelled'), ('closed', 'Closed')], default='created', max_length=50),
        ),
        migrations.AlterField(
            model_name='loanmemberapplication',
            name='status',
            field=models.CharField(choices=[('connecting', 'Connecting'), ('connected', 'Connected'), ('disconnected', 'Disconnected')], max_length=50, null=True),
        ),
    ]
