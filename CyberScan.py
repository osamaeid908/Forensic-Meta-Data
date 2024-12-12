# Optimized Python Code Structure

# Import required libraries
import math
import os
import sys

# Utility Functions
def calculate_area(radius):
    """Calculate the area of a circle given its radius."""
    if radius <= 0:
        raise ValueError("Radius must be greater than 0")
    return math.pi * radius ** 2

def read_file(filepath):
    """Read the contents of a file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    with open(filepath, 'r') as file:
        return file.read()

def write_file(filepath, content):
    """Write content to a file."""
    with open(filepath, 'w') as file:
        file.write(content)

# Main Application Logic
def main():
    """Main application entry point."""
    try:
        print("Welcome to the Circle Area Calculator!")
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_area(radius)
        print(f"The area of the circle is: {area:.2f}")

        save_option = input("Do you want to save the result to a file? (yes/no): ").strip().lower()
        if save_option == 'yes':
            filepath = input("Enter the file path to save the result: ").strip()
            write_file(filepath, f"Radius: {radius}\nArea: {area:.2f}")
            print(f"Result saved to {filepath}")
        else:
            print("Result not saved.")

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except FileNotFoundError as fe:
        print(f"File Error: {fe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry Point
if __name__ == "__main__":
    main()
