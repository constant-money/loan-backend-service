# Generated by Django 2.1.4 on 2019-01-31 07:29

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('purpose', models.CharField(choices=[('email_connection', 'Email connection')], max_length=100)),
                ('language', models.CharField(blank=True, choices=[('en', 'English'), ('vi', 'Tiếng Việt')], max_length=20)),
                ('subject', models.CharField(max_length=500)),
                ('content', tinymce.models.HTMLField()),
            ],
            options={
                'verbose_name': 'Email Content',
                'verbose_name_plural': 'Email Contents',
            },
        ),
        migrations.CreateModel(
            name='SMSContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('purpose', models.CharField(choices=[('phone_verification', 'Phone verification')], max_length=100)),
                ('language', models.CharField(blank=True, choices=[('en', 'English'), ('vi', 'Tiếng Việt')], max_length=20)),
                ('content', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'SMS Content',
                'verbose_name_plural': 'SMS Contents',
            },
        ),
        migrations.AlterUniqueTogether(
            name='smscontent',
            unique_together={('purpose', 'language')},
        ),
        migrations.AlterUniqueTogether(
            name='emailcontent',
            unique_together={('purpose', 'language')},
        ),
    ]
