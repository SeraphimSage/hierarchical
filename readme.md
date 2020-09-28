# Data hierarchy's and you.

## Why bother with this project?
This app helps to better learn and visualize how data can be stored in Django.

In this app we explore tree type data structures.

To do this we will be using MPTT, or Modified Preorder Tree Traversal.

This will allow us to get all of the data attached to a "root" folder and display it on one page.

## So let's dive in
### Depencies required for this project
* Linux or Mac OS
* A Bash or Zsh shell
* Python 3.8+
* Poetry

Once you have those all in place feel free to fork and clone this repo, then continue on.

To get this running in the terminal let's get a few things setup.

```
cd into the directory you just cloned

poetry install - installs all of the dependices you need for you

poetry shell - creates the virtual environment needed to run the project.

python manage.py createsuperuser - creates a login for an admin user so you can modify the site through the admin panel.

python manage.py runserver - this starts the server up for you.

To get into the site (on Linux) CTRL + left click on the IP address that is returned to your terminal.

If you need to get to the admin site. type "/admin" without the quotes into the URL bar after the IP address you went to.

Happy Hacking!
```