from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thuesday', 'Thuesday'),
        ('Friday', 'Friday'),
        ('Saturaday', 'Saturaday'),
        ('Sunday', 'Sunday'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    task = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user.name} - {self.day}: {self.task}"