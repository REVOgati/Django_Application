# Generated by Django 5.1.3 on 2024-11-05 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoitem',
            old_name='name',
            new_name='title',
        ),
    ]