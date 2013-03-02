# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FacebookButtonPluginModel'
        db.create_table('cmsplugin_facebookbuttonpluginmodel', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('layout', self.gf('django.db.models.fields.CharField')(default='standard', max_length=50)),
            ('url', self.gf('django.db.models.fields.CharField')(default='http://', max_length=255, blank=True)),
            ('send', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('show_faces', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None, null=True, blank=True)),
            ('verb', self.gf('django.db.models.fields.CharField')(default='like', max_length=50)),
            ('font', self.gf('django.db.models.fields.CharField')(default='verdana', max_length=50)),
            ('color_scheme', self.gf('django.db.models.fields.CharField')(default='light', max_length=50)),
        ))
        db.send_create_signal('facebook_button', ['FacebookButtonPluginModel'])


    def backwards(self, orm):
        # Deleting model 'FacebookButtonPluginModel'
        db.delete_table('cmsplugin_facebookbuttonpluginmodel')


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
        'facebook-button.facebookbuttonpluginmodel': {
            'Meta': {'object_name': 'FacebookButtonPluginModel', 'db_table': "'cmsplugin_facebookbuttonpluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'color_scheme': ('django.db.models.fields.CharField', [], {'default': "'light'", 'max_length': '50'}),
            'font': ('django.db.models.fields.CharField', [], {'default': "'verdana'", 'max_length': '50'}),
            'layout': ('django.db.models.fields.CharField', [], {'default': "'standard'", 'max_length': '50'}),
            'send': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_faces': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "'http://'", 'max_length': '255', 'blank': 'True'}),
            'verb': ('django.db.models.fields.CharField', [], {'default': "'like'", 'max_length': '50'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['facebook_button']
