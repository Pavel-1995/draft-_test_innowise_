import method as method
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Ticket(models.Model):
    """Class create ticket"""
    class Status(models.Model):
        """Class choice status"""
        statu_s = [
            (1, "В обработке"),
            (2, "Обработан"),
            (3, "Закрыт")
        ]
    text_ticket = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.PositiveSmallIntegerField(('status'), choices=Status.statu_s, blank=False, default=1)

    def __str__(self):
        """Display ticket"""
        return self.text_ticket   #Ticket.objects.all() это все поля text_ticket в бд


class Message(models.Model):
    """Class answer"""
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    number_ticket = models.ForeignKey(Ticket, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    text_answer = models.TextField(blank=True)

    def __str__(self):
        """Display answer"""
        return self.text_answer  ##Message.objects.all() это все поля text_answer в бд


