from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .user_base import UserBase
from .team_base import TeamBase
from .project_board_base import ProjectBoardBase
import json
# Create your views here.

icorrect_payload_error = "Incorrect Payload"
user_base = UserBase()
team_base = TeamBase()
board_base = ProjectBoardBase()

class CreateUserApi(APIView):
    """
        This API will create new user, get details of given user, update details of user
    """
    def get(self, request):
        try:
            res = user_base.describe_user(json.dumps(request.data))
            return Response(res, status=status.HTTP_200_OK)
        except KeyError:
            res = icorrect_payload_error
        except Exception as e:
            res = str(e)

        print(res)
        return Response(str(res), status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            res = user_base.create_user(json.dumps(request.data))
            return Response(res, status=status.HTTP_200_OK)
        except KeyError:
            res = icorrect_payload_error
        except Exception as e:
            res = str(e)

        print(res)
        return Response(str(res), status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            res = user_base.update_user(json.dumps(request.data))
            return Response(res, status=status.HTTP_200_OK)
        except KeyError:
            res = icorrect_payload_error
        except Exception as e:
            res = str(e)

        print(res)
        return Response(str(res), status=status.HTTP_400_BAD_REQUEST)


class ListUsersApi(APIView):
    """
        This API will list all the active users
    """
    def get(self, request):
        try:
            res = user_base.list_users()
            return Response(res, status=status.HTTP_200_OK)
        except KeyError:
            res = icorrect_payload_error
        except Exception as e:
            res = str(e)

        print(res)
        return Response(res, status=status.HTTP_400_BAD_REQUEST)


class GetUserTeams(APIView):
    """
        This API will return all the teams details for given user
    """
    def get(self, request):
        try:
            res = user_base.get_user_teams(json.dumps(request.data))
            return Response(res, status=status.HTTP_200_OK)
        except KeyError:
            res = icorrect_payload_error
        except Exception as e:
            res = str(e)

        print(res)
        return Response(str(res), status=status.HTTP_400_BAD_REQUEST)


class CreateTeamApi(APIView):
    """
        This API will create new team, get details of given team, update details of team
    """
    def get(self, request):
        try:
            res = team_base.describe_team(json.dumps(request.data))
            return Response(res, status=status.HTTP_200_OK)
        except KeyError:
            res = icorrect_payload_error
        except Exception as e:
            res = str(e)

        print(res)
        return Response(str(res), status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            res = team_base.create_team(json.dumps(request.data))
            return Response(res, status=status.HTTP_200_OK)
        except KeyError:
            res = icorrect_payload_error
        except Exception as e:
            res = str(e)

        print(res)
        return Response(str(res), status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            res = team_base.update_team(json.dumps(request.data))
            return Response(res, status=status.HTTP_200_OK)
        except KeyError:
            res = icorrect_payload_error
        except Exception as e:
            res = str(e)

        print(res)
        return Response(str(res), status=status.HTTP_400_BAD_REQUEST)


class ListTeamApi(APIView):
    """
        This API will list all the active teams
    """
    def get(self, request):
        try:
            res = team_base.list_teams()
            return Response(res, status=status.HTTP_200_OK)
        except KeyError:
            res = icorrect_payload_error
        except Exception as e:
            res = str(e)

        print(res)
        return Response(res, status=status.HTTP_400_BAD_REQUEST)


class AddUsersToTeam(APIView):
    """
        This API will add users to given team
    """
    def post(self, request):
        try:
            res = team_base.add_users_to_team(json.dumps(request.data))
            return Response(res, status=status.HTTP_200_OK)
        except KeyError:
            res = icorrect_payload_error
        except Exception as e:
            res = str(e)

        print(res)
        return Response(res, status=status.HTTP_400_BAD_REQUEST)


class RemovUsersFromTeam(APIView):

    def post(self, request):
        try:
            res = team_base.remove_users_from_team(json.dumps(request.data))
            return Response(res, status=status.HTTP_200_OK)
        except KeyError:
            res = icorrect_payload_error
        except Exception as e:
            res = str(e)

        print(res)
        return Response(res, status=status.HTTP_400_BAD_REQUEST)


class ListTeamUsers(APIView):
    """
        This API will remove users from given team
    """
    def get(self, request):
        try:
            res = team_base.list_team_users(json.dumps(request.data))
            return Response(res, status=status.HTTP_200_OK)
        except KeyError:
            res = icorrect_payload_error
        except Exception as e:
            res = str(e)

        print(res)
        return Response(res, status=status.HTTP_400_BAD_REQUEST)


class CreateBoardApi(APIView):
    """
        This API will create new board, delete board
    """
    def post(self, request):
        try:
            res = board_base.create_board(json.dumps(request.data))
            return Response(res, status=status.HTTP_200_OK)
        except KeyError:
            res = icorrect_payload_error
        except Exception as e:
            res = str(e)

        print(res)
        return Response(str(res), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            res = board_base.close_board(json.dumps(request.data))
            return Response(res, status=status.HTTP_200_OK)
        except KeyError:
            res = icorrect_payload_error
        except Exception as e:
            res = str(e)

        print(res)
        return Response(str(res), status=status.HTTP_400_BAD_REQUEST)


class ListBoardsApi(APIView):
    """
        This API will list all active boards
    """
    def get(self, request):
        try:
            res = board_base.list_boards(json.dumps(request.data))
            return Response(res, status=status.HTTP_200_OK)
        except KeyError:
            res = icorrect_payload_error
        except Exception as e:
            res = str(e)

        print(res)
        return Response(res, status=status.HTTP_400_BAD_REQUEST)


class CreateTaskApi(APIView):
    """
        This API will create new task, update details of task
    """
    def post(self, request):
        try:
            res = board_base.add_task(json.dumps(request.data))
            return Response(res, status=status.HTTP_200_OK)
        except KeyError:
            res = icorrect_payload_error
        except Exception as e:
            res = str(e)

        print(res)
        return Response(str(res), status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            res = board_base.update_task_status(json.dumps(request.data))
            return Response(res, status=status.HTTP_200_OK)
        except KeyError:
            res = icorrect_payload_error
        except Exception as e:
            res = str(e)

        print(res)
        return Response(str(res), status=status.HTTP_400_BAD_REQUEST)


class ExportBoardApi(APIView):
    """
        This API will export all data related to given board into csv file
    """
    def post(self, request):
        try:
            res = board_base.export_board(json.dumps(request.data))
            return Response(res, status=status.HTTP_200_OK)
        except KeyError:
            res = icorrect_payload_error
        except Exception as e:
            res = str(e)

        print(res)
        return Response(str(res), status=status.HTTP_400_BAD_REQUEST)
