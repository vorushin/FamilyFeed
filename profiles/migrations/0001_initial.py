# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Child'
        db.create_table('profiles_child', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('birthdate', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('profiles', ['Child'])

        # Adding model 'DataSource'
        db.create_table('profiles_datasource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('child', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.Child'])),
            ('keywords', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('profiles', ['DataSource'])

        # Adding model 'TwitterSource'
        db.create_table('profiles_twittersource', (
            ('datasource_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['profiles.DataSource'], unique=True, primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('profiles', ['TwitterSource'])

        # Adding model 'YoutubeSource'
        db.create_table('profiles_youtubesource', (
            ('datasource_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['profiles.DataSource'], unique=True, primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('profiles', ['YoutubeSource'])

        # Adding model 'FacebookSource'
        db.create_table('profiles_facebooksource', (
            ('datasource_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['profiles.DataSource'], unique=True, primary_key=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('access_token', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('profiles', ['FacebookSource'])


    def backwards(self, orm):
        
        # Deleting model 'Child'
        db.delete_table('profiles_child')

        # Deleting model 'DataSource'
        db.delete_table('profiles_datasource')

        # Deleting model 'TwitterSource'
        db.delete_table('profiles_twittersource')

        # Deleting model 'YoutubeSource'
        db.delete_table('profiles_youtubesource')

        # Deleting model 'FacebookSource'
        db.delete_table('profiles_facebooksource')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'profiles.child': {
            'Meta': {'object_name': 'Child'},
            'birthdate': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'profiles.datasource': {
            'Meta': {'object_name': 'DataSource'},
            'child': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.Child']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {})
        },
        'profiles.facebooksource': {
            'Meta': {'object_name': 'FacebookSource', '_ormbases': ['profiles.DataSource']},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'datasource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['profiles.DataSource']", 'unique': 'True', 'primary_key': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'profiles.twittersource': {
            'Meta': {'object_name': 'TwitterSource', '_ormbases': ['profiles.DataSource']},
            'datasource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['profiles.DataSource']", 'unique': 'True', 'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'profiles.youtubesource': {
            'Meta': {'object_name': 'YoutubeSource', '_ormbases': ['profiles.DataSource']},
            'datasource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['profiles.DataSource']", 'unique': 'True', 'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['profiles']
