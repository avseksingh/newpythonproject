from django.contrib import admin


from .models import BooksModel,Reader,TestBook, Quiz, Question

# Register your models here.
admin.site.register(BooksModel)
admin.site.register(Reader)
admin.site.register(TestBook)
admin.site.register(Quiz)
admin.site.register(Question)