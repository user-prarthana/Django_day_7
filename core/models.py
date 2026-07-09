from django.db import models
from django.contrib.auth.models import User

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.TextField()
    experience = models.IntegerField()

    def __str__(self):
        return self.user.username


class Job(models.Model):
    employer = models.ForeignKey(
        Employer,
        on_delete=models.CASCADE,
        related_name='jobs'
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )