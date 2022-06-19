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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from support.views import  *    #TicketApiView,

router = routers.DefaultRouter() # создание objects class DefaultRouter
router.register(r'ticket', TicketViewSet) # регисtrация TicketViewSet # get and post
#print(router.urls)
router_2 = routers.SimpleRouter()
router_2.register(r'message', MessageViewSet)
print(router_2.urls)


urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # соединяет 1 и 2 # ticket/ and ticket/<int:pk>/
    # https:127.0.0.1:8000/api/ticket/...# ..ticket/pk/
    path('api/', include(router_2.urls)),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # появляется поля для ввода
    # # логин и пароль
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),# если время
    # # истекло по этому пути вводим рефреш и получаем новый токены
    #
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

   # path('api/ticketlist/', TicketViewSet.as_view(), # перейдя по
    # ссылке api/ticketlist/ вызовется
    # метод представления TicketViewSet
    #  get-запрос, list-это во
    #   views.py вызовется ModelViewSet он наследуется от ListModelMixin в нем вызрвется метод list
    # path('api/ticketlist/<int:pk>/', TicketViewSet.as_view({'get': 'list', 'post': 'create'})),


]
