from django.db import models
from django.conf import settings


class AbstractComment(models.Model):
    CREATED = 10
    APPROVED = 20
    REJECTED = 30
    DELETED = 40
    STATUS_CHOICE = (
        (CREATED, 'created'),
        (APPROVED, 'approved'),
        (REJECTED, 'rejected'),
        (DELETED, 'deleted')
    )
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)ss')
    comment_body = models.TextField(max_length=300)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICE, default=CREATED)
    validated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='validated_%(class)ss')
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
