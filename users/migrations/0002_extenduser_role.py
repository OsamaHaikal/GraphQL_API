# Generated by Django 3.2.9 on 2021-12-06 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extenduser',
            name='role',
            field=models.CharField(choices=[('user', 'user'), ('manager', 'manager')], default='user', max_length=120),
        ),
    ]
