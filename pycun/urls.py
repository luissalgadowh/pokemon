"""pycun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from pokemon.views import pokemon, descripcion_pokemon, tipo_pokemon, onus, pre_message_async, home

urlpatterns = [
    url(r'^$', home),
    url(r'^pokemon/$', pokemon),
    url(r'^admin/', admin.site.urls),
    url(r'^ver-pokemon/$', descripcion_pokemon),
    url(r'^ver-tipo/$', tipo_pokemon),
    url(r'^onus/$', onus),
    # url(r'^pre-message_async/$', pre_message_async),
]
