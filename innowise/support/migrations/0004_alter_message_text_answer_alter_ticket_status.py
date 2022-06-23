# Generated by Django 4.0.5 on 2022-06-23 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0003_rename_status_id_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='text_answer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Ожидает получения вопроса'), (1, 'В обработке'), (2, 'Обработан'), (3, 'Закрыт')], default=1, verbose_name='status'),
        ),
    ]
