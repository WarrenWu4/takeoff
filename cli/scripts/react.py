import subprocess
import os
import inquirer
import typer
from scripts.constants import Constants

class React:
    def __init__(self, name, path, pkgs, typescript):
        self.name = name
        self.path = path
        self.pkgs = pkgs.split(",")
        self.typescript = typescript 

    def takeoff(self):
        self.configure()
        # self.verify()
        # self.install()
        # self.setup()

    def configure(self):
        # if ts = None, prompt for js or ts
        if (self.typescript == None):
            question = inquirer.List("language", message="Choose a language:", choices=["Javascript", "Typescript"])
            answer = inquirer.prompt([question])
            if (answer["language"] == "Typescript"):
                self.typescript = True
            else:
                self.typescript = False
        # if name = None, prompt for name
        if (self.name == None):
            # TODO: validate name
            self.name = typer.prompt("Enter project name")
        # if path = None, prompt for path
        if (self.path == None):
            # TODO: validate path
            self.path = typer.prompt("Enter project path", default="./")
        # if pkgs = None, inquirer list of available packages
        if (self.pkgs == None):
            question = inquirer.Checkbox("pkgs", message="Which packages do you want to add? (Press <space> to select, Enter when finished)", choices=["tailwindcss", "react-router", "firebase"])
            answer = inquirer.prompt([question])
            self.pkgs = answer["pkgs"]
        print(self.typescript, self.name, self.path, self.pkgs)


    def verify(self):
        process = subprocess.run("node -v", capture_output=True, text=True,  shell=True)
        if len(process.stderr) != 0 and len(process.stdout) == 0:
            print("Node is not installed. Please install node before proceeding.")
            exit(1)
        process = subprocess.run("npm -v", capture_output=True, text=True,  shell=True)
        if len(process.stderr) != 0 and len(process.stdout) == 0:
            print("NPM is not installed. Please install NPM before proceeding.")
            exit(1)
        print("Prerequisites met. Proceeding...")

    def install(self):
        if os.path.exists(self.path):
            os.chdir(self.path)
        else:
            print("Path does not exist.\nExiting...")
            exit(1) 
        if "typescript" in self.options:
            subprocess.run(f"npm create vite@latest {self.name} -- --template react-ts", shell=True)
        else:
            subprocess.run(f"npm create vite@latest {self.name} -- --template react", shell=True)

    def setup(self):
        # install initial project
        self.install()
        # additional project packages & setup
        if "tailwindcss" in self.options:
            os.chdir(self.name)
            subprocess.run("npm install tailwindcss postcss autoprefixer", shell=True)
            subprocess.run("npx tailwindcss init -p", shell=True)
            with open(self.path+"/"+self.name+"/tailwind.config.js") as f:
                f.write(Constants.TAILWIND_CONFIG)
            with open(self.path+"/"+self.name+"/src/index.css") as f:
                f.write(Constants.TAILWIND_INDEXCSS)

    def add_pkgs(self):
        pass
