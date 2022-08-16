# Generated by Django 2.2 on 2022-08-15 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_employee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='app.Team'),
        ),
    ]
