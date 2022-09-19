# Generated by Django 4.1.1 on 2022-09-19 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ingredients",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("unit", models.CharField(max_length=100)),
                ("food", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Stats",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("calories", models.PositiveSmallIntegerField()),
                ("daily_carbs", models.PositiveSmallIntegerField()),
                ("daily_protein", models.PositiveSmallIntegerField()),
                ("daily_fats", models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Steps",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("picture_url", models.URLField(max_length=1000)),
                ("description", models.CharField(max_length=2500)),
                ("calories", models.PositiveSmallIntegerField()),
                ("carbs", models.PositiveSmallIntegerField()),
                ("protein", models.PositiveSmallIntegerField()),
                ("fats", models.PositiveSmallIntegerField()),
                (
                    "ingredients",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="recipe",
                        to="macros.ingredients",
                    ),
                ),
                (
                    "steps",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="recipe",
                        to="macros.steps",
                    ),
                ),
            ],
        ),
    ]
