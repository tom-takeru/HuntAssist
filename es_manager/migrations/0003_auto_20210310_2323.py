# Generated by Django 2.2.5 on 2021-03-10 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('es_manager', '0002_auto_20210310_1832'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrysheet',
            old_name='user_id',
            new_name='user',
        ),
    ]
