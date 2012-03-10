# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Feed'
        db.create_table('aggregator_feed', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('base_url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('feed_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('profile_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('favicon_ext', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('uses_title', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('br2nl', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('aggregator', ['Feed'])

        # Adding model 'Post'
        db.create_table('aggregator_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=500)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('remote_url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('feed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aggregator.Feed'])),
        ))
        db.send_create_signal('aggregator', ['Post'])


    def backwards(self, orm):
        
        # Deleting model 'Feed'
        db.delete_table('aggregator_feed')

        # Deleting model 'Post'
        db.delete_table('aggregator_post')


    models = {
        'aggregator.feed': {
            'Meta': {'object_name': 'Feed'},
            'base_url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'br2nl': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'favicon_ext': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'feed_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'profile_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'uses_title': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'aggregator.post': {
            'Meta': {'object_name': 'Post'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aggregator.Feed']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '500'}),
            'remote_url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['aggregator']
