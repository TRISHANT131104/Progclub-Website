# Generated by Django 4.1.7 on 2023-07-15 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_event_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram Profile'),
        ),
        migrations.AddField(
            model_name='team',
            name='phone_number',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='event',
            name='subtitle',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='Subtitle'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='Event Title'),
        ),
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(blank=True, choices=[('aUpcoming', 'Upcoming'), ('bOngoing', 'Ongoing'), ('cPast', 'Past')], max_length=225, null=True, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='domain',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='Domain'),
        ),
        migrations.AlterField(
            model_name='project',
            name='github',
            field=models.URLField(blank=True, null=True, verbose_name='Repository'),
        ),
        migrations.AlterField(
            model_name='project',
            name='subtitle',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='Project Subtitle'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='Project Title'),
        ),
        migrations.AlterField(
            model_name='team',
            name='codeforces',
            field=models.URLField(blank=True, null=True, verbose_name='Codeforces Profile'),
        ),
        migrations.AlterField(
            model_name='team',
            name='division',
            field=models.CharField(blank=True, choices=[('aCompetitive Programming', 'Competitive Programming'), ('cCyber Security', 'Cyber Security'), ('bSoftware Development', 'Software Development')], max_length=225, null=True, verbose_name='Division'),
        ),
        migrations.AlterField(
            model_name='team',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='team',
            name='github',
            field=models.URLField(blank=True, null=True, verbose_name='GitHub Profile'),
        ),
        migrations.AlterField(
            model_name='team',
            name='linkedin',
            field=models.URLField(blank=True, null=True, verbose_name='LinkedIn Profile'),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='team',
            name='position',
            field=models.CharField(blank=True, choices=[('aPresident', 'President'), ('bMember', 'Member'), ('cVolunteer', 'Volunteer')], max_length=225, null=True, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='team',
            name='year',
            field=models.CharField(blank=True, choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth')], max_length=10, null=True, verbose_name='Year'),
        ),
    ]
