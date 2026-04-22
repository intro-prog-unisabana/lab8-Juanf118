"""Laboratorio 8 - CLI del gestor de tareas."""
import sys 
from todo_manager import read_todo_file, write_todo_file

def main():
            try:
                if len(sys.argv) < 2:
                 raise IndexError("Insufficient arguments provided!")


