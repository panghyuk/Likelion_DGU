# Generated by Django 3.2 on 2022-01-25 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0004_alter_homework_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
