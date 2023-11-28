from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path('', views.home, name='home'),
    path('aboutus/', views.about, name='about'),
    path('product/<slug:product_slug>/', views.product_detail_view, name='product_detail'),
    path('productlist/', views.product_list, name='productlist'),
    path('founder/<slug:fname_slug>', views.founder, name='founder'),
    path('teamlist/', views.teamlist, name='teamlist'),
    path('team/<slug:tname_slug>', views.team, name='team'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 