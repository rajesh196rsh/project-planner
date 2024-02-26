import json
from .models import User, TeamUsersMapping, Team
class UserBase:
    """
    Base interface implementation for API's to manage users.
    """

    # create a user
    def create_user(self, request: str) -> str:
        """
        :param request: A json string with the user details
        {
          "name" : "<user_name>",
          "display_name" : "<display name>"
        }
        :return: A json string with the response {"id" : "<user_id>"}

        Constraint:
            * user name must be unique
            * name can be max 64 characters
            * display name can be max 64 characters
        """
        data = json.loads(request)

        if len(data["name"]) > 64:
            raise ValueError("User name cannot exceed 64 characters")
        if len(data["display_name"]) > 64:
            raise ValueError("Display name cannot exceed 64 characters")

        user_obj = User.objects.create(name=data["name"].lower(), display_name=data["display_name"])
        res = {
            "id": user_obj.id
        }
        res = json.dumps(res)
        return res

    # list all users
    def list_users(self) -> str:
        """
        :return: A json list with the response
        [
          {
            "name" : "<user_name>",
            "display_name" : "<display name>",
            "creation_time" : "<some date:time format>"
          }
        ]
        """
        users_objs = User.objects.filter(active=True)

        res = []
        for a_user in users_objs:
            user = {
              "name" : a_user.name.capitalize(),
              "display_name" : a_user.display_name,
              "creation_time" : str(a_user.created_at)
            }
            res.append(user)

        res = json.dumps(res)
        return res

    # describe user
    def describe_user(self, request: str) -> str:
        """
        :param request: A json string with the user details
        {
          "id" : "<user_id>"
        }

        :return: A json string with the response

        {
          "name" : "<user_name>",
          "description" : "<some description>",
          "creation_time" : "<some date:time format>"
        }

        """
        data = json.loads(request)

        user_obj = User.objects.filter(id=data["user_id"], active=True)
        if user_obj:
            res = {
                "name": user_obj[0].name.capitalize(),
                "display_name": user_obj[0].display_name,
                "creation_time": str(user_obj[0].created_at)
            }
            res = json.dumps(res)
        else:
            res = "User does not exists"
        return res

    # update user
    def update_user(self, request: str) -> str:
        """
        :param request: A json string with the user details
        {
          "id" : "<user_id>",
          "user" : {
            "name" : "<user_name>",
            "display_name" : "<display name>"
          }
        }

        :return:

        Constraint:
            * user name cannot be updated
            * name can be max 64 characters
            * display name can be max 128 characters
        """
        data = json.loads(request)

        display_name = data.get("user", {}).get("display_name")
        if display_name:
            if len(display_name) > 64:
              raise ValueError("Display name cannot exceed 64 characters")
            User.objects.update(display_name=display_name)

        return "updated"

    def get_user_teams(self, request: str) -> str:
        """
        :param request:
        {
          "id" : "<user_id>"
        }

        :return: A json list with the response.
        [
          {
            "name" : "<team_name>",
            "description" : "<some description>",
            "creation_time" : "<some date:time format>"
          }
        ]
        """
        data = json.loads(request)

        user_id = data["id"]
        user_teams = TeamUsersMapping.objects.filter(user_id=user_id, active=True)

        user_teams_creation_map = {}
        team_ids = []
        for a_user_team in user_teams:
            team_ids.append(a_user_team.team_id)
            user_teams_creation_map[a_user_team.team_id] = str(a_user_team.created_at)

        teams = Team.objects.filter(id__in=team_ids)

        res = []
        for a_team in teams:
            res.append(
                {
                    "name": a_team.name.capitalize(),
                    "description": a_team.description,
                    "creation_time": user_teams_creation_map[a_team.id]
                }
            )
        res = json.dumps(res)
        return res
