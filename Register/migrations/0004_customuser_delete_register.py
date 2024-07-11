# Generated by Django 5.0.2 on 2024-07-09 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0003_alter_register_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('Name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('Mobile', models.BigIntegerField()),
                ('password', models.CharField(max_length=50)),
                ('Re_Enter_password', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
