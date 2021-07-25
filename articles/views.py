from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'articles/article_edit.html'
    # برای این ویو حتی اگر ریورس لیزی رو برای ساکسس یو آر ال‌ش ننویسی هم می‌ره خودش توی دیتیل ویوی اون آبجکت
    # خیلی عجیب بود...
    # فهمیدمممممم چرااااا
    # توی مدل آرتیکل‌مون یه متد تعریف کردیم get_absolute_url
    # این متد باعث این می‌شه که این‌جا خود به خود ریدایرکت بشه به دیتیل اون آبجکت
    # گویا فقط آپدیت ویو و کرییت ویو از این متد استفاده می‌کنن و ریدایرکت می‌شن

    # این متده هم جدیده برای این‌که اگه خواستی یه متغیر هم به ریورس لیزی بدی
    # def get_success_url(self):
    #     pk = self.kwargs['pk']
    #     return reverse_lazy('article_detail', kwargs={'pk': pk})


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    # کلا به جای این ساکسس یو آر الا می‌تونی هندل کنی
    # که توی تمپلیت اگه روی دکمه‌ی سابمیت زد، بره به اون یو آر الی که می‌خوای
    # باید تگ a توی دکمه بذاری
    success_url = reverse_lazy('article_list')


class ArticleCreateView(CreateView):
    # این ویو خودش یه فرم بر اساس فیلدز می‌سازه و به تمپلیت می‌فرسته
    # اینم خودش خود به خود ریدایرکت می‌شه به دیتیل ویو
    model = Article
    template_name = 'articles/article_new.html'
    fields = ('title', 'body', 'author',)
