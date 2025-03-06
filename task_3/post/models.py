from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db import models


def validate_keywords(value):
    keywords = [kw.strip() for kw in value.split(",")]
    if len(keywords) < 3:
        raise ValidationError("At least 3 different keywords are required.")
    if len(set(keywords)) < 3:
        raise ValidationError("At least 3 unique keywords are required.")
    return value


class Post(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1024)
    keywords = models.CharField(max_length=500, validators=[validate_keywords])
    url = models.URLField(max_length=1024, validators=[URLValidator()])
    created_at = models.DateTimeField(auto_now_add=True)
    created_by_ip = models.GenericIPAddressField()

    def clean(self):
        if self.name in self.keywords.split(","):
            raise ValidationError("Name cannot be one of the keywords")

    def __str__(self):
        return self.name


class PostHistory(models.Model):
    class Action(models.TextChoices):
        CREATE = 'CREATE', 'Create'
        UPDATE = 'UPDATE', 'Update'
        DELETE = 'DELETE', 'Delete'

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="history")
    action = models.CharField(
        max_length=10,
        choices=Action.choices,
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    data_snapshot = models.JSONField()  # Stores the state of the post at this point

    class Meta:
        ordering = ["-timestamp"]
