from django.urls import path

from .views import HomePageView, AboutPageView, NewsPageView, CompatationsPageView


urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('news/', NewsPageView.as_view(), name='news'),
    path('compatations/', CompatationsPageView.as_view(), name='comptations'),
    path('', HomePageView.as_view(), name='home'),
]