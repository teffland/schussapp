# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mountain'
        db.create_table(u'mountains_mountain', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('state', self.gf('localflavor.us.models.USStateField')(default='NY', max_length=2)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('phone', self.gf('localflavor.us.models.PhoneNumberField')(max_length=20)),
            ('vertical', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('num_lifts', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('num_trails', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('ski_acre', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'mountains', ['Mountain'])

        # Adding model 'MountainCheckin'
        db.create_table(u'mountains_mountaincheckin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('member_pass', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.Pass'])),
            ('mountain', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mountains.Mountain'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'mountains', ['MountainCheckin'])

        # Adding model 'MountainScheduleSlot'
        db.create_table(u'mountains_mountainscheduleslot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
            ('mountain', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mountains.Mountain'])),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.Season'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'mountains', ['MountainScheduleSlot'])


    def backwards(self, orm):
        # Deleting model 'Mountain'
        db.delete_table(u'mountains_mountain')

        # Deleting model 'MountainCheckin'
        db.delete_table(u'mountains_mountaincheckin')

        # Deleting model 'MountainScheduleSlot'
        db.delete_table(u'mountains_mountainscheduleslot')


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
        },
        u'mountains.mountain': {
            'Meta': {'object_name': 'Mountain'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'num_lifts': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_trails': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'phone': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'ski_acre': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('localflavor.us.models.USStateField', [], {'default': "'NY'", 'max_length': '2'}),
            'vertical': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'mountains.mountaincheckin': {
            'Meta': {'object_name': 'MountainCheckin'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_pass': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['members.Pass']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'mountain': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mountains.Mountain']"})
        },
        u'mountains.mountainscheduleslot': {
            'Meta': {'object_name': 'MountainScheduleSlot'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'mountain': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mountains.Mountain']"}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['members.Season']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['mountains']