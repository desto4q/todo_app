# Generated by Django 4.2.2 on 2023-06-12 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_item_compeleted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='compeleted',
            new_name='completed',
        ),
    ]