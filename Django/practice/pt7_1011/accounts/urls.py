from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('', views.main, name='main'),
    path('accounts/', views.index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/<int:pk>/', views.detail, name='detail'),
]