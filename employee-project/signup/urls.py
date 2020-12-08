from django.urls import path

from . import views

urlpatterns = [
    path('data/', views.data, name='data'),
    path('signup/', views.signup, name='signup'),
    path('test/', views.test, name='test'),
]