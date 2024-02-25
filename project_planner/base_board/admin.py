from django.contrib import admin
from .models import User, Team, TeamUsersMapping, Task, ProjectBoard

# Register your models here.
admin.site.register(User)
admin.site.register(Team)
admin.site.register(TeamUsersMapping)
admin.site.register(Task)
admin.site.register(ProjectBoard)
