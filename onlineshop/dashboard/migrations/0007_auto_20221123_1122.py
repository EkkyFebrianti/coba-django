# Generated by Django 2.2.12 on 2022-11-23 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='tahun_gabung',
            field=models.CharField(max_length=10),
        ),
    ]
