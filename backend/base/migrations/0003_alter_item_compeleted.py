# Generated by Django 4.2.2 on 2023-06-12 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_item_compeleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='compeleted',
            field=models.BooleanField(default=False),
        ),
    ]