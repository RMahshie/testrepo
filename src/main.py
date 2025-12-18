"""Main entry point for the calculator application."""

import sys
from calculator import Calculator, add, subtract, multiply, divide
from calculator.utils import format_result, validate_number, parse_input


def print_menu():
    """Print the main menu."""
    print("\n" + "=" * 40)
    print("Simple Calculator")
    print("=" * 40)
    print("1. Basic operations (direct)")
    print("2. Calculator with history")
    print("3. Interactive mode")
    print("4. Exit")
    print("=" * 40)


def basic_operations():
    """Perform basic operations without state."""
    print("\n--- Basic Operations ---")
    print("Available operations: +, -, *, /")
    print("Enter expression (e.g., '5 + 3') or 'back' to return")
    
    while True:
        user_input = input("\nExpression: ").strip()
        
        if user_input.lower() == 'back':
            break
        
        parsed = parse_input(user_input)
        if not parsed:
            print("Invalid input. Please use format: number operator number")
            continue
        
        operand1, operator, operand2 = parsed
        
        try:
            if operator == '+':
                result = add(operand1, operand2)
            elif operator == '-':
                result = subtract(operand1, operand2)
            elif operator == '*':
                result = multiply(operand1, operand2)
            elif operator == '/':
                result = divide(operand1, operand2)
            else:
                print(f"Unknown operator: {operator}")
                continue
            
            print(f"Result: {format_result(result)}")
        except ValueError as e:
            print(f"Error: {e}")


def calculator_with_history():
    """Use Calculator class with history tracking."""
    calc = Calculator()
    print("\n--- Calculator with History ---")
    print("Commands: add, subtract, multiply, divide, result, history, clear, back")
    
    while True:
        command = input("\nCommand: ").strip().lower()
        
        if command == 'back':
            break
        elif command == 'result':
            print(f"Current result: {format_result(calc.get_result())}")
        elif command == 'history':
            history = calc.get_history()
            if history:
                print("\nCalculation History:")
                for entry in history:
                    print(f"  - {entry}")
            else:
                print("No history yet")
        elif command == 'clear':
            calc.clear()
            print("Calculator cleared")
        elif command in ['add', 'subtract', 'multiply', 'divide']:
            value_input = input(f"Enter value to {command}: ").strip()
            if not validate_number(value_input):
                print("Invalid number")
                continue
            
            value = float(value_input)
            try:
                if command == 'add':
                    result = calc.add(value)
                elif command == 'subtract':
                    result = calc.subtract(value)
                elif command == 'multiply':
                    result = calc.multiply(value)
                elif command == 'divide':
                    result = calc.divide(value)
                
                print(f"Result: {format_result(result)}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Unknown command")


def interactive_mode():
    """Simple interactive calculator mode."""
    print("\n--- Interactive Mode ---")
    print("Enter calculations like '5 + 3' or 'quit' to exit")
    
    while True:
        user_input = input("\n> ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'back']:
            break
        
        parsed = parse_input(user_input)
        if not parsed:
            print("Invalid input. Please use format: number operator number")
            continue
        
        operand1, operator, operand2 = parsed
        
        try:
            if operator == '+':
                result = add(operand1, operand2)
            elif operator == '-':
                result = subtract(operand1, operand2)
            elif operator == '*':
                result = multiply(operand1, operand2)
            elif operator == '/':
                result = divide(operand1, operand2)
            else:
                print(f"Unknown operator: {operator}")
                continue
            
            print(f"= {format_result(result)}")
        except ValueError as e:
            print(f"Error: {e}")


def main():
    """Main application entry point."""
    print("Welcome to Simple Calculator!")
    
    while True:
        print_menu()
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == '1':
            basic_operations()
        elif choice == '2':
            calculator_with_history()
        elif choice == '3':
            interactive_mode()
        elif choice == '4':
            print("\nThank you for using Simple Calculator!")
            sys.exit(0)
        else:
            print("Invalid option. Please select 1-4.")


if __name__ == "__main__":
    main()
