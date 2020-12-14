import os, subprocess

class Creator():
    s_DefaultAppName            = "app"
    s_DefaultImage              = "python:3.9-alpine"
    s_DefaultTag                = "rohitrohitrohit/django-unchained"
    s_DefaultComposeVersion     = "3.7"
    s_DefaultModuleName         = "module"

    def __init__(self):
        # First we need to get the user input for what the app will be called
        self.setInputs()

        # Store the working directory of this program
        self.s_cwd  = os.getcwd()

        # We need to create a Django project (named by user) located in our current directory
        self.createDjangoProject()

        # We also need to create a Dockerfile
        self.createDockerfile()

        # and finally a docker-compose file
        self.createDockerCompose()
        
    def setInputs(self):
        s_NameInput = input(f"Enter the name for your app (leave blank for '{self.s_DefaultAppName}'): ")
        if s_NameInput == "":
            print(f"\tNo input provided, using default app name: '{self.s_DefaultAppName}'")
            self.s_AppName  = self.s_DefaultAppName
            return
        else:
            self.cleanNameInput(s_NameInput)
        s_TagInput  = input(f"Do you have a special tag for this container? (leave blank if not): ")
        if s_TagInput == "":
            print(f"\tNo input provided, using default tag name: '{self.s_DefaultTag}'")
            self.s_TagName  = self.s_DefaultTag
        else:
            self.s_TagName = s_TagInput
        s_ImageInput  = input(f"Do you have a special Docker image for this project? (leave blank for {self.s_DefaultImage}): ")
        if s_ImageInput == "":
            print(f"\tNo input provided, using default image: '{self.s_DefaultImage}'")
            self.s_Image  = self.s_DefaultImage
        else:
            self.s_Image    = s_ImageInput

        s_ComposeVersionInput  = input(f"Do you have a special compose version for this project? (leave blank for {self.s_DefaultComposeVersion}): ")
        if s_ComposeVersionInput == "":
            print(f"\tNo input provided, using default compose version: '{self.s_DefaultComposeVersion}'")
            self.s_ComposeVersion   = self.s_DefaultComposeVersion
        else:
            self.s_ComposeVersion   = self.s_ComposeVersionInput

    def cleanNameInput(self, s_NameInput):
        print(f"Checking if {s_NameInput} is a valid app name...")
        if s_NameInput.isalpha():
            self.s_AppName = s_NameInput
            print(f"\t{s_NameInput} is valid, using app name: '{self.s_AppName}'")
            return
        else:
            raise ValueError(f"\napp name must only contain letters, you have provided: {s_NameInput}")

    def createDjangoProject(self):
        s_BashCommand   = f"django-admin startproject {self.s_AppName}"
        a_BashCommand   = s_BashCommand.split()

        process = subprocess.Popen(a_BashCommand, stdout=subprocess.PIPE)
        output, error = process.communicate()

    def createDockerfile(self):
        # Create the dockerfile, append lines to it one at a time
        f_Dockerfile    = open("Dockerfile", "w")
        # This line is where we import our base image from
        f_Dockerfile.write(f"FROM {self.s_Image}\n")
        # In our base image, enter a new folder, app
        f_Dockerfile.write(f"WORKDIR /app/\n")
        # Copy our requirements file to be installed in our container
        f_Dockerfile.write(f"COPY ./requirements.txt ./requirements.txt\n")
        # Temporarily install anything we need for our requirements.txt install
        f_Dockerfile.write(f"RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers\n")
        # Install what is specified in requirements.txt
        f_Dockerfile.write(f"RUN pip install -r ./requirements.txt\n")
        # Delete all the temporary tools we needed
        f_Dockerfile.write(f"RUN apk del .tmp\n")
        # Copy our data from host to container
        f_Dockerfile.write(f"COPY ./{self.s_AppName} ./\n")
        # Command to be executed
        f_Dockerfile.write(f"CMD [\"python\", \"{self.s_AppName}/manage.py\", \"runserver\", \"0.0.0.0:8000\"]")
        # Close the file
        f_Dockerfile.close()

    def createDockerCompose(self):
        # Create the docker-compose.yml file
        f_DockerComposefile    = open("docker-compose.yml", "w")
        # Set the version to the number provided by the user
        f_DockerComposefile.write(f"version: '{self.s_ComposeVersion}'\n")
        # Define our services
        f_DockerComposefile.write(f"services:\n")
        #   Start with our app
        f_DockerComposefile.write(f"    app:\n")
        #       Outline the build
        f_DockerComposefile.write(f"        build:\n")
        #           Locate where the Dockerfile will be (. is current directory)
        f_DockerComposefile.write(f"            context: .\n")
        #       Connect our container ports to our host ports
        f_DockerComposefile.write(f"        ports:\n")
        #           Specifically, connect our 8000 port to 8000
        f_DockerComposefile.write(f"            - \"8000:8000\"\n")
        #       Define our shared volumes
        f_DockerComposefile.write(f"        volumes:\n")
        f_DockerComposefile.write(f"            - ./{self.s_AppName}:/{self.s_AppName}\n")
        #       The closing command
        f_DockerComposefile.write(f"        command: sh -c \"python app/manage.py runserver 0.0.0.0:8000\"\n")
        f_DockerComposefile.write(f"        environment:\n")
        f_DockerComposefile.write(f"            - DEBUG=1\n")
        f_DockerComposefile.write(f"\n")
        f_DockerComposefile.write(f"volumes:\n")
        f_DockerComposefile.write(f"    shared:\n")
        f_DockerComposefile.write(f"    {self.s_AppName}:")
        f_DockerComposefile.close()


def main():
    o_Creator   = Creator()

if __name__=="__main__":
    main()