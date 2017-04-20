# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-04-20 08:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('objects', '0005_auto_20150403_2339'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('typeclasses', '0008_auto_20170420_0811'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_key', models.CharField(db_index=True, max_length=255, verbose_name=b'key')),
                ('db_typeclass_path', models.CharField(help_text=b"this defines what 'type' of entity this is. This variable holds a Python path to a module with a valid Evennia Typeclass.", max_length=255, null=True, verbose_name=b'typeclass')),
                ('db_date_created', models.DateTimeField(auto_now_add=True, verbose_name=b'creation date')),
                ('db_lock_storage', models.TextField(blank=True, help_text=b"locks limit access to an entity. A lock is defined as a 'lock string' on the form 'type:lockfunctions', defining what functionality is locked and how to determine access. Not defining a lock means no access is granted.", verbose_name=b'locks')),
                ('db_expiry_maxposts', models.IntegerField(blank=True, help_text='Maximum number of active/visible posts for this board.', null=True, verbose_name='max_posts')),
                ('db_expiry_duration', models.IntegerField(blank=True, help_text='Maximum timeline in days for posts to live on this board.', null=True, verbose_name='lifetime_days')),
                ('db_attributes', models.ManyToManyField(help_text=b'attributes on this object. An attribute can hold any pickle-able python object (see docs for special cases).', null=True, to='typeclasses.Attribute')),
                ('db_subscriptions', models.ManyToManyField(blank=True, help_text='Players subscribed to this board.', related_name='board_subscriptions', to=settings.AUTH_USER_MODEL, verbose_name='subscribers')),
                ('db_tags', models.ManyToManyField(help_text=b'tags on this object. Tags are simple string markers to identify, group and alias objects.', null=True, to='typeclasses.Tag')),
            ],
            options={
                'verbose_name': 'Board',
                'verbose_name_plural': 'Boards',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_poster_name', models.CharField(help_text='Poster display name.', max_length=40, verbose_name='poster')),
                ('db_subject', models.CharField(help_text='Subject of post.', max_length=40, verbose_name='subject')),
                ('db_date_created', models.DateTimeField(auto_now_add=True, db_index=True, help_text='Date post was made.', verbose_name='date created')),
                ('db_pinned', models.BooleanField(help_text='Should the post remain visible even after expiration?', verbose_name='pinned')),
                ('db_text', models.TextField(blank=True, help_text='Text of the post.', null=True, verbose_name='post_text')),
                ('db_board', models.ForeignKey(help_text='Board this post is on.', on_delete=django.db.models.deletion.CASCADE, to='paxboards.BoardDB', verbose_name='board')),
                ('db_parent', models.ForeignKey(blank=True, help_text='Parent/child map for threaded replies.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='paxboards.Post', verbose_name='parent')),
                ('db_poster_object', models.ForeignKey(blank=True, help_text='Post origin (if object),', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='objects.ObjectDB', verbose_name='poster(object)')),
                ('db_poster_player', models.ForeignKey(blank=True, help_text='Post origin (if player).', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='poster(player)')),
                ('db_readers', models.ManyToManyField(blank=True, help_text='Players who have read this post.', null=True, related_name='read_posts', to=settings.AUTH_USER_MODEL, verbose_name='readers')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
