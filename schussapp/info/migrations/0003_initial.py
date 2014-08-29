# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'info_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('article_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['info.ArticleGroup'])),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('is_published', self.gf('django.db.models.fields.BinaryField')()),
        ))
        db.send_create_signal(u'info', ['Article'])

        # Adding model 'ArticleGroup'
        db.create_table(u'info_articlegroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('article_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['info.ArticleGroup'], null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'info', ['ArticleGroup'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'info_article')

        # Deleting model 'ArticleGroup'
        db.delete_table(u'info_articlegroup')


    models = {
        u'info.article': {
            'Meta': {'object_name': 'Article'},
            'article_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['info.ArticleGroup']"}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BinaryField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'info.articlegroup': {
            'Meta': {'object_name': 'ArticleGroup'},
            'article_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['info.ArticleGroup']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['info']