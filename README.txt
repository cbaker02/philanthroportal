Steps to create a Virtual Environment to run:
In CMD navigate to folder with project
  python -m venv env1
  env1\Scripts\activate (Windows) or env1/bin/activate (Linux)
  pip install django
  pip install "django-phonenumber-field[phonenumbers]"
  pip install pillow
  pip install django-resized
  python manage.py runserver

Logins:
  -Can navigate around the website without an account
  -Here are three accounts, one for each user type to navigate to additional pages:
  Non-for-profit:
    email - info@goodwill.org
    password - MtAR5-c9eH.n4Xx
  Corporation:
    email - info@cliffamilyfoundation.org
    password - 7iCK!ncBFSAADqN
  Individual:
    email - crb190003@utdallas.edu
    password - philanthro1
  -Additionally, feel free to register a new user or access any other accounts we have created that is listed in our "Fake   Data" Sheet available in our repo
