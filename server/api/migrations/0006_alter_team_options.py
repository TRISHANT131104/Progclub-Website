# Generated by Django 4.1.7 on 2023-03-17 15:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0005_team_delete_contact_alter_event_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="team",
            options={"verbose_name": "Member", "verbose_name_plural": "Team"},
        ),
    ]
