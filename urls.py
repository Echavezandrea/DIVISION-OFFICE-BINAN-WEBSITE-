from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('issuances/', views.issuances, name='issuances'),
    path('qms/', views.qms, name='qms'),
    path('procurement/', views.procurement, name='procurement'),
    path('learningresources/', views.learningresources, name='learningresources'),
    path('research/', views.research, name='research'),
    path('contact/', views.contact, name='contact'),
]
