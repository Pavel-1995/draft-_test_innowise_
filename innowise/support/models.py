from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    class Status(models.Model):
        statu_s = [
            (1, "В обработке"),
            (2, "Обработан"),
            (3, "Закрыт")
        ]
    text_ticke = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    name_user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.PositiveSmallIntegerField(('status'), choices=Status.statu_s, blank=False, default=1)

    def __str__(self):
        return self.text_ticke


class Message(models.Model):
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    ticket_id = models.ForeignKey(Ticket, on_delete=models.PROTECT)
    name_user = models.ForeignKey(User, on_delete=models.PROTECT)
    text_answer = models.TextField(blank=True)

    def __str__(self):
        return self.text_answer