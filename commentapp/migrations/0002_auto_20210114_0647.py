# Generated by Django 3.1.5 on 2021-01-14 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commentapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='cotent',
            new_name='content',
        ),
    ]
