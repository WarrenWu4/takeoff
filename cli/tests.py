from scripts.react import React

def test_react_prereqs():
    react_proj = React("test", "./testing", ["typescript"])
    react_proj.checkPrereqs()
    
test_react_prereqs()