"""Laboratorio 8 - CLI del gestor de tareas."""
import sys 
from todo_manager import read_todo_file, write_todo_file

try:
    if len(sys.argv) < 2:
        raise IndexError("Insufficient arguments provided!")
    arguments = sys.argv[1:]
    file = arguments[0]

    tasks = read_todo_file(file)

    print("Command-line arguments:")
    for arg in arguments:
        print(arg)
    print("\nTasks:")
    for task in tasks:
        print(task)
except IndexError as e:
    print(e)

    



