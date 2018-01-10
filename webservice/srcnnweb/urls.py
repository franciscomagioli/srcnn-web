from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('results/<int:imagecontrol_id>', views.detail, name='detail'),
]
