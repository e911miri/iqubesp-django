# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StudentTestimony'
        db.create_table(u'operations_studenttestimony', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('testimony', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'operations', ['StudentTestimony'])


    def backwards(self, orm):
        # Deleting model 'StudentTestimony'
        db.delete_table(u'operations_studenttestimony')


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
        },
        u'operations.studenttestimony': {
            'Meta': {'object_name': 'StudentTestimony'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'testimony': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['operations']