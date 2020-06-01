"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('404/', TemplateView.as_view(template_name='404.html'), name='404'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('blog-home-1/', TemplateView.as_view(template_name='blog-home-1.html'), name='blog-home-1'),
    path('blog-home-2/', TemplateView.as_view(template_name='blog-home-2.html'), name='blog-home-2'),
    path('blog-post/', TemplateView.as_view(template_name='blog-post.html'), name='blog-post'),
    path('faq/', TemplateView.as_view(template_name='faq.html'), name='faq'),
    path('full-width/', TemplateView.as_view(template_name='full-width.html'), name='full-width'),
    path('portfolio-1-col/', TemplateView.as_view(template_name='portfolio-1-col.html'), name='portfolio-1-col'),
    path('portfolio-2-col/', TemplateView.as_view(template_name='portfolio-2-col.html'), name='portfolio-2-col'),
    path('portfolio-3-col/', TemplateView.as_view(template_name='portfolio-3-col.html'), name='portfolio-3-col'),
    path('portfolio-4-col/', TemplateView.as_view(template_name='portfolio-4-col.html'), name='portfolio-4-col'),
    path('portfolio-item/', TemplateView.as_view(template_name='portfolio-item.html'), name='portfolio-item'),
    path('pricing/', TemplateView.as_view(template_name='pricing.html'), name='pricing'),
    path('services/', TemplateView.as_view(template_name='services.html'), name='services'),
    path('sidebar/', TemplateView.as_view(template_name='sidebar.html'), name='sidebar'),
]
