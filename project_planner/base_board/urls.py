from django.urls import path
from .views import *


urlpatterns = [
    path("users", CreateUserApi.as_view(), name="create_user"),
    path("users/teams", GetUserTeams.as_view(), name="get_users_teams"),
    path("list/users", ListUsersApi.as_view(), name="list_users"),
    path("teams", CreateTeamApi.as_view(), name="create_team"),
    path("list/teams", ListTeamApi.as_view(), name="list_teams"),
    path("list/teams/users", ListTeamUsers.as_view(), name="list_teams_users"),
    path("teams/add/users", AddUsersToTeam.as_view(), name="add_users_to_teams"),
    path("teams/remove/users", RemovUsersFromTeam.as_view(), name="remove_users_to_teams"),
    path("boards", CreateBoardApi.as_view(), name="create_board"),
    path("list/boards", ListBoardsApi.as_view(), name="list_board"),
    path("tasks", CreateTaskApi.as_view(), name="create_task"),
    path("export/boards", ExportBoardApi.as_view(), name="export_board"),
]
