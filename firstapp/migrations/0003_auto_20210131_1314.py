# Generated by Django 3.1.5 on 2021-01-31 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_book_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta', models.CharField(max_length=100)),
                ('apps', models.CharField(max_length=100)),
                ('playlist', models.CharField(max_length=100)),
                ('jobtype', models.CharField(choices=[{'debug': 'debug', 'standard': 'standard'}], max_length=10)),
                ('sp', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]