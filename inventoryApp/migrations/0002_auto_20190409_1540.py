# Generated by Django 2.2 on 2019-04-09 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='author',
            new_name='readlink',
        ),
    ]
