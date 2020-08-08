# Covin Task
- Description of Task\
    In this assignment, you will be implementing the following using Django \
    Create two models as follows:-\
    - Task -> task should have task_type(integer) and task_desc(string)
    - TaskTracker -> tracker should have task_type(type of task to track), update_type(per day, weekly or monthly) and email
    - Create apis to create and update tasks, task types can be pre-defined(let's say 1,2,3 and 4). Throw error if task type is not valid
    - Create api to create TaskTracker.
    - Create a background task using django-celery which should send email updates to users based on TaskTracker objects.
   
## Installation
1. Clone the repository using
    - `git clone https://github.com/RifasM/Convin.git`
    - or
    - `git clone git@github.com:RifasM/Convin.git` - Needs SSH Keys
2. Create a virtual environment
    - `vitualenv venv`
3. Activate the virtual environment
    - Ubuntu
        - `source venv/bin/activate`
    - Windows
        - `cd venv/Scripts`
        - `activate`
4. `pip install -r requirements.txt`
5. Import `SECRETS (API Keys, DJANGO_SECRET, etc)` into Operating System Environment
    - Ubuntu
        - Edit `~/.bashrc` and add the secrets
    - Windows
        - Add to environment variable in system
    - Set it up in IDE Environment Variables
        - Refer [this](https://code.visualstudio.com/docs/python/environments) for VSCode
        - Refer [this](https://www.jetbrains.com/help/pycharm/console-python-console.html) for Pycharm
6. Run 
    - `celery -A Convin worker -l info`
        - If no errors, proceed by pressing `Ctrl+C`
        - Errors - Check if redis is started by running:
            - `redis-server` on terminal
            - Confirm by `redis-cli ping`
    - On a separate terminal 
        - `celery -A Convin beat -l info`
    - `python manage.py makemigrations`
    - `python manage.py migrate`
    - `python manage.py createsuperuser`
        - Follow steps to create your account
    - `python manage.py runserver`
7. Navigate to `localhost:8000`
8. Log in to Created Account to query on endpoints

# Note
- Authenticated Users allowed to make calls such as `PUT`, `POST`, `DELETE`
- Un-Authenticated Users allowed to view
- Click on the endpoint to avail options such as `POST` and `DELETE`
- Added Checks to check for duplicated emails
- Emails send using Celery Task with Redis at Scheduled times
    - Weekly -> Every Monday
    - Daily -> Every day at 5 pm
    - Monthly -> First day of month


# View Screenshots
- Click [here](Screenshots/README.md)