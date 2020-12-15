![alt text](https://github.com/RohitKochhar/django-unchained/blob/main/logo.png?raw=true)
# Automatic Creation and Containerization of Django Applications

a containerized app to make containerized apps

## Abstract

`django-unchained` is a template engine for containerized [Django](https://www.djangoproject.com/) applications, all contained within it's own [Docker](https://www.docker.com) container, invoked by one call.

`django-unchained` is run as a Docker container hosted on Docker Hub. It will ask you some base questions about your project and then create a skeleton app along with both a Dockerfile and docker-compose.yml file, creating a containerized skeleton Django container within seconds.

## Requirements

All you need to have pre-installed to use this package is Docker. I'm not going to explain how to download Docker, since it is so well documented on their website. 

### Docker Installation

1. In your terminal (with Docker installed), run the following command:

`$ docker run -v $(pwd)/output:/output -it rohitrohitrohit/django-unchained`

This will create a folder `output` in your current directory, and will ask you some questions about how to set up your Django app. You can leave them all blank for default answers. If you want to store the output files in another directory, say for example `django-app`, you would use the following command:

**For steps below, it is assumed that all default prompts were selected in the previous step**

`$ docker run -v $(pwd)/django-app:/output -it rohitrohitrohit/django-unchained`

The rest of this description will assumed you have name this folder `output`

2. Navigate into the created `output` directory:

`$ cd output`

Here we have 2 files:

- Dockerfile: This is the file which Docker reads to create our image. Each file here is an operation which we tell Docker to perform on some base OS image.
- docker-compose.yml: This is a file which starts and configures multiple containers. Since this is only a template generator, only the simple app class is included at the start

We also have 1 folder. This folder will be named whatever input was given to the container when step #1 was executed. This is our skeleton django app.

3. Start up our container using our docker-compose file:

`$ docker-compose up`

4. This will build your sample app, which is contained within the folder we saw in our `output` folder. We can verify this step is working by going to our browser [http://localhost:8000](http://localhost:8000) to the Django welcome page

5. At this point, you can navigate into your app container, and start hacking!

`cd app`

This is where you find you Django app. If you don't know what to do from here, Django has an amazing tutorial here on it's [website](https://docs.djangoproject.com/en/3.1/intro/tutorial01/). If you follow this tutorial, we have already completed the first steps in creating the project, and the step that contextually follows development after we have created our project is the step in which we run

`python manage.py startapp polls`

