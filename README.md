# chat-app
Django chat application using WebSockets for real-time message sending,
implemented on the backend using django-channels.

# setup and installation
To get started with the project:

<br>On a windows operating system
```
#setup a virtual environment
$ python -m venv .env

#start the virtual environment
$ .env/Scripts/activate

#clone the repository (or simply download the zip)
$ git clone https://github.com/K-Kelvin/chat-app.git

#navigate to the project directory
$ cd chat-app

#install the dependencies
$ pip install -r requirements-windows.txt

#start the server
$ python manage.py runserver 8001
```

<br> On a linux operating system
```
#setup a virtual environment
$ python3 -m venv .env

#start the virtual environment
$ source .env/bin/activate

#clone the repository (or simply download the zip)
$ git clone https://github.com/K-Kelvin/chat-app.git

#navigate to the project directory
$ cd chat-app

#install the dependencies
$ pip install -r requirements-linux.txt

#start the server
$ python3 manage.py runserver 8001
```