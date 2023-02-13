# Full-stack-take-home-assignment

How to set up Django in Ubuntu:

Step 01: Clone Repository
```
  git clone https://github.com/zunerazaidi/Full-stack-take-home-assignment.git
```

Step 02: Setup environment on Ubuntu:

- Check version of Python using
```
python3 -V
```
- Create Virtual Environment using 
```
python3 -m venv <env_name>
```
- Activated it by using:
```
source <env_name>/bin/activate
```
- For installation:
```
pip install -r requirements.txt
```
- Migration commands:
```
python manage.py makemigrations
python manage.py migrate
```
```
python manage.py collectstatic
```
- Create SuperUser:
```
python manage.py createsuperuser
```
Note: If you selected Role: Admin as a superuser, you will be able to add Regular members in application but if you selected Role: Regular, you won't be able to add new members in application.

Step 03: Testing a Server:

- Run server using:
```
python3 manage.py runserver        ---> Success
```
Steps to execute application:

- There are 2 roles in application for now: Admin and Regular. Admin can add new member, update any information of the member and delete any member except for himself while Regular have only rights to change its own information.

1- Flow for Admin:

- First page is Login Page, enter email and password you set for superuser. If you enter wrong details it won't proceed to Member list page but if you enter right details ii will proceed to Member list page.
- Because you register only one member which is superuser, you will be able to see only 1 Member in list. 
- Now add another member by clicking "+" symbol on page. Add Member information and Save it.
- The application will redirect to Member list page and you can see that now there are 2 Members in list.
- If Admin wants to delete any member, click on the specific user name and delete the member by clicking delete button. Admin will redirect to member list page and ypu can see that deleted member is no longer available in the team list.
- If Admin wants to change its information, he/she can click on the name and the edit page will open. On save button, information will be save and the page will redirect to Member list page.
- On clicking logout button, admin will logout from application.

2- Flow for Regular User:

- On login page, regular user will add email and password added by the Admin. By entering right credentials, Member list page open where list of all team members are displayed. You can see there is no "+" symbol on page because Regular user is not authorized to add any new member.
- Regular user can change his/her information by clicking own name, edit new information and click on save button. 
- After saving, user will redirect to Member list page.
- On clicking logout button, user will logout from the session.

Future Plans:

- Forgot Password functionality, in which user will get an email to reset the password.
- User will be able to upload picture in add/update page