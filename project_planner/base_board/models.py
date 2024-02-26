from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=64, unique=True)
    display_name = models.CharField(max_length=64)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Team(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=128)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TeamUsersMapping(models.Model):
    team_id = models.IntegerField()
    user_id = models.IntegerField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Mets:
        unique_together = ('team_id', 'user_id')


task_status_choices = (
    ('1', 'OPEN'),
    ('2', 'IN_PROGRESS'),
    ('3', 'COMPLETE')
)

class Task(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=20, choices=task_status_choices, default="OPEN")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Mets:
        unique_together = ('name', 'board')


board_status_choices = (
    ("1", "OPEN"),
    ("2", "CLOSED")
)

class ProjectBoard(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=128)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)
    tasks = models.ManyToManyField(Task, blank=True, related_name="tasks_list")
    status = models.CharField(max_length=20, choices=board_status_choices, default="OPEN")
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
