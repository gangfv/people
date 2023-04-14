from django.contrib import admin
from django.contrib.auth.models import Group
from django_summernote.admin import SummernoteModelAdmin
from .models import Article, New


class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)


admin.site.register(Article, ArticleAdmin)
admin.site.unregister(Group)
admin.site.register(New)

