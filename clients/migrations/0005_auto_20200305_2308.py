# Generated by Django 3.0.3 on 2020-03-05 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default_profile.jpg', null=True, upload_to=''),
        ),
    ]
