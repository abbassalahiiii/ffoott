from django.contrib import admin
from .models import Article,category,News,Tables,Post,Natayej,Rooznameh

# Register your models here.

def make_published(ModelAdmin,request,queryset):
    rows_updated=queryset.update(status='p')
    if rows_updated == 1:
        message_bit="منتشر شد."
    else:
        message_bit="منتشر شدند."
        ModelAdmin.message_user(request,"{} مقاله {}".format(rows_updated,message_bit))
make_published.short_description="انتشار مقالات انتخاب شده."

def make_draft(ModelAdmin,request,queryset):
    rows_updated=queryset.update(status='d')
    if rows_updated == 1:
        message_bit="پیش‌نویس شد."
    else:
        message_bit="پیش‌نویش شدند."
        ModelAdmin.message_user(request,"{} مقاله {}".format(rows_updated,message_bit))
make_draft.short_description="پیش‌نویس مقالات انتخاب شده."

class categoryadmin(admin.ModelAdmin):
    list_display=('position','title','parent','slug','status')
    list_filter=(['status'])
    search_fields=('title','slug')
    prepopulated_fields={'slug':('title',)}

admin.site.register(category,categoryadmin)


class artadmin(admin.ModelAdmin):
    list_display=('title','slug','author','status','category_str')
    list_filter=('status',)
    search_fields=('title','discriptions')
    prepopulated_fields={'slug':('title',)}
    ordering=['status']
    actions=[make_published,make_draft]

admin.site.register(Article,artadmin)


class newsadd(admin.ModelAdmin):
    list_display=('title','discriptions','slug','status')
    list_filter=('status',)
    search_fields=('title','discriptions')
    prepopulated_fields={'slug':('title',)}
    ordering=['status']
    actions=[make_published,make_draft]

admin.site.register(News,newsadd)

class tableadd(admin.ModelAdmin):
    list_display=('title','slug','emtiaz')
    prepopulated_fields={'slug':('title',)}
    ordering=['category','-emtiaz','-tafazolegoal','rotbeh']
admin.site.register(Tables,tableadd)

class rooznamehadd(admin.ModelAdmin):
    list_display=('title','slug')
    prepopulated_fields={'slug':('title',)}
    
admin.site.register(Rooznameh,rooznamehadd)


class natayej(admin.ModelAdmin):
    list_display=('mizban','slug')
    prepopulated_fields={'slug':('mizban',)}

admin.site.register(Natayej,natayej)



