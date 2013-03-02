# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TwitterButtonPluginModel'
        db.create_table('cmsplugin_twitterbuttonpluginmodel', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('tweet_text', self.gf('django.db.models.fields.CharField')(default=None, max_length=60, blank=True)),
            ('hash_tag', self.gf('django.db.models.fields.CharField')(default=None, max_length=60, blank=True)),
            ('large_button', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('twitter_button', ['TwitterButtonPluginModel'])


    def backwards(self, orm):
        # Deleting model 'TwitterButtonPluginModel'
        db.delete_table('cmsplugin_twitterbuttonpluginmodel')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 25, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'twitter-button.twitterbuttonpluginmodel': {
            'Meta': {'object_name': 'TwitterButtonPluginModel', 'db_table': "'cmsplugin_twitterbuttonpluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'hash_tag': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'large_button': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tweet_text': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'})
        }
    }

    complete_apps = ['twitter_button']
