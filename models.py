from __future__ import unicode_literals

from django.db import models

class todo(models.Model):
    todo_title = models.CharField(max_length=50)
    todo_note = models.CharField(max_length=500)
    todo_date = models.CharField(max_length=100)

    def __str__(self):
        return self.todo_title + ':' + self.todo_note + ':' + self.todo_date