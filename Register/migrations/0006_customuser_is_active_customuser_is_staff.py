# Generated by Django 5.0.2 on 2024-07-09 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0005_alter_customuser_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
