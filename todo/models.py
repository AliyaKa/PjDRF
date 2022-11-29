from django.conf import settings
from django.db import models


class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=75)
    href = models.URLField
    users = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class ToDo(models.Model):
    project_id = models.ForeignKey(Projects,
                                   null=True,
                                   blank=True,
                                   on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    is_complete = models.BooleanField('Завершено', default=False)

    class Meta:
        ordering = ['created']
