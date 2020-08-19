# Generated by Django 2.2.15 on 2020-08-05 00:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='producto',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]