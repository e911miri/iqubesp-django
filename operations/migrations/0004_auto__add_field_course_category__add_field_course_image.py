# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Course.category'
        db.add_column(u'operations_course', 'category',
                      self.gf('django.db.models.fields.CharField')(default='Web', max_length=10),
                      keep_default=False)

        # Adding field 'Course.image'
        db.add_column(u'operations_course', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Course.category'
        db.delete_column(u'operations_course', 'category')

        # Deleting field 'Course.image'
        db.delete_column(u'operations_course', 'image')


    models = {
        u'operations.course': {
            'Meta': {'object_name': 'Course'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'testimonial': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['operations']