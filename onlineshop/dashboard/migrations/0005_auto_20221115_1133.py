# Generated by Django 2.2.12 on 2022-11-15 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_barang_jenis_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jenis',
            old_name='nama',
            new_name='name',
        ),
    ]