# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Feed'
        db.create_table(u'aggregator_feed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('base_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('feed_url', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('favicon_ext', self.gf('django.db.models.fields.CharField')(default='ico', max_length=10)),
            ('uses_markdown', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('uses_titles', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('convert_newlines', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('category', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'aggregator', ['Feed'])

        # Adding model 'Post'
        db.create_table(u'aggregator_post', (
            ('post_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('feed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aggregator.Feed'])),
        ))
        db.send_create_signal(u'aggregator', ['Post'])

    def backwards(self, orm):
        # Deleting model 'Feed'
        db.delete_table(u'aggregator_feed')

        # Deleting model 'Post'
        db.delete_table(u'aggregator_post')

    models = {
        u'aggregator.feed': {
            'Meta': {'object_name': 'Feed'},
            'base_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'category': ('django.db.models.fields.SmallIntegerField', [], {}),
            'convert_newlines': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'favicon_ext': ('django.db.models.fields.CharField', [], {'default': "'ico'", 'max_length': '10'}),
            'feed_url': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'uses_markdown': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'uses_titles': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'aggregator.post': {
            'Meta': {'ordering': "['-updated']", 'object_name': 'Post'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['aggregator.Feed']"}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'post_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['aggregator']