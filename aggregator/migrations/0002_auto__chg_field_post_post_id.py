# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Post.post_id'
        db.alter_column('aggregator_post', 'post_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255))


    def backwards(self, orm):
        
        # Changing field 'Post.post_id'
        db.alter_column('aggregator_post', 'post_id', self.gf('django.db.models.fields.CharField')(max_length=500, unique=True))


    models = {
        'aggregator.feed': {
            'Meta': {'ordering': "['-updated']", 'object_name': 'Feed'},
            'base_url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'br2nl': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'favicon_ext': ('django.db.models.fields.CharField', [], {'default': "'png'", 'max_length': '4'}),
            'feed_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'profile_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'uses_title': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'with_markdown': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'aggregator.post': {
            'Meta': {'ordering': "['-updated']", 'object_name': 'Post'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aggregator.Feed']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'remote_url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['aggregator']
