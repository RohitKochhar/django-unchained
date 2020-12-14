import subprocess

class Creator():
    s_DefaultModuleName    = "module"

    def __init__(self):
        print(f"Setting app configuration...")
        self.setConfig()

    def createDjangoProject(self):
        s_BashCommand   = f"django-admin startproject {self.s_AppName}"
        a_BashCommand   = s_BashCommand.split()

        process = subprocess.Popen(a_BashCommand, stdout=subprocess.PIPE)
        output, error = process.communicate()

    def createDjangoModule(self):
        s_BashCommand   = f"python {self.s_AppName}/manage.py startapp {self.s_DefaultModuleName}"
        a_BashCommand   = s_BashCommand.split()

        process = subprocess.Popen(a_BashCommand, stdout=subprocess.PIPE)
        output, error = process.communicate()

    def setConfig(self):
        self.a_Config       = open('./config/appconfig.txt', 'r').readlines()
        # Get the app name
        self.s_AppName      = self.a_Config[0].split("=")[1]
        
class CreatorTester():
    i_SuccessCount  = 0
    i_TestCount     = 2

    def __init__(self):
        self.i_SuccessCount += self.test_valid_config_set()
        self.i_SuccessCount += self.test_valid_django_project_creation()

    def test_valid_config_set(self):
        o_TestObject    = Creator()
        a_Expected      = open('./config/appconfig.txt', 'r').readlines()
        if o_TestObject.a_Config == a_Expected:
            print("Success!")
            return 1
        else:
            print(f"Error: Got {o_TestObject.a_Requirements}, expected {a_Expected}")
            return 0

    def test_valid_django_project_creation(self):
        o_Test      = Creator()
        o_Test.createDjangoProject()
        # Try to open manage.py
        try:
            f_Manage    = open(f'/django-app/{o_Test.s_AppName}/manage.py', 'r')
            print(f"Success! /django-app/{o_Test.s_AppName}/manage.py exists")
            return 1
        except Exception as e:
            print(e)
            print(f"Error! Could not find /django-app/{o_Test.s_AppName}/manage.py not found")
            return 0
            

def main():
    o_Creator   = Creator()
    print(f"Creating Django configuration")
    o_Creator.createDjangoProject()
    o_Creator.createDjangoModule()

if __name__=="__main__":    
    TEST = 0
    if TEST == 1:
        print("\n")
        print("\t\t ~ Performing Pre-run checks ~")
        o_Tester = CreatorTester()
        print(f"\t\t Pre-run checks run with score: {o_Tester.i_SuccessCount}/{o_Tester.i_TestCount}")
    else:
        print("\n\t\t Starting User Interface\n\n")
        main()