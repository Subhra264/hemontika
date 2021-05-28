from django.contrib import admin
from .models import HemontikaUser, Story, Poem, Novel, Book, Chapter, Tag

# Register your models here.

admin.site.register(Tag)
admin.site.register(HemontikaUser)
admin.site.register(Story)
admin.site.register(Poem)
admin.site.register(Novel)
admin.site.register(Book)
admin.site.register(Chapter)
