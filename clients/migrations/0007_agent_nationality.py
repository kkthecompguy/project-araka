# Generated by Django 3.0.3 on 2020-03-07 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_auto_20200307_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='nationality',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
