# project-planner
Project planner tool

## Overview

This Django project provides APIs for managing users, teams, tasks, and project boards. Users can be associated with teams, and tasks can be assigned to users. Project boards are used to organize tasks within a team.

## Models

### User
- `name`: Unique username
- `display_name`: Display name of the user
- `active`: Boolean indicating user's active status
- `created_at`: Timestamp of user creation
- `updated_at`: Timestamp of last user update

### Team
- `name`: Unique team name
- `description`: Team description
- `active`: Boolean indicating team's active status
- `created_at`: Timestamp of team creation
- `updated_at`: Timestamp of last team update

### TeamUsersMapping
- `team_id`: Foreign key to Team model
- `user_id`: Foreign key to User model
- `active`: Boolean indicating mapping's active status
- `created_at`: Timestamp of mapping creation
- `updated_at`: Timestamp of last mapping update

### Task
- `name`: Task name
- `description`: Task description
- `user`: Foreign key to User model (can be null)
- `status`: Task status (OPEN, IN_PROGRESS, COMPLETE)
- `created_at`: Timestamp of task creation
- `updated_at`: Timestamp of last task update

### ProjectBoard
- `name`: Unique project board name
- `description`: Project board description
- `team`: Foreign key to Team model (can be null)
- `tasks`: Many-to-Many relationship with Task model
- `status`: Project board status (OPEN, CLOSED)
- `active`: Boolean indicating project board's active status
- `created_at`: Timestamp of project board creation
- `updated_at`: Timestamp of last project board update


1. Clone the repository:

   git clone https://github.com/rajesh196rsh/project-planner.git
   cd project-planner

2. Create virtual env
    virtualenv venv

3. Activate env
    source venv/bin/activate

4. Install Requirements
    pip install -r requirements.txt

5. Apply migrations
    python manage.py migrate

6. Run Server
    python manage.py runserver

7. Visualize all models on
    http://127.0.0.1:8000/admin/
