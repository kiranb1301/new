# Generated by Django 5.0.2 on 2024-07-09 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0007_remove_customuser_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Mobile',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
