# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Member'
        db.create_table(u'members_member', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('person_number', self.gf('django.db.models.fields.CharField')(max_length=8, blank=True)),
            ('local_address', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(default='Buffalo', max_length=25)),
            ('state', self.gf('localflavor.us.models.USStateField')(default='NY', max_length=2)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(default='14261', max_length=5)),
            ('dorm', self.gf('django.db.models.fields.CharField')(max_length=4, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('phone', self.gf('localflavor.us.models.PhoneNumberField')(max_length=20)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(default='M', max_length=1)),
            ('photo', self.gf('django.db.models.fields.BinaryField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'members', ['Member'])

        # Adding model 'Pass'
        db.create_table(u'members_pass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.Member'])),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.Season'])),
            ('is_reserved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('active_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('member_type', self.gf('django.db.models.fields.CharField')(default='FR', max_length=4, db_column='type')),
            ('lost_stolen', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('lost_stolen_note', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('bus_flag', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bus_flag_note', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('pass_flag', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pass_flag_note', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'members', ['Pass'])

        # Adding model 'Season'
        db.create_table(u'members_season', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fall', self.gf('django.db.models.fields.DateField')()),
            ('spring', self.gf('django.db.models.fields.DateField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'members', ['Season'])


    def backwards(self, orm):
        # Deleting model 'Member'
        db.delete_table(u'members_member')

        # Deleting model 'Pass'
        db.delete_table(u'members_pass')

        # Deleting model 'Season'
        db.delete_table(u'members_season')


    models = {
        u'members.member': {
            'Meta': {'object_name': 'Member'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'default': "'Buffalo'", 'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dorm': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'local_address': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'person_number': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'phone': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'photo': ('django.db.models.fields.BinaryField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('localflavor.us.models.USStateField', [], {'default': "'NY'", 'max_length': '2'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'default': "'14261'", 'max_length': '5'})
        },
        u'members.pass': {
            'Meta': {'object_name': 'Pass'},
            'active_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bus_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bus_flag_note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_reserved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lost_stolen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lost_stolen_note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['members.Member']"}),
            'member_type': ('django.db.models.fields.CharField', [], {'default': "'FR'", 'max_length': '4', 'db_column': "'type'"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'pass_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pass_flag_note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['members.Season']"})
        },
        u'members.season': {
            'Meta': {'object_name': 'Season'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fall': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'spring': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['members']