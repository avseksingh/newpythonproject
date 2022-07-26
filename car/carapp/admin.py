from django.contrib import admin


from .models import BooksModel,Reader,TestBook, Quiz, Question, Result, TodoList

# Register your models here.
admin.site.register(BooksModel)
admin.site.register(Reader)
admin.site.register(TestBook)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Result)
admin.site.register(TodoList)