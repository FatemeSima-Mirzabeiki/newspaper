from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'articles/article_list.html'


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'articles/article_detail.html'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'articles/article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
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


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    # کلا به جای این ساکسس یو آر الا می‌تونی هندل کنی
    # که توی تمپلیت اگه روی دکمه‌ی سابمیت زد، بره به اون یو آر الی که می‌خوای
    # باید تگ a توی دکمه بذاری
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    # این ویو خودش یه فرم بر اساس فیلدز می‌سازه و به تمپلیت می‌فرسته
    # اینم خودش خود به خود ریدایرکت می‌شه به دیتیل ویو
    model = Article
    template_name = 'articles/article_new.html'
    fields = ('title', 'body')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
