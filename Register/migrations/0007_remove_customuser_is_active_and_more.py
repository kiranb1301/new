# Generated by Django 5.0.2 on 2024-07-09 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0006_customuser_is_active_customuser_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_login',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Mobile',
            field=models.BigIntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Name',
            field=models.CharField(max_length=50),
        ),
    ]