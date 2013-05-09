# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table('aggregator_post', (
            ('post_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('aggregator', ['Post'])

    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table('aggregator_post')

    models = {
        'aggregator.post': {
            'Meta': {'ordering': "['-updated']", 'object_name': 'Post'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'post_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['aggregator']