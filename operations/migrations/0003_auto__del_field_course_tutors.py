# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Course.tutors'
        db.delete_column(u'operations_course', 'tutors')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Course.tutors'
        raise RuntimeError("Cannot reverse this migration. 'Course.tutors' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Course.tutors'
        db.add_column(u'operations_course', 'tutors',
                      self.gf('django.db.models.fields.TextField')(),
                      keep_default=False)


    models = {
        u'operations.course': {
            'Meta': {'object_name': 'Course'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'testimonial': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['operations']