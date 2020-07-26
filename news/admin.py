from django.contrib import admin
from . import models

# Register your models here.

# Представление модели в админке
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published', 'category')
    list_display_links = ('id', 'title') # Наименования, к-ые должны быть ссылкой в админке
    search_fields = ('title', 'content') # Поля, по к-ым можно осуществлять поиск в админке
    list_editable = ('is_published',) # Поля, к-ые можно отредактировать прям со списка новостей
    list_filter = ('is_published', 'category') # Поля, по которым можно осуществлять фильтрацию




class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',) # Так как это кортеж в конце должна стоять запятая


admin.site.register(models.News, NewsAdmin) # Сперва регистрируем основную модель
admin.site.register(models.Category)
