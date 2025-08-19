from django.urls import path
from . import views


urlpatterns = [
    path('',views.Login.as_view(),name='home'),
    path('reset-password',views.Reset.as_view()),
    path('code', views.Code.as_view()),
    
    
]
