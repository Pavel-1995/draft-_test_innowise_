from _testcapi import raise_exception
from .tasks import send_email
from django.core import mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from .models import *
from .permissions import IsAdminOrIsAuthenticated
from django.core.mail import EmailMessage, send_mail
from .serializers import TicketSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
#
#
def index(request):
    """Пробная ф-ц потом удалить"""
    return HttpResponse('Временно вместо page not found 404')


class TicketApiListPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 30


class MessageApiListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 30


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    pagination_class = TicketApiListPagination
    permission_classes = (IsAdminOrIsAuthenticated,)

    def perform_update(self, serializer, default_status = 1):
        serializer.save()
        if serializer.data['status'] != default_status:
            #send_mail('status', 'Status your ticket changed', 'dudufhdbchfuhd@gmail.com', ['pavelalexei1177@gmail.com',], fail_silently=False)
            send_email.delay()
        else:
            print('error sent_email')

    def perform_create(self, serializer, default_status = 1):
        serializer.validated_data['status'] = default_status
        serializer.save()


    @action(methods=['get', 'post'], detail=True)
    def answer(self, request, pk=None):
        answer_s = Message.objects.get(number_ticket_id=pk)
        num_ticket = Ticket.objects.get(pk=pk)
        CreateModelMixin.create(self, request)
        return Response({'ticket': num_ticket.text_ticket, 'answer': answer_s.text_answer})


    @action(methods=['get'], detail=False)
    def answer(self, request):
        answer_s = Message.objects.filter(user=self.request.user).values()
        num_ticket = Ticket.objects.filter(user=self.request.user).values()
        return Response({'ticket': num_ticket, 'answer': answer_s})


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = MessageApiListPagination
    permission_classes = (IsAdminUser,)














#-------------Код начальной разработки для автора проекта------------------------------------------------------#

# ##class TicketViewSet(viewsets.ModelViewSet):
#    ## """class for CRUD"""
#    ## queryset = Ticket.objects.all() # выберет все записи и отдаст его методу
#     # list он после проверки отдаст его сериализатору сериализотор вернет те поля которые прописаны в поле
#     # field in class meta
#    ## serializer_class = TicketSerializer # указываем какой сериализотор будет обрабатывать данные queryset
#     # @action(methods=['get'], detail=True) # return json
#     #  True Отображение записи ответов, if False то всех записей
#     # def answer(self, request, pk = None): # add new path in class TicketViewSet
#     #     number_answer = Message.objects.get(pk=pk)
#     #     return Response({'number_answer': number_answer.text_answer,  'user_id': number_answer.user_id})
#
#
#
# # class TicketApiView(generics.ListAPIView):
# #     queryset = Ticket.objects.all()
# #     serializer_class = TicketSerializer
#
# # class TicketApiList(generics.ListCreateAPIView):
# #     """class for get and post"""
# #     queryset = Ticket.objects.all()  # Список записей возвращаемые по запросу
# #     serializer_class = TicketSerializer # serializer  для применения к queryset
# #
# # class TicketApiUpdate(generics.UpdateAPIView):
# #     """class for put or patch"""
# #     queryset = Ticket.objects.all()  # Вернет только одну измененную запись для отображения
# #     serializer_class = TicketSerializer  # serializer  для применения к queryset
#
# # class TicketAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = Ticket.objects.all()
# #     serializer_class = TicketSerializer
#
# # class TicketApiView(APIView):
# #
# #     def get(self, request):
# #         """Get data from BaseData"""
# #         t = Ticket.objects.all()
# #         return Response({'ticket': TicketSerializer(t, many=True).data})
# #
# #     def post(self, request):
# #         """Add data in BaseDate"""
# #         serializer = TicketSerializer(data=request.data) # входные данные преобразованы в сериализатор in object
# #         serializer.is_valid(raise_exception=True) # Проверка данных
# #         serializer.save() # Вызовет метод create
# #
# #         # ticket_new = Ticket.objects.create(
# #         #     text_ticket=request.data['text_ticket'], # Поля class TicketSerializer
# #         #     user_id=request.data['user_id'],
# #         #     status=request.data['status']
# #         # )
# #         #return Response({'ticket': TicketSerializer(ticket_new).data}) # Словарь добавленной записи
# #         return Response({'ticket': serializer.data}) # data - return def create
# #
# #     def put(selfself, request, *args, **kwargs):
# #         """Update data in BaseData"""
# #         pk = kwargs.get('pk', None) # если нет ключа pk верни None
# #         if not pk:
# #             return Response({'error': 'not pk'})
# #
# #         try:  # Попробуй сделать
# #             instance = Ticket.objects.get(pk=pk)
# #         except:
# #             return Response({'error': 'objects not found'})
# #
# #         # Если получили ключ и запись по pk создаем сериализатор
# #         serializer = TicketSerializer(data=request.data, instance=instance) # Данные которые надо изменить
# #         serializer.is_valid(raise_exception=True) # Проверка данных
# #         serializer.save() # method save  вызывает def update
# #         return Response({'ticket': serializer.data})
#
#
#
# from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
#
#
# # class TicketApiListPagination(PageNumberPagination):
# #     page_size = 3  # ображение на стр по 3 записи
# #     page_size_query_param = 'page_size' # переопределения атрибута page_size в строке запроса
# #     max_page_size = 30 # ксимальное значение которое может принимать page_size_query_param
# #     # т е отображать не более 30 записей на стр
#
#
# class TicketViewSet(viewsets.ModelViewSet):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer
#     permission_classes_by_action = {
#                                    'list': [AllowAny], # list метод в миксинах
#
#     }
#     #pagination_class = TicketApiListPagination
#     def get_permissions(self):
#         try:
#             # return permission_classes depending on `action`
#             return [permission() for permission in self.permission_classes_by_action[self.action]]
#
#         except KeyError:
#             # action is not set return default permission_classes
#             return [permission() for permission in self.permission_classes]
#









