# Generated by Django 4.2.14 on 2024-08-04 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0008_remove_mailing_actual_end_time_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="mailing",
            name="actual_end_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="mailing",
            name="actual_start_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
