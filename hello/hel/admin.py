from django.contrib import admin
from hel.models import BookInfo,HeroInfo
# Register your models here.
class BookInfoAdmin(admin.ModelAdmin):
    '''book model manage'''
    list_display = ['id','btitle','bpub_data']

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)