# Generated by Django 2.0.3 on 2018-08-14 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20180814_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='repository',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]