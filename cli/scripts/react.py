import subprocess
import os

class React:
    name = ""
    path = ""
    options = []

    def __init__(self, name, path, options):
        self.name = name
        self.path = path
        self.options = options

    def checkPrereqs(self):
        process = subprocess.Popen("node -v", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        if len(error) != 0 and len(output) == 0:
            print("Node is not installed. Please install node before proceeding.")
            exit(1)
        process = subprocess.Popen("npm -v", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        if len(error) != 0 and len(output) == 0:
            print("NPM is not installed. Please install NPM before proceeding.")
            exit(1)
        print("Prerequisites met. Proceeding...")

    def setupProj(self):
        # TODO: fix pathing issues
        # check if folder with name & path exists
        if os.path.exists(self.path+"/"+self.name):
            # if exists cd into it
            os.chdir(self.path+"/"+self.name)
        # if doesn't exist mkdir and cd into it
        else:
            os.mkdir(self.path+"/"+self.name)
            os.chdir(self.path+"/"+self.name)
        # based on parameters, create desired react app
        if "typescript" in self.options:
            subprocess.run("npm create vite@latest react-app -- --template react-ts", shell=True)
        else:
            subprocess.run("npm create vite@latest react-app -- --template react", shell=True)
        
        # install other options
        if "tailwindcss" in self.options:
            subprocess.run("npm install tailwindcss", shell=True)
        if "firebase" in self.options:
            subprocess.run("npm install firebase", shell=True)
        if "react-router" in self.options:
            subprocess.run("npm install react-router-dom", shell=True)