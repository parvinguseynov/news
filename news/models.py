from django.db import models
from django.urls import reverse

# Create your models here.

# id - INT
# title - Varchar
# content - Text
# created_at - Datetime
# updated_at - Datetime
# photo - Image
# is_published - Boolean


# Данная модель будет вторичной
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации') # Это поле будет заполнено при создании
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено') # Это поле будет заполнено при создании и при редактировании
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано') # Черновик. Чекбокс отмечен, т.е. по умолчанию новость публикуется
    # Т.к News вторичная модель, связываем ее с первичной моделью Category. PROTECT - обеспечивает защиту от удаления связанных данных
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')


    # Строковое представление объекта __str__
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('news:view_news', kwargs={"news_id": self.pk})


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['created_at'] # Порядок сортировки новостей, он влияет также на news в views



# Данная модель будет первичной
class Category(models.Model):
    # Атрибут db_index - индексирует данное поле, делает более быстрым для поиска
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')


    # Первый параметр - название маршрута, второй параметр - необходимый параметр для построения данного маршрута
    def get_absolute_url(self):
        return reverse('news:category', kwargs={"category_id": self.pk})


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
