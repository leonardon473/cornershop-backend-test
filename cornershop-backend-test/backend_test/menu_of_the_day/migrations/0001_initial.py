# Generated by Django 3.0.8 on 2021-11-24 07:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=140)),
                ("slack_id", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="MenuOfTheDay",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="FoodDish",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("food", models.CharField(max_length=140)),
                (
                    "menu_of_the_day",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="menu_of_the_day.MenuOfTheDay",
                        related_name="food_dishes",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EmployeeMenuSelection",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="menu_of_the_day.Employee",
                    ),
                ),
                (
                    "food_dish",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="menu_of_the_day.FoodDish",
                    ),
                ),
                (
                    "menu_of_the_day",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="menu_of_the_day.MenuOfTheDay",
                    ),
                ),
            ],
        ),
    ]
