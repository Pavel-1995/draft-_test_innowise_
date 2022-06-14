from rest_framework import serializers
from .models import Ticket


# class TicketSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ticket
#         fields = ('user', 'text_ticket', 'status')

class TicketSerializer(serializers.ModelSerializer):
    """Данные в jso nреобразовывает в object"""
    class Meta:
        model = Ticket
        fields =('user', 'text_ticket', 'time_create', 'status') # Поля возвражаемые по запросу











    # text_ticket = serializers.CharField()  # Поля модели Ticket
    # user_id = serializers.CharField()
    # status = serializers.IntegerField()
    # time_create = serializers.DateTimeField(read_only=True)
    #
    # def create(self, validated_data):
    #     """Add data in BaseData"""
    #     return Ticket.objects.create(**validated_data)  # распаковка словоря validated_data
    # # validated_data - Проверенные данные из ф-ц post method is_valid
    #
    # def update(self, instance, validated_data): # instance ссылка на object Ticket
    #     """Update data in BaseData"""
    #     instance.text_ticket = validated_data.get('text_ticket', instance.text_ticket)
    #     instance.user_id = validated_data.get('user_id', instance.user_id)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.time_create = validated_data.get('time_create', instance.time_create)
    #     instance.save()
    #     return instance
    #


