from django.db import models

# Create your models here.

# id - INT
# title - Varchar
# content - Text
# created_at - Datetime
# updated_at - Datetime
# photo - Image
# is_published - Boolean


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True) # Черновик. Чекбокс отмечен, т.е. по умолчанию новость публикуется



