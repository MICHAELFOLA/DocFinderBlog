from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.index, name='index'),
]



