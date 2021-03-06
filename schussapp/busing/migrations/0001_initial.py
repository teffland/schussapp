# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bus'
        db.create_table(u'busing_bus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('capacity', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('number', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'busing', ['Bus'])

        # Adding model 'BusCheckin'
        db.create_table(u'busing_buscheckin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.Pass'])),
            ('bus', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['busing.Bus'])),
            ('pickup', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'busing', ['BusCheckin'])


    def backwards(self, orm):
        # Deleting model 'Bus'
        db.delete_table(u'busing_bus')

        # Deleting model 'BusCheckin'
        db.delete_table(u'busing_buscheckin')


    models = {
        u'busing.bus': {
            'Meta': {'object_name': 'Bus'},
            'capacity': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'busing.buscheckin': {
            'Meta': {'object_name': 'BusCheckin'},
            'bus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['busing.Bus']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['members.Pass']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'pickup': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
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
        u'members.membertype': {
            'Meta': {'object_name': 'MemberType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['members.MemberType']", 'null': 'True', 'blank': 'True'}),
            'type_abbr': ('django.db.models.fields.CharField', [], {'max_length': '4'})
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
            'member_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['members.MemberType']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'pass_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pass_flag_note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'photo': ('django.db.models.fields.BinaryField', [], {'null': 'True', 'blank': 'True'}),
            'price_paid': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
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

    complete_apps = ['busing']