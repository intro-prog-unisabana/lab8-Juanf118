import sys

def calculate_load_per_support():
    try:
        total_load_str = sys.argv[1] 
        num_supports_str = sys.argv[2]

        total_load = float(total_load_str)
        num_supports = float(num_supports_str)
  
        if num_supports == 0:
            print("Error: Cannot divide by zero! Supports must be greater than zero.")
            return 
        
        load_per_support = total_load / num_supports
        print(f"Load per support point: {load_per_support:.2f} N")

    except (ValueError, IndexError):
        print("Error: Invalid input! Enter numeric values only.")

if __name__ == "__main__":
        calculate_load_per_support()