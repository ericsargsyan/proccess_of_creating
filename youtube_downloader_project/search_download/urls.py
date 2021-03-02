from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search_page'),
    path('support/', views.support, name='support_page'),
    path('download/', views.download, name='download_page'),
    # path('download/', views.download, name='download_page'),
    path('test/', views.test, name='test'),
]