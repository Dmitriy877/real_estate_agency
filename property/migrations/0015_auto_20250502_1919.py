# Generated by Django 2.2.24 on 2025-05-02 16:19

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20250502_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, verbose_name='Нормализованный номер владельца'),
        ),
    ]
