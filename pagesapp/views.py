from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """Bosh sahifani ko'rsatish uchun"""
    template_name = 'home.html'


class AboutPageView(TemplateView):
    """About sahifasini ko'rsatish uchun"""
    template_name = 'about.html'


class NewsPageView(TemplateView):
    """News sahifasini ko'rsatish uchun"""
    template_name = 'news.html'


class CompatationsPageView(TemplateView):
    """Comtations sahifasini ko'rsatish uchun"""
    template_name = 'compatations.html'