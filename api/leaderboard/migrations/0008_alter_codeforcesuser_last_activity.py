# Generated by Django 5.1.5 on 2025-02-18 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("leaderboard", "0007_alter_codeforcesuser_last_activity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="codeforcesuser",
            name="last_activity",
            field=models.BigIntegerField(default=1739902669.24653),
        ),
    ]
