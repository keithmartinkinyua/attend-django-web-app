# Generated by Django 3.0.8 on 2020-10-13 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attend_class_app', '0007_auto_20201013_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='unit_taken',
        ),
        migrations.AddField(
            model_name='class',
            name='unit_taken',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='attend_class_app.Units'),
            preserve_default=False,
        ),
    ]
