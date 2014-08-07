# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ArticleGroup.article_group'
        db.add_column(u'info_articlegroup', 'article_group',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['info.ArticleGroup'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ArticleGroup.article_group'
        db.delete_column(u'info_articlegroup', 'article_group_id')


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