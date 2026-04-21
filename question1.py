"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""
import sys

total_load = input("Ingrese la carga total en Newtons (N): ")
num_supports = input("Ingrese el número de puntos de soporte: ")
try:
        total_load = float(total_load)
        num_supports = int(num_supports)
        load_per_support = float(total_load) / int(num_supports)
except ValueError:
        print("Error: Invalid input! Enter numeric values only.")
        sys.exit(1)
except ZeroDivisionError:
        print("Error: Cannot divide by zero! Support must be greater than zero.")
        sys.exit(1)

print(f"Load per support point: {load_per_support:.2f} N")



# TODO: Implementar según README.md
