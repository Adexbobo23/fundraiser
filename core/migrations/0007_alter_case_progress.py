# Generated by Django 5.1.2 on 2024-11-16 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_case_beneficiary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='progress',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
