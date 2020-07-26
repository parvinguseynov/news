from django.shortcuts import render
from django.shortcuts import get_object_or_404


from .models import News, Category


# Create your views here.
def index(request):
    news = News.objects.all()
    # categories = Category.objects.all() - можем убрать, т.к мы уже прописали его в тег templatetaghs/news_tags и загрузили в файле _sidebar.html
    context = {
        'news': news,
        'title': 'Список новостей',
        # 'categories': categories,
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id) # filter - т.е WHERE category_id в News равна category_id, то что в url
    # categories = Category.objects.all()
    category = Category.objects.get(pk=category_id) # pk - primary key, то же самое что и id
    return render(request, 'news/category.html', {'news': news, 'category': category}) # 'categories': categories, - можем убрать, есть тег


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id) # Это короткий вариант try ... except. На случай если перейти по не сущест. новости на сайте
    return render (request, 'news/view_news.html', {"news_item": news_item})