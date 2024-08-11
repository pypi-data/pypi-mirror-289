__all__ = ['Stdout']

import time

from django.core.management import get_commands
from django.db import models

NAME2APP = dict(get_commands().items())

def get_timestamp():
    return int(time.time())


class Stdout(models.Model):
    id = models.AutoField(primary_key=True)
    app = models.CharField(max_length=256)
    command = models.CharField(max_length=256)
    stdout = models.TextField()
    size = models.IntegerField()
    created_at = models.IntegerField(default=get_timestamp)

    class Meta:
        db_table = 'django_command_stdout'
        indexes = [
            models.Index(fields=['app',]),
            models.Index(fields=['command',]),
            models.Index(fields=['created_at',]),
        ]
        ordering = ('-created_at','id')
        verbose_name_plural = "stdout"

    def save(self, *args, **kwargs):
        self.app = NAME2APP.get(self.command,self.app).split('.')[-1]
        if self.stdout:
            self.stdout = self.stdout.strip()
            self.size = len(self.stdout)
            super().save(*args, **kwargs)
