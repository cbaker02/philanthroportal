# Generated by Django 5.0.3 on 2024-04-08 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_grantapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grantapplication',
            name='status_changed',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
