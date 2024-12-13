# Generated by Django 5.1.3 on 2024-12-13 08:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0009_alter_usertable_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingdtable',
            name='Username',
        ),
        migrations.AddField(
            model_name='bookingdtable',
            name='USER',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='administrator.usertable'),
            preserve_default=False,
        ),
    ]