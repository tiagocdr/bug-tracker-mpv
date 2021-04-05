from django.db import models
from django.db.models.base import Model
from django.utils import timezone
from myuser.models import MyUser
# Create your models here.

class TicketModel(models.Model):
    title = models.CharField(max_length=50)
    timestamp = models.TimeField(default=timezone.now)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    user_assigned = models.ForeignKey(
        MyUser,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='assigned')
    completed_by = models.ForeignKey(
        MyUser,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='completed')
    NEW = 'new'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'
    INVALID = 'invalid'
    STATUS_CHOICES = [  
        (NEW, 'New'),
        (IN_PROGRESS, 'In progress'),
        (DONE, 'Done'),
        (INVALID, 'Invalid')
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=NEW
        )