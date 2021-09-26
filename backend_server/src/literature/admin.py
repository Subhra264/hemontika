from django.contrib import admin
from .models import Story, Poem, Novel, DragDropSelectBook, Chapter

# Register your models here.

admin.site.register(Story)
admin.site.register(Poem)
admin.site.register(Novel)
admin.site.register(DragDropSelectBook)
admin.site.register(Chapter)
