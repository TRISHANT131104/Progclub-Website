# Generated by Django 4.1.7 on 2023-03-09 07:14

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_event_subtitle_project_project_state_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="codeforces_profile_link",
        ),
        migrations.RemoveField(
            model_name="contact",
            name="github_profile_link",
        ),
        migrations.RemoveField(
            model_name="contact",
            name="linkedIn_profile_link",
        ),
        migrations.RemoveField(
            model_name="contact",
            name="message",
        ),
        migrations.RemoveField(
            model_name="event",
            name="event_type",
        ),
        migrations.RemoveField(
            model_name="project",
            name="git_repo_link",
        ),
        migrations.RemoveField(
            model_name="project",
            name="project_state",
        ),
        migrations.RemoveField(
            model_name="project",
            name="project_type",
        ),
        migrations.AddField(
            model_name="contact",
            name="codeforces",
            field=models.URLField(
                default="https://codeforces.com/", verbose_name="Codeforces Profile"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="contact",
            name="github",
            field=models.URLField(
                default="https://github.com/", verbose_name="GitHub Profile"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="contact",
            name="linkedin",
            field=models.URLField(
                default="https://www.linkedin.com/", verbose_name="LinkedIn Profile"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="event",
            name="type",
            field=models.CharField(
                choices=[
                    ("Upcoming", "Upcoming"),
                    ("Ongoing", "Ongoing"),
                    ("Past", "Past"),
                ],
                default="Past",
                max_length=225,
                verbose_name="Type",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="project",
            name="domain",
            field=models.CharField(
                default="Web Development", max_length=225, verbose_name="Domain"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="project",
            name="github",
            field=models.URLField(
                default="https://github.com/", verbose_name="Repository"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="contact",
            name="division",
            field=models.CharField(
                choices=[
                    ("Competitive Programming", "Competitive Programming"),
                    ("Cyber Security", "Cyber Security"),
                    ("Software Development", "Software Development"),
                ],
                max_length=225,
                verbose_name="Division",
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="Email"),
        ),
        migrations.AlterField(
            model_name="contact",
            name="name",
            field=models.CharField(max_length=225, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="contact",
            name="position",
            field=models.CharField(
                choices=[
                    ("President", "President"),
                    ("Member", "Member"),
                    ("Volunteer", "Volunteer"),
                ],
                max_length=225,
                verbose_name="Position",
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="year",
            field=models.CharField(
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
        migrations.AlterField(
            model_name="event",
            name="description",
            field=models.TextField(verbose_name="Description"),
        ),
        migrations.AlterField(
            model_name="event",
            name="image",
            field=models.ImageField(
                upload_to=api.models.blog_path, verbose_name="Poster"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="subtitle",
            field=models.CharField(max_length=225, verbose_name="Subtitle"),
        ),
        migrations.AlterField(
            model_name="event",
            name="title",
            field=models.CharField(max_length=225, verbose_name="Event Title"),
        ),
        migrations.AlterField(
            model_name="project",
            name="category",
            field=models.CharField(max_length=225, verbose_name="Category"),
        ),
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.TextField(verbose_name="Description"),
        ),
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(
                upload_to=api.models.project_path, verbose_name="Image"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="title",
            field=models.CharField(max_length=225, verbose_name="Project Title"),
        ),
    ]