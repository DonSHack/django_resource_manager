# Resource Manager

This is an sample application to manage employees and companies using django framework. This will be help to learn the dejango basic concept and how to use them in real scenario. **Django** is a real eazy but strong framework to build web application. **Django** use Python as the programming language.


# Prerequisites

To run this application followings are required.
>python 3.6 or higher version
>mysql installed
>Django 2.1 or higher version

## Steps to run application

Step 1:
	Clone the repository https://github.com/DonSHack/django_resource_manager.git
Step2:
	Create a python3 virtual environment and activate it.
   

	python -m venv <env_name> 
	source <path_to_env>/bin/activate
Step3:
install  **Django** framework
	

    pip install django	

Step4:
install  all the requirements

    pip install -r requirements.txt
Step5:
Migrate the database

    python manage.py migrate

Step6:
Navigate to the project directory and create superuser using **Django** command

    python manage.py createthesuperuser

(Enter the username email and password appropriately)

Step7:
Run the development server and then goto http://localhost:8000

    python manage.py runserver
