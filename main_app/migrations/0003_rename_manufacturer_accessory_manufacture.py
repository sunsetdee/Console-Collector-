# Generated by Django 3.2.4 on 2021-07-15 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_accessory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessory',
            old_name='manufacturer',
            new_name='manufacture',
        ),
    ]
