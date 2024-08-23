# # # # from django.urls import path
# # # # from django.conf.urls import handler404, handler500
# # # # from django.shortcuts import redirect
# # # # from . import views

# # # Definir las funciones que manejarán los errores
# # # # def redirect_to_home(request, exception=None):
    # # # # return redirect('index')  # Aquí 'index' es el nombre de tu vista de inicio

# # # # def redirect_to_home_500(request):
    # # # # return redirect('index')  # Aquí 'index' es el nombre de tu vista de inicio

# # # Asignar las funciones a los manejadores de errores
# # # # handler404 = redirect_to_home
# # # # handler500 = redirect_to_home_500

# # # # urlpatterns = [
    # # # tus otras rutas aquí
    # # # # path('', include('pipi.urls')),  # Asegúrate de que la ruta al home esté incluida
# # # # ]

"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
URL configuration for pipipuntos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
