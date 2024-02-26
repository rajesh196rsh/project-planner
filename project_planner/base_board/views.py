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
            res = user_base.update_user(request)
            return Response(res, status=status.HTTP_200_OK)
        except KeyError:
            res = icorrect_payload_error
        except Exception as e:
            res = str(e)

        print(res)
        return Response(str(res), status=status.HTTP_400_BAD_REQUEST)


class ListUsersApi(APIView):

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
