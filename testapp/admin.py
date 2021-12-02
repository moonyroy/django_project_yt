from django.contrib import admin

from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None , {'fields' : ['title']}),
        ('contact information' , {'fields' : ['content' , 'author']}),
        ('image' , {'fields' : ['image']}),
        ('like' , {'fields' : ['likes']})
    ]
    list_display = ['title' , 'date']
    search_fields = ['title']
admin.site.register(Blog , BlogAdmin)
