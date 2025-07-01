from django.urls import path
from usuarios import views as usuarios_views

urlpatterns = [
    path('registro/', usuarios_views.registro_usuario, name='registro'),
    path('login/', usuarios_views.login_usuario, name='login'),
    path('dashboard/', usuarios_views.dashboard, name='dashboard'),
]
