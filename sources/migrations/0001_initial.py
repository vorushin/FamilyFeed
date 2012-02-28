# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FacebookPost'
        db.create_table('sources_facebookpost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('access_token', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('data', self.gf('jsonfield.fields.JSONField')()),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('sources', ['FacebookPost'])


    def backwards(self, orm):
        
        # Deleting model 'FacebookPost'
        db.delete_table('sources_facebookpost')


    models = {
        'sources.facebookpost': {
            'Meta': {'object_name': 'FacebookPost'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {}),
            'data': ('jsonfield.fields.JSONField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['sources']
