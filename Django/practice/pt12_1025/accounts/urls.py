from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/<int:pk>/', views.detail, name='detail'),
    path('accounts/<int:pk>/update', views.update, name='update'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', views.logout, name='logout'),
    path('accounts/<int:pk>/follow', views.follow, name='follow'),
]