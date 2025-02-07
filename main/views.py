
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Comfort - Главная'
        context['content'] = 'Магазин мебели COMFORT'      
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Comfort - О нас'
        context['content'] = 'О нас'
        context['text_on_page'] = 'Текст о том почему этот магазин такой класный, и какой хороший товар.'
        return context

# def index(request):  

#     context = {
#         'title': 'Comfort - Главная',
#         'content': 'Магазин мебели COMFORT',
       
#     }
#     return render(request, 'main/index.html', context)

# def about(request):
       
#     context = {
#         'title': 'Comfort - О нас',
#         'content': 'О нас',
#         'text_on_page': 'Текст о том почему этот магазин такой класный, и какой хороший товар.'
#     }
#     return render(request, 'main/about.html', context)
