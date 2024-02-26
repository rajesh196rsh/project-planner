import json
from .models import ProjectBoard, Team, Task, User
import pandas as pd


class ProjectBoardBase:
    """
    A project board is a unit of delivery for a project. Each board will have a set of tasks assigned to a user.
    """

    # create a board
    def create_board(self, request: str):
        """
        :param request: A json string with the board details.
        {
            "name" : "<board_name>",
            "description" : "<description>",
            "team_id" : "<team id>"
            "creation_time" : "<date:time when board was created>"
        }
        :return: A json string with the response {"id" : "<board_id>"}

        Constraint:
         * board name must be unique for a team
         * board name can be max 64 characters
         * description can be max 128 characters
        """
        data = json.loads(request)

        if len(data["name"]) > 64:
            raise ValueError("Board name cannot exceed 64 characters")
        if len(data["description"]) > 128:
            raise ValueError("Description cannot exceed 128 characters")

        team = Team.objects.get(id=data["team_id"])
        board_obj = ProjectBoard.objects.create(name=data["name"], description=data["description"], team=team)

        res = {
            "id": board_obj.id
        }
        res = json.dumps(res)
        return res

    # close a board
    def close_board(self, request: str) -> str:
        """
        :param request: A json string with the user details
        {
          "id" : "<board_id>"
        }

        :return:

        Constraint:
          * Set the board status to CLOSED and record the end_time date:time
          * You can only close boards with all tasks marked as COMPLETE
        """
        data = json.loads(request)

        board_obj = ProjectBoard.objects.filter(id=data["id"])
        if board_obj:
            board_obj = board_obj[0]

            tasks = board_obj.tasks
            for a_task in tasks:
                _ = self.update_task_status(json.dumps({
                    "id": a_task.id,
                    "status": "COMPLETE"
                }))

            board_obj.status = "CLOSED"
            board_obj.save()
        else:
            res = "Board does not exists"

        return res


    # add task to board
    def add_task(self, request: str) -> str:
        """
        :param request: A json string with the task details. Task is assigned to a user_id who works on the task
        {
            "title" : "<board_name>",
            "description" : "<description>",
            "user_id" : "<team id>"
            "creation_time" : "<date:time when task was created>"
        }
        :return: A json string with the response {"id" : "<task_id>"}

        Constraint:
         * task title must be unique for a board
         * title name can be max 64 characters
         * description can be max 128 characters

        Constraints:
        * Can only add task to an OPEN board
        """
        data = json.loads(request)

        if len(data["title"]) > 64:
            raise ValueError("Task name cannot exceed 64 characters")
        if len(data["description"]) > 128:
            raise ValueError("Description cannot exceed 128 characters")

        task_obj = Task.objects.create(name=data["title"], description=data["description"])
        user = User.objects.get(id=data["user_id"])
        task_obj.user = user
        task_obj.save()

        res = {
            "id": task_obj.id
        }
        res = json.dumps(res)
        return res

    # update the status of a task
    def update_task_status(self, request: str):
        """
        :param request: A json string with the user details
        {
            "id" : "<task_id>",
            "status" : "OPEN | IN_PROGRESS | COMPLETE"
        }
        """
        data = json.loads(request)

        task_obj = Task.objects.get(id=data["id"])
        if task_obj:
            task_obj = task_obj[0]
            task_obj.status = data["status"].upper()
            task_obj.save()
            res = "updated"
        else:
            res = "Task does not exists"
        return res


    # list all open boards for a team
    def list_boards(self, request: str) -> str:
        """
        :param request: A json string with the team identifier
        {
          "id" : "<team_id>"
        }

        :return:
        [
          {
            "id" : "<board_id>",
            "name" : "<board_name>"
          }
        ]
        """
        data = json.loads(request)

        boards_objs = ProjectBoard.objects.filter(team__id=data["team_id"], active=True)
        res = []
        for a_board in boards_objs:
            res.append(
                {
                    "id": a_board.id,
                    "name": a_board.name
                }
            )
        res = json.dumps(res)

        return res

    def export_board(self, request: str) -> str:
        """
        Export a board in the out folder. The output will be a txt file.
        We want you to be creative. Output a presentable view of the board and its tasks with the available data.
        :param request:
        {
          "id" : "<board_id>"
        }
        :return:
        {
          "out_file" : "<name of the file created>"
        }
        """
        data = json.loads(request)

        board_id = data["id"]
        board_obj = ProjectBoard.objects.filter(id=board_id)
        if board_obj:
            board_obj = board_obj[0]
            team_id = board_obj.team.id
            team_name = board_obj.team.name
            out_file_name = str(board_id) + "__" + board_obj.name + ".csv"

            board_data = []
            tasks = board_obj.tasks
            for a_task in tasks:
                a_board_data = []

                a_board_data.append(team_id)
                a_board_data.append(team_name)
                a_board_data.append(a_task.id)
                a_board_data.append(a_task.name)
                a_board_data.append(a_task.description)
                a_board_data.append(a_task.user.id)
                a_board_data.append(a_task.user.name)
                a_board_data.append(a_task.user.display_name)
                a_board_data.append(a_task.status)
                a_board_data.append(a_task.created_at)
                a_board_data.append(a_task.updated_at)

                board_data.append(board_data)

            # creating df
            columns = ["team_id", "team_name", "task_id", "task_name", "task_description", "user_id", "user_name", "user_display_name", "status", "created_at", "updated_at"]
            df = pd.DataFrame(board_data, columns=columns)

            # saving the dataframe
            df.to_csv(out_file_name)
            res = out_file_name
        else:
            res = "Board does not exist"
        return res
