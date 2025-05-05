from django.db import models
from django.conf import settings


# Create your models here.
class Message(models.Model):
    ROLE_CHOICES = (
        ("user", "User"),
        ("system", "System"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role} ({self.timestamp}): {self.content[:30]}"
