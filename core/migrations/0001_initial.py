# Generated by Django 5.0.1 on 2024-10-30 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='cases/images/')),
                ('progress', models.DecimalField(decimal_places=2, max_digits=5)),
                ('raised_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('goal_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]