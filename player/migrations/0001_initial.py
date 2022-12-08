# Generated by Django 4.1.1 on 2022-12-08 00:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Name', help_text='name', max_length=255)),
                ('team', models.CharField(default='Team', help_text='team name', max_length=255)),
                ('Position', models.CharField(default='Position', help_text='Position', max_length=255)),
                ('Age', models.IntegerField()),
                ('data', models.TextField(default='information ')),
                ('image', models.TextField(default='add the path of picture')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'players',
                'ordering': ['pk'],
            },
        ),
    ]