# Generated by Django 3.2.4 on 2021-07-13 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Console',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
                ('consolemodel', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('released_year', models.IntegerField()),
            ],
        ),
    ]
