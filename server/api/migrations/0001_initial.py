# Generated by Django 4.1.7 on 2023-03-20 11:46

import api.models
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("title", models.CharField(max_length=225, verbose_name="Event Title")),
                ("subtitle", models.CharField(max_length=225, verbose_name="Subtitle")),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Upcoming", "Upcoming"),
                            ("Ongoing", "Ongoing"),
                            ("Past", "Past"),
                        ],
                        max_length=225,
                        verbose_name="Type",
                    ),
                ),
                (
                    "image",
                    django_resized.forms.ResizedImageField(
                        crop=None,
                        force_format="WEBP",
                        keep_meta=True,
                        quality=100,
                        scale=None,
                        size=[1920, 1080],
                        upload_to=api.models.event_path,
                        verbose_name="Poster",
                    ),
                ),
            ],
            options={
                "verbose_name": "Event",
                "verbose_name_plural": "Events",
            },
        ),
        migrations.CreateModel(
            name="Project",
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
                (
                    "title",
                    models.CharField(max_length=225, verbose_name="Project Title"),
                ),
                ("domain", models.CharField(max_length=225, verbose_name="Domain")),
                ("category", models.CharField(max_length=225, verbose_name="Category")),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "image",
                    django_resized.forms.ResizedImageField(
                        crop=None,
                        force_format="WEBP",
                        keep_meta=True,
                        quality=100,
                        scale=None,
                        size=[1920, 1080],
                        upload_to=api.models.project_path,
                        verbose_name="Image",
                    ),
                ),
                ("github", models.URLField(verbose_name="Repository")),
            ],
            options={
                "verbose_name": "Project",
                "verbose_name_plural": "Projects",
                "ordering": ("-category",),
            },
        ),
        migrations.CreateModel(
            name="Team",
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
                ("name", models.CharField(max_length=225, verbose_name="Name")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("President", "President"),
                            ("Member", "Member"),
                            ("Volunteer", "Volunteer"),
                        ],
                        max_length=225,
                        verbose_name="Position",
                    ),
                ),
                (
                    "division",
                    models.CharField(
                        choices=[
                            ("Competitive Programming", "Competitive Programming"),
                            ("Cyber Security", "Cyber Security"),
                            ("Software Development", "Software Development"),
                        ],
                        max_length=225,
                        verbose_name="Division",
                    ),
                ),
                (
                    "year",
                    models.CharField(
                        choices=[
                            ("First", "First"),
                            ("Second", "Second"),
                            ("Third", "Third"),
                            ("Fourth", "Fourth"),
                        ],
                        max_length=10,
                        verbose_name="Year",
                    ),
                ),
                ("github", models.URLField(verbose_name="GitHub Profile")),
                ("codeforces", models.URLField(verbose_name="Codeforces Profile")),
                ("linkedin", models.URLField(verbose_name="LinkedIn Profile")),
                (
                    "image",
                    django_resized.forms.ResizedImageField(
                        crop=None,
                        force_format="WEBP",
                        keep_meta=True,
                        quality=100,
                        scale=None,
                        size=[1920, 1080],
                        upload_to=api.models.team_path,
                        verbose_name="Image",
                    ),
                ),
            ],
            options={
                "verbose_name": "Member",
                "verbose_name_plural": "Team",
            },
        ),
    ]
