# Generated by Django 4.1.6 on 2023-02-08 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Members",
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
                ("fname", models.TextField(max_length=20)),
                ("lname", models.TextField(max_length=20)),
                ("email", models.EmailField(max_length=100)),
                ("telephone", models.BigIntegerField(max_length=50)),
                ("role", models.CharField(max_length=50)),
            ],
        ),
    ]