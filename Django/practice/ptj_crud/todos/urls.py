from django.urls import path, include
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('update/<int:pk>', views.update, name='update'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('editUpdate/<int:pk>', views.editUpdate, name='editUpdate'),
]

