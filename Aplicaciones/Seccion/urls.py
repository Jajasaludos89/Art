from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/login/')),  # Redirige la raíz al login
    path('login/', views.login_view),
    path('registro/', views.registro_view),
    path('logout/', views.logout_view),
]
