from django.urls import path
from Aplicaciones.usuarios import views as usuarios_views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/login/')),
    path('registro/', usuarios_views.registro_usuario, name='registro'),
    path('login/', usuarios_views.login_usuario, name='login'),
    path('dashboard/', usuarios_views.dashboard, name='dashboard'),
]
