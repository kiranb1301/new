# Generated by Django 5.0.2 on 2024-07-09 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0004_customuser_delete_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Mobile',
            field=models.BigIntegerField(null=True),
        ),
    ]