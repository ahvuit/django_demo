# Generated by Django 4.2.7 on 2023-12-01 07:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="myapp",
            name="joined_date",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="myapp",
            name="phone",
            field=models.CharField(max_length=11, null=True),
        ),
    ]
