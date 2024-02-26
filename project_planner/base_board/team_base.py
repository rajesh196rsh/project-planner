import json
from .models import Team, TeamUsersMapping, User


class TeamBase:
    """
    Base interface implementation for API's to manage teams.
    For simplicity a single team manages a single project. And there is a separate team per project.
    Users can be
    """

    # create a team
    def create_team(self, request: str) -> str:
        """
        :param request: A json string with the team details
        {
          "name" : "<team_name>",
          "description" : "<some description>",
          "admin": "<id of a user>"
        }
        :return: A json string with the response {"id" : "<team_id>"}

        Constraint:
            * Team name must be unique
            * Name can be max 64 characters
            * Description can be max 128 characters
        """
        data = json.loads(request)

        if len(data["name"]) > 64:
            raise ValueError("Team name cannot exceed 64 characters")
        if len(data["description"]) > 128:
            raise ValueError("Description cannot exceed 128 characters")

        team_obj = Team.objects.create(name=data["name"], description=data["description"])

        users = [data["admin"]] if data.get("admin") else []
        add_users_payload = {
            "id": team_obj.id,
            "users": users
        }
        _ = self.add_users_to_team(json.dumps(add_users_payload))

        res = {
            "id": team_obj.id
        }
        res = json.dumps(res)
        return res

    # list all teams
    def list_teams(self) -> str:
        """
        :return: A json list with the response.
        [
          {
            "name" : "<team_name>",
            "description" : "<some description>",
            "creation_time" : "<some date:time format>",
            "admin": "<id of a user>"
          }
        ]
        """
        teams_objs = Team.objects.all(active=True)
        team_ids = []
        for a_team in team_ids:
            team_ids.append(a_team.id)
        teams_users_map_objs = TeamUsersMapping.objects.filter(team_id__in=team_ids, active=True).values("team_id", "user_id")

        teams_users_map = {}
        for a_team_user in teams_users_map_objs:
            if teams_users_map.get(a_team_user[0]):
                teams_users_map[a_team_user[0]].append(a_team_user[1])
            else:
                teams_users_map[a_team_user[0]] = [a_team_user[1]]

        res = []
        for a_team in teams_objs:
            user = {
              "name" : a_team.name,
              "description" : a_team.description,
              "creation_time" : a_team.created_at,
              "admin": teams_users_map[a_team.id]
            }
            res.append(user)

        res = json.dumps(res)
        return res

    # describe team
    def describe_team(self, request: str) -> str:
        """
        :param request: A json string with the team details
        {
          "id" : "<team_id>"
        }

        :return: A json string with the response

        {
          "name" : "<team_name>",
          "description" : "<some description>",
          "creation_time" : "<some date:time format>",
          "admin": "<id of a user>"
        }

        """
        data = json.loads(request)

        team_id = data["id"]
        team_obj = Team.objects.filter(id=team_id, active=True)
        if team_obj:
            team_obj = team_obj[0]
            user_ids = TeamUsersMapping.objects.filter(team_id=team_id, active=True).values("user_id")
            res = {
                "name": team_obj.name,
                "desccription": team_obj.description,
                "creation_time": team_obj.created_at,
                "admin": user_ids
            }
            res = json.dumps(res)
            return res
        else:
            return "Team does not exists"

    # update team
    def update_team(self, request: str) -> str:
        """
        :param request: A json string with the team details
        {
          "id" : "<team_id>",
          "team" : {
            "name" : "<team_name>",
            "description" : "<team_description>",
            "admin": "<id of a user>"
          }
        }

        :return:

        Constraint:
            * Team name must be unique
            * Name can be max 64 characters
            * Description can be max 128 characters
        """
        data = json.loads(request)

        team_id = data["id"]
        team_obj = Team.objects.filter(id=team_id)
        if team_obj:
            team_obj = team_obj[0]
            team = data.get("team", {})
            new_name = team.get("name", None)
            if new_name:
                if len(new_name) > 64:
                    raise ValueError("Team name cannot exceed 64 characters")
                else:
                    team_obj.name = new_name
            new_description = team.get("description", None)
            if new_description:
                if len(new_description) > 128:
                    raise ValueError("Discription cannot exceed 128 characters")
                else:
                    team_obj.description = new_description
            team_obj.save()

            users = [team["admin"]] if team.get("admin", None) else []
            add_users_payload = {
                "id": team_id,
                "users": users
            }

            res = self.add_users_to_team(json.dumps(add_users_payload))
        else:
            res = "Team does not exists"

        return res

    # add users to team
    def add_users_to_team(self, request: str):
        """
        :param request: A json string with the team details
        {
          "id" : "<team_id>",
          "users" : ["user_id 1", "user_id2"]
        }

        :return:

        Constraint:
        * Cap the max users that can be added to 50
        """
        data = json.loads(request)

        team_id = data["id"]
        existing_users = TeamUsersMapping.objects.filter(team_id=team_id, active=True).values("user_id")
        users = data["users"]
        users = list(set(users) - set(existing_users))
        existing_number_of_users = len(existing_users)
        vacant = 50 - existing_number_of_users
        extra_users = users[vacant:]
        users = users[:vacant]

        for a_user in users:
            team_map = TeamUsersMapping.objects.get_or_create(team_id=team_id, user_id=a_user.id)
            team_map.active = True
            team_map.save()

        res = {
            "status": "added"
        }
        if len(extra_users) > 0:
            res["extra_users"] = extra_users
        res = json.dumps(res)

        return res

    # add users to team
    def remove_users_from_team(self, request: str):
        """
        :param request: A json string with the team details
        {
          "id" : "<team_id>",
          "users" : ["user_id 1", "user_id2"]
        }

        :return:

        Constraint:
        * Cap the max users that can be added to 50
        """
        data = json.loads(request)

        team_id = data["id"]
        users = data["users"]

        TeamUsersMapping.objects.filter(team_id=team_id, user_id__in=users).update(active=False)
        return "updated"

    # list users of a team
    def list_team_users(self, request: str):
        """
        :param request: A json string with the team identifier
        {
          "id" : "<team_id>"
        }

        :return:
        [
          {
            "id" : "<user_id>",
            "name" : "<user_name>",
            "display_name" : "<display name>"
          }
        ]
        """
        data = json.loads(request)

        team_id = data["id"]
        user_ids = TeamUsersMapping.objects.filter(team_id=team_id, active=True).values("user_id")
        user_objs = User.objects.filter(id__in=user_ids, active=True)

        res = []
        for a_user in user_objs:
            res.append(
                {
                    "id": a_user.id,
                    "name": a_user.name,
                    "display_name": a_user.display_name
                }
            )
        res = json.dumps(res)
        return res
