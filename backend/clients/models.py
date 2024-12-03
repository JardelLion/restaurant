from django.db import models
import uuid

# Create your models here.

class Client(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    send_notification = models.BooleanField(default=False)
    address = models.TextField(blank=True, null=True)
    birthday = models.DateTimeField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

