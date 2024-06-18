import typer
from scripts.react import React
from pathlib import Path
from typing import List

app = typer.Typer()

@app.command()
def welcome():
    print(f"Welcome to takeoff!")

@app.command()
def react(name:str = typer.Option(default=None), path:Path = typer.Option(default=None), pkgs:str = typer.Option(default=None), typescript:bool = typer.Option(default=None)):
    React(name, path, pkgs, typescript).takeoff()

if __name__ == "__main__":
    app()
