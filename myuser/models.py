from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    # filed_tickets = models.ForeignKey(
    #     TicketModel,
    #     on_delete=models.CASCADE
    #     )
    # in_progress = models.ForeignKey(
    #     TicketModel,
    #     on_delete=models.CASCADE,
    #     related_name=
    #     )
    # completed = models.ForeignKey(
    #     TicketModel,
    #     on_delete=models.CASCADE,
    #     related_name='completed'
    #     )
    pass