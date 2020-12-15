![alt text](https://github.com/RohitKochhar/django-unchained/blob/main/logo.png?raw=true)
# Automatic Creation and Containerization of Django Applications

an app to make apps

## Abstract

django-unchained is a template engine for containerized Django applications.

unchained.py is a CLI which takes in some user input variables and creates a skeleton Django application along with a Dockerfile to build the image and a docker-compose file for awesome local development

## Requirements

The install process requires that the host machine either be linux/unix-based, or if Windows, WSL must be active and enabled. This is to ensure consistency with the relevant Docker files.

Docker must also be installed on the host machine, not to run this package but instead to run the products of this package, like your applications Dockerfile and docker-compose.yml.

This template engine can be used without Docker installed, and will still generate the associated Dockerfile and docker-compose.yml file and the app as expected, but container advantages will be unavailable.

Finally Python and pip are also required to run the `unchained.py` program.

### GitHub

1. In your terminal (with Git installed), run the following command to collect the source code:

`git clone https://github.com/RohitKochhar/django-unchained.git`

2. Change into the repository directory:

`cd django-unchained`

