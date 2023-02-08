# Full-stack-take-home-assignment

Step 01: Setup Django on Ubuntu:

- Firstly check version of Python:
  python3 -V
- Install Django on my system:
  sudo apt install python3-django
- Check installation version with:
  django-admin -version


Step 02: Created a Project:

- Created a directory for the project and switch to it
- Create virtual environment:
  python3 -m venv djangoenv
- Activated it by using:
  source djangoenv/bin/activate
- Install Django:
  pip install django
- Created startproject using admin command:
  django-admin startproject
- Migrate it to database using:
  python manage.py migrate
- Created superuser:
  python manage.py createsuperuser

Step 03: Testing of Development Server:

- Use admin command to build the project:
  django-admin startproject django_project
- Execute command on terminal to check project:
  python3 manage.py runserver

Step 04: Create new startapp "pages" using:
python manage.py startapp Pages

Step 05: Create templates folder in root directory and create 3 new html files to generate 3 pages shown in pdf file. Html files are:

- team_member_list.html: This will be the first page in web app that shows list of all team members within a team.
- edit_team_member.html: This file is responsible for showing html page when user wants to edit any team member information.
- add_team_member.html: This file is responsible for showing html page when user wants to add any new team member.

Step 06: In settings.py of root directory, add [os.path.join(BASE_DIR, 'templates')] in directory->Template section.

Step 07: Created 3 functions for each html file in views.py of pages. These functions render all 3 html pages.

Step 08: Write urls for each html file within pages->urls.py and then call this pages->urls.py in django_project->urls.py which is the root directory.

Step 09: Run server to check if everything is working till now or not i.e., Result->Success

Step 10: Download basic admin theme, url is: https://medium.com/djangotube/tomdjango-use-startbootstrap-theme-in-project-50ae96ed2e0e and follow all steps written as mentioned in the link.

Step 11: After following all steps mentioned on the theme website, i realized there were some errors related to static folder so i came to the solution that the static folder is outdated and the latest one is staticfiles, as i am using latest version of django so i need to set up latest folder. I followed some basic steps which was mentioned in django website and after that all errors were gone.

Step 12: Created public repository on GitHub and commit, push all changes to github.

Step 13: Adding HTML code for 3 pages: List of Team Members, Add Team Member, Edit/Delete Team member

Step: Create login page

Created SuperUser from following commands:
python manage.py createsuperuser
Username: admin
email: admin@instawork.com
password: 12345

python manage.py runserver
http://127.0.0.1:8000/admin/
login with registered user

Creation of Database Table using models.py
python manage.py migrate
python manage.py makemigrations pages
python manage.py sqlmigrate pages
