# Debugging a Poetry package script with VSCode

It is not so straight forward to debug a Python script that is part of a Poetry package with VSCode.
One way to do it is to add a launch.json file to the .vscode folder of the project.
This is also discussed in [this discussion](https://stackoverflow.com/questions/69106483/python-project-with-poetry-how-to-debug-it-in-visual-studio-code)
For me this approach is too cumbersome because I do not fully understand how the debug mechanism works in VSCode.
My solution is to add a .vscodedebug folder with a debug.py file that adds the src directory to the sys.path and performs the import of the script that I want to debug.
This can be used as an entry point for the debugger.