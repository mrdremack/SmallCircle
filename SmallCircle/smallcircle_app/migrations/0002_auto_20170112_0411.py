# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 04:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('smallcircle_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('audio', embed_video.fields.EmbedVideoField(blank=True)),
                ('artist', models.CharField(blank=True, max_length=128)),
                ('song', models.CharField(blank=True, max_length=128)),
                ('photo', models.ImageField(blank=True, upload_to='posts')),
                ('img_alt', models.CharField(blank=True, max_length=128)),
                ('quote', models.TextField(blank=True)),
                ('quoter', models.CharField(blank=True, max_length=128)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('video', embed_video.fields.EmbedVideoField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.RemoveField(
            model_name='audio',
            name='user',
        ),
        migrations.RemoveField(
            model_name='miscellaneous',
            name='user',
        ),
        migrations.RemoveField(
            model_name='page',
            name='category',
        ),
        migrations.RemoveField(
            model_name='page',
            name='user',
        ),
        migrations.RemoveField(
            model_name='photos',
            name='user',
        ),
        migrations.RemoveField(
            model_name='quotes',
            name='user',
        ),
        migrations.RemoveField(
            model_name='videos',
            name='user',
        ),
        migrations.RemoveField(
            model_name='category',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
        migrations.DeleteModel(
            name='Audio',
        ),
        migrations.DeleteModel(
            name='Miscellaneous',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.DeleteModel(
            name='Photos',
        ),
        migrations.DeleteModel(
            name='Quotes',
        ),
        migrations.DeleteModel(
            name='Videos',
        ),
        migrations.AddField(
            model_name='media',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smallcircle_app.Category'),
        ),
        migrations.AddField(
            model_name='media',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]