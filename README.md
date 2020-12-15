![alt text](https://github.com/RohitKochhar/django-unchained/blob/main/logo.png?raw=true)
# Automatic Creation and Containerization of Django Applications

a containerized app to make containerized apps

## Abstract

`django-unchained` is a [Docker](https://www.docker.com) image used to create templated, containerized [Django](https://www.djangoproject.com/) applications, along with both a templated [Dockerfile](https://docs.docker.com/engine/reference/builder/) and templated [docker-compose](https://docs.docker.com/compose/) file 

## How it works

This is a systems-level overview of the package. For technical usage, look below.

By executing the following command:

`$ docker run -v $(pwd)/output:/output -it rohitrohitrohit/django-unchained`

We are saying a few things:
    - We are telling docker that we want to run the image rohitrohitrohit/django-unchained interactively (-it). 
        - First, Docker checks if this image, rohitrohitrohit/django-unchained exists on your local machine. If it doesn't it is pulled from [Docker Hub](https://hub.docker.com/repository/docker/rohitrohitrohit/django-unchained).
    - We are also telling docker that we want to share a volume (-v) with this image. That means that there will be a folder which contains data for both our Host and out image, the rest of the two systems are isolated.
        - Here we are saying that the volume should be called `output` on both the host and container (host-location:container-location).
        - We use $(pwd) since docker requires that the argument to the -v flag be an absolute path.

Once this command is run, the image is retrieved remotely and then run interactively on your host machine. 
    - When our container starts running, it will automatically execute `unchained.py`, which starts and waits for the users input.
    - Once the user input is provided, the image will create the relevant files and skeleton app files and save them in the shared volume, which is `output` by default.
    - After the files are created, the container exits and the files are available for the user in the `output` folder.

## Requirements

All you need to have pre-installed to use this package is Docker. I'm not going to explain how to download Docker, since it is so well documented on their website.

### Docker Usage

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

### Bug Reports

Please report any bugs to rkochhar@uwaterloo.ca

