# Generated by Django 4.0.6 on 2022-07-28 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0006_remove_department_unique_member'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='department',
            constraint=models.UniqueConstraint(fields=('name', 'status'), name='unique_member'),
        ),
    ]
