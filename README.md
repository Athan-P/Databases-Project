# ELIDEK

This is a project for the Databases class in NTUA Electrical and Computer Engineering Department 

## Contributors
Listed alphabetically:
1. Nastou Savvina
1. Papadopoulos Theodoros
1. Pyliotis Athanasios

## Dependencies

 - [MySQL](https://dev.mysql.com/downloads/workbench/) for Windows
 - [XAMPP](https://www.apachefriends.org/download.html) For Windows
    - It is possible that XAMPP cannot configure python. You should follow these steps:
      - Open XAMPP Control Panel
      - Start Apache and MySQL (you should do that no matter)
      - From Apache open Config and press Apache (httpd.conf)
      - ctrl+f and search for `AddHandler` and add .py at the end
 - [Python](https://www.python.org/downloads/), with the additional libraries:
    - [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    - [Flask-MySQLdb](https://flask-mysqldb.readthedocs.io/en/latest/)
    - [Flask-WTForms](https://flask-wtf.readthedocs.io/en/1.0.x/)

## Creating our Database Folder

Inside Windows PowerShell (make sure to *Run as Administrator*): Use `pip3 install <package_name>` to install each individual Python package (library) directly for the entire system. It is advised to create a virtual environment with the [`venv`](https://docs.python.org/3/library/venv.html) module. You should run `py -3 -m venv <VE_name>` to create your virtual environment and inside of it you can download the necessary packages. Use `<VE_name>\Scripts\activate` to activate it and then `cd <VE_name>` to get into the virtual environment. In case it doesn't activate, use `Set-ExecutionPolicy RemoteSigned` and then `Set-ExecutionPolicy Restricted` when you finish using the Web Application. 

The necessary packages for this app are listed in [`requirements.txt`](https://github.com/Athan-P/Databases-Project/blob/main/requirements.txt) and can be installed all together via `pip install -r requirements.txt`. The Virtual Environement should be preferable in the htdocs file of xampp for Windows. Your Database files should all be inside the Virtual Environment, after you download and unzip it from GitHub.

## Creation of the Database

Through Workbench, after having established connection with XAMPP, open the 2 SQL files provided to [`Create the Schema`](https://github.com/Athan-P/Databases-Project/blob/main/schemaright.sql) and to [`Insert Data`](https://github.com/Athan-P/Databases-Project/blob/main/insert.sql). Execute them both in this order.

## Project Structure

A package named "`ELIDEK`", contains the application's code and files, separated into folders for each category (models, controllers, HTML templates - views, static files such as css or images).

 - `__init__.py` configures the application, including the necessary information and credentials for the database
 - `forms.py` contains the necessary forms/classes that were used for this application
 - `routes.py` currently contains all the endpoints and corresponding controllers
 - `run.py` launches the simple, built-in server and runs the app on it

When inside the Database, Run via the `setx FLASK_APP "Run.py"` command, to set the environment variable `FLASK_APP` to `run.py`, and then use `flask run`.

## Screenshots

![landing1](https://user-images.githubusercontent.com/59802631/172061833-fb437523-4930-4da7-bfa3-39b420d663ee.png)

![landing2](https://user-images.githubusercontent.com/59802631/172061870-73f3ad21-b39d-4d37-9421-3876a3a3707e.png)

![Projects](https://user-images.githubusercontent.com/59802631/172061906-b70cf51e-c8f4-4d34-8d5a-11363ade6498.png)

![Create Researchers](https://user-images.githubusercontent.com/59802631/172061936-c5dab42e-6c6e-45cf-9dbc-1710106a68f8.png)

![Filters of Projects](https://user-images.githubusercontent.com/59802631/172061963-f533dbf9-f673-43b0-9f68-009e87de3857.png)

![View of query 3.5](https://user-images.githubusercontent.com/59802631/172061990-9fa4dc0b-e203-4b5d-8c8a-8bfb6d954cf4.png)
