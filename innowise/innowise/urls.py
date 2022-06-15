"""innowise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import  include
from rest_framework import routers
from support.views import  *    #TicketApiView,

router = routers.DefaultRouter() # создание objects class DefaultRouter
router.register(r'ticket', TicketViewSet) # регисtrация TicketViewSet # get and post

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),   # https:127.0.0.1:8000/api/ticket/...# ..ticket/pk/

    path('api/ticketlist/', TicketViewSet.as_view({'get': 'list'})), # перейдя по
    # ссылке api/ticketlist/ вызовется
    # метод представления TicketViewSet
    #  get-запрос, list-это во
    #   views.py вызовется ModelViewSet он наследуется от ListModelMixin в нем вызрвется метод list
    path('api/ticketlist/<int:pk>/', TicketViewSet.as_view({'put': 'update'})),


]
