import subprocess

class Template():
    s_DefaultAppName    = "app"
    s_DefaultImage      = "python:3.9-alpine"
    s_DefaultTag        = "rohitrohitrohit/django-unchained"

    def __init__(self, s_NameInput):
        self.setNameInput(s_NameInput)

        self.writeOutputFile()

    def setNameInput(self, s_NameInput):
        if s_NameInput == "":
            print(f"No input provided, using default app name: '{self.s_DefaultAppName}'")
            self.s_AppName  = self.s_DefaultAppName
            return
        else:
            self.cleanNameInput(s_NameInput)

    def cleanNameInput(self, s_NameInput):
        print(f"Checking if {s_NameInput} is a valid app name...")
        if s_NameInput.isalpha():
            self.s_AppName = s_NameInput
            print(f"\t{s_NameInput} is valid, using app name: '{self.s_AppName}'")
            return
        else:
            raise ValueError(f"\napp name must only contain letters, you have provided: {s_NameInput}")

    def writeOutputFile(self):
        f_Output    = open("./config/appconfig.txt", "w")
        f_Output.write(f"app_name={self.s_AppName}")
        f_Output.close()

    def createDockerfile(self):
        f_Dockerfile    = open("Dockerfile", "w")
        f_Dockerfile.write(f"FROM {self.s_DefaultImage}\n")
        f_Dockerfile.write(f"WORKDIR /django-app/\n")
        f_Dockerfile.write(f"COPY ./config ./config\n")
        f_Dockerfile.write(f"COPY ./shared ./shared\n")
        f_Dockerfile.write(f"RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers\n")
        f_Dockerfile.write(f"RUN pip install -r ./shared/requirements.txt\n")
        f_Dockerfile.write(f"RUN apk del .tmp\n")
        # ToDo: Change this to pull from my github or something
        f_Dockerfile.write(f"COPY creator.py ./creator.py\n")

        f_Dockerfile.write(f"RUN python creator.py\n")
        f_Dockerfile.write(f"CMD [\"python\", \"{self.s_AppName}/manage.py\", \"runserver\", \"0.0.0.0:8000\"]")
        f_Dockerfile.close()

    def buildDockerImage(self):
        s_BashCommand   = f"docker build -t {self.s_DefaultTag} ."
        a_BashCommand   = s_BashCommand.split()
        process = subprocess.Popen(a_BashCommand, stdout=subprocess.PIPE)
        output, error = process.communicate()

    def runDockerImage(self):
        s_BashCommand   = f"docker run -p 8000:8000 --rm {self.s_DefaultTag}"
        a_BashCommand   = s_BashCommand.split()
        process = subprocess.Popen(a_BashCommand, stdout=subprocess.PIPE)
        output, error = process.communicate()
        print(output)


class TemplateTester():
    i_SuccessCount  = 0
    i_TestCount     = 2

    def __init__(self):
        self.i_SuccessCount += self.test_valid_creation()
        self.i_SuccessCount += self.test_valid_file_write()

    def test_valid_creation(self):
        o_TestObject    = Template("default")
        s_Expected      = "default"
        if o_TestObject.s_AppName == s_Expected:
            print("Success!")
            return 1
        else:
            print("Error!")
            return 0
    
    def test_valid_file_write(self):
        o_TestObject    = Template("default")
        s_Expected      = f"app_name=default"
        if (open('./config/appconfig.txt', 'r').readlines()[0] == s_Expected):
            print("Success!")
            return 1
        else:
            print("Error!")
            return 0 
   
def main():
    s_NameInput = input(f"Enter the name for your app (leave blank for '{Template.s_DefaultAppName}'):")
    o_Template = Template(s_NameInput)    
    o_Template.createDockerfile()
    o_Template.buildDockerImage()
    o_Template.runDockerImage()

if __name__=="__main__":
    print("\n")
    print("\t\t ~ Performing Pre-run checks ~")
    o_Tester = TemplateTester()
    print(f"\t\t Pre-run checks run with score: {o_Tester.i_SuccessCount}/{o_Tester.i_TestCount}")
    print("\n\t\t Starting User Interface\n\n")
    main()
    