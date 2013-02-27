# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'StyleModifierPluginModel.font_family'
        db.add_column('cmsplugin_stylemodifierpluginmodel', 'font_family',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=64, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'StyleModifierPluginModel.font_family'
        db.delete_column('cmsplugin_stylemodifierpluginmodel', 'font_family')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 27, 0, 0)'}),
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
        'style_modifier.stylemodifierpluginmodel': {
            'Meta': {'object_name': 'StyleModifierPluginModel', 'db_table': "'cmsplugin_stylemodifierpluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            'background_color': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'background_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'bottom_gradient_color': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'font_family': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'freeform': ('django.db.models.fields.CharField', [], {'max_length': '96', 'blank': 'True'}),
            'mod_class': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'text_align': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'text_color': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'text_shadow': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'top_gradient_color': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'})
        }
    }

    complete_apps = ['style_modifier']