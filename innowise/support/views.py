from _testcapi import raise_exception
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from .models import *
from .serializers import TicketSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


def index(request):
    """Пробная ф-ц потом удалить"""
    return HttpResponse('Временно вместо page not found 404')


class TicketViewSet(viewsets.ModelViewSet):
    """class for CRUD"""
    queryset = Ticket.objects.all() # выберет все записи и отдаст его методу
    # list он после проверки отдаст его сериализатору сериализотор вернет те поля которые прописаны в поле
    # field in class meta
    serializer_class = TicketSerializer # указываем какой сериализотор будет обрабатывать данные queryset

    # @action(methods=['get'], detail=True) #  True Отображение записи ответов, if False то всех записей
    # def answer(self, request, pk = None): # add new path in class TicketViewSet
    #     number_answer = Message.objects.get(pk=pk)
    #     return Response({'number_answer': number_answer.text_answer,  'user_id': number_answer.user_id})



# class TicketApiView(generics.ListAPIView):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer

# class TicketApiList(generics.ListCreateAPIView):
#     """class for get and post"""
#     queryset = Ticket.objects.all()  # Список записей возвращаемые по запросу
#     serializer_class = TicketSerializer # serializer  для применения к queryset
#
# class TicketApiUpdate(generics.UpdateAPIView):
#     """class for put or patch"""
#     queryset = Ticket.objects.all()  # Вернет только одну измененную запись для отображения
#     serializer_class = TicketSerializer  # serializer  для применения к queryset

# class TicketAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer

# class TicketApiView(APIView):
#
#     def get(self, request):
#         """Get data from BaseData"""
#         t = Ticket.objects.all()
#         return Response({'ticket': TicketSerializer(t, many=True).data})
#
#     def post(self, request):
#         """Add data in BaseDate"""
#         serializer = TicketSerializer(data=request.data) # входные данные преобразованы в сериализатор in object
#         serializer.is_valid(raise_exception=True) # Проверка данных
#         serializer.save() # Вызовет метод create
#
#         # ticket_new = Ticket.objects.create(
#         #     text_ticket=request.data['text_ticket'], # Поля class TicketSerializer
#         #     user_id=request.data['user_id'],
#         #     status=request.data['status']
#         # )
#         #return Response({'ticket': TicketSerializer(ticket_new).data}) # Словарь добавленной записи
#         return Response({'ticket': serializer.data}) # data - return def create
#
#     def put(selfself, request, *args, **kwargs):
#         """Update data in BaseData"""
#         pk = kwargs.get('pk', None) # если нет ключа pk верни None
#         if not pk:
#             return Response({'error': 'not pk'})
#
#         try:  # Попробуй сделать
#             instance = Ticket.objects.get(pk=pk)
#         except:
#             return Response({'error': 'objects not found'})
#
#         # Если получили ключ и запись по pk создаем сериализатор
#         serializer = TicketSerializer(data=request.data, instance=instance) # Данные которые надо изменить
#         serializer.is_valid(raise_exception=True) # Проверка данных
#         serializer.save() # method save  вызывает def update
#         return Response({'ticket': serializer.data})



