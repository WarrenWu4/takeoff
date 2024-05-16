import typer
from scripts.react import React

app = typer.Typer()


@app.command()
def main():
    print(f"Welcome to takeoff!")
    print(f"Usage: python main.py [project] [--flag1] [--flag2]")

@app.command()
def react(
        typescript: bool = False, 
        tailwindcss:bool = False, 
        firebase:bool = False,
        react_router:bool = False
    ):
    options = []
    if (typescript): options.append("typescript")
    if (tailwindcss): options.append("tailwindcss")
    if (firebase): options.append("firebase")
    if (react_router): options.append("react-router")
    name = input("Enter project name: ")
    path = input("Enter project path: ")
    react_project = React(name, path, options)
    react_project.checkPrereqs()
    react_project.setupProj()

if __name__ == "__main__":
    app()
