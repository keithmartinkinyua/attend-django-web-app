# Generated by Django 3.0.8 on 2020-10-13 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attend_class_app', '0006_auto_20201013_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='unit_taken',
            field=models.ManyToManyField(related_name='units', to='attend_class_app.Units'),
        ),
    ]