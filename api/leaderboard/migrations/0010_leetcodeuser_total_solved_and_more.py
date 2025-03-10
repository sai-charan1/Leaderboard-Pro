# Generated by Django 5.1.5 on 2025-02-20 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("leaderboard", "0009_codeforcesuser_total_solved_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="leetcodeuser",
            name="total_solved",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="codeforcesuser",
            name="last_activity",
            field=models.BigIntegerField(default=1740068943.875184),
        ),
    ]
