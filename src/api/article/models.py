from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField('The time it was created',
                                      auto_now_add=True)
    edited_at = models.DateTimeField('The time when it was latestly edited',
                                     auto_now=True)
    deleted_at = models.DateTimeField('The time when it was deleted',
                                      null=True, blank=True)
    deleted = models.BooleanField('This record is deleted', default=False)

    class Meta:
        abstract = True


class Article(BaseModel):
    title = models.CharField(name='title', max_length=128)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(verbose_name='The content of an article')
    html = models.TextField(
        verbose_name='The html formed content of an article')

    def __str__(self):
        return self.title
