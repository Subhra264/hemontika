from django.contrib import admin
from .models import Story, Poem, Novel, Book, Chapter

# Register your models here.

admin.site.register(Story)
admin.site.register(Poem)
admin.site.register(Novel)
admin.site.register(Book)
admin.site.register(Chapter)
