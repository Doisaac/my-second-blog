# Generated by Django 2.2.15 on 2020-08-05 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200804_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='published_date',
        ),
    ]
