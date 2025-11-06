from django.db import models

# Create your models here.

class Task(models.Model):
    choices = [
        ['1','Muhim'],
        ['2','Kerak'],
        ['3','Keraksiz'],
        ['4','Sal muhim'],
    ]


    title = models.CharField(max_length=128)
    description = models.TextField()
    task_level = models.CharField(choices=choices,default='1')

    def __str__(self):
        return f'Task(id = {self.id},title = {self.title})'