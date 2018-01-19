# XMTInventory
Inventory Management System for XMT Technologies Sdn. Bhd.

This system is designed to replace the current method of recording inventory for XMT Technologies Sdn. Bhd.

Written in Python using Django Framework

Other dependencies:
1. Jquery
2. JqueryUI
3. django-rest-framework
4. Bootstrap 4

# Installation

1. Download and install python 3.6 at https://www.python.org/downloads/ . Ensure correct installation by executing command"python --version" on command line
2. Install django web framwork by following this tutorial https://www.youtube.com/watch?v=qgGIqRFvFFk&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK&index=1 or executing "pip install django"
3. Install django-rest-framework by executing "pip install djangorestframework" on the command line.
4. Download the source code and place in any directory on the server or computer.
5. Navigate to the root directory where the source code is located.
6. Run the webserver by executing "python manage.py runserver".
7. The site can be accessed at http://127.0.0.1:8000

# Admin Panel

1. Create a new user by execeuting "python manage.py createsuperuser" at the site directory
2. Follow the instruction (enter email and password)
3. Access the admin panel at http://127.0.0.1:8000/admin
4. The admin panel is used to delete inventories, create new customer, staff, tenants, location and person in charge.
5. The same email and password is used to log in into the system.

# Database Structure
1. View the database structure by opening the db.sqlite3 file using this software http://sqlitebrowser.org/

# Backing up database

1. Simply copy the db.sqlite3 file and save it without changing the filename i.e The filename always needs to be "db.sqlite3"
2. Restore the database by copying the file into the root folder.

# Tutorials

1. Understanding the Django Python web framework will help dramatically to understand the source code. A playlist for django tutorial is here https://www.youtube.com/watch?v=qgGIqRFvFFk&index=1&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK . The official reference is https://docs.djangoproject.com/en/2.0/
2. Jquery. Jquery is an essential part in processing the clients input at interaction and sending requests to the server. The simple https://www.w3schools.com/Jquery/default.asp , the official documentation http://api.jquery.com/ or the e book (best and complete reference) http://web-algarve.com/books/JS%20AJAX%20jquery%20&%20angular/JavaScript%20&%20jQuery-%20The%20Missing%20Manual,%203rd%20Edition.pdf .
3. JSON. The data formatting for sending and receiving request. This reference is enough https://www.w3schools.com/js/js_json_intro.asp
4. JqueryUI. Handling the dialog and datepicker http://api.jqueryui.com/
5. Bootstrap. The main part to make this site look pretty https://v4-alpha.getbootstrap.com/getting-started/introduction/

# Imporvement
Please do not hesitate to contact me at muhammad.zafran@outlook.com



