# Mayuresh Jadhav - Student Grade Calculator
# Control Flow, Data Structures, File Handling, Color Coding and Error Handling
import sys

# Color Constants
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BLUE = '\033[94m'
CYAN = '\033[96m'
RESET = '\033[0m'

def get_color(grade):
    """Helper to return color based on grade."""
    if grade == 'A': return GREEN
    if grade == 'B': return CYAN
    if grade == 'C': return YELLOW
    if grade in ['D', 'F']: return RED
    return RESET

def calculate_grade(avg):
    try:
        if avg >= 90: return 'A', 'Great Work!!!'
        elif avg >= 80: return 'B', 'Good Work!!!'
        elif avg >= 70: return 'C', 'Improvement Required.'
        elif avg >= 60: return 'D', 'Study More.'
        else: return 'F', 'Failed'
    except Exception as e:
        return 'N/A', f'Error: {e}'

def get_valid_number(msg, min_val, max_val, integer=False):
    while True:
        try:
            val = input(msg)
            num = int(val) if integer else float(val)
            if min_val <= num <= max_val:
                return num
            print(f'{RED}Value must be between {min_val} and {max_val}.{RESET}')
        except ValueError:
            print(f'{RED}Invalid input. Please enter a valid number.{RESET}')

def save_to_file(students):
    if not students:
        print(f"{YELLOW}Nothing to save. Please add student data first.{RESET}")
        return
    filename = input("\nEnter the filename to save as (e.g., results): ").strip()
    
    if not filename:
        filename = "students_report"
    
    if not filename.endswith(".txt"):
        filename += ".txt"
    try:
        with open(filename, 'w') as f:
            f.write("Student Report\n" + "="*40 + "\n")
            for s in students:
                f.write(f"{s['name']} | AVG: {s['average']:.2f} | Grade: {s['grade']}\n")
        print(f"\n{GREEN}[System Message]: Student data saved to '{filename}' {RESET}")
    except PermissionError:
        print(f"{RED}Error: File is open in another program or permission denied.{RESET}")
    except Exception as e:
        print(f"{RED}Error saving file: {e}{RESET}")

def display_result(students):
    try:
        if not students:
            print(f"{YELLOW}No students found.{RESET}")
            return
        
        print("\n" + "=" * 80)
        print(f"{BLUE}{'Student':<20} | {'Average':<10} | {'Grade':<10} | {'Comment'}{RESET}")
        print("-" * 80)
        
        for s in students:
            color = get_color(s['grade'])
            print(f"{s['name']:<20} | {s['average']:<10.1f} | {color}{s['grade']:^10}{RESET} | {s['comment']}")
        
        avgs = [s['average'] for s in students]
        print("-" * 80)
        print(f"{BLUE}CLASS STATS | Avg: {sum(avgs)/len(avgs):.1f} | Max: {max(avgs):.1f} | Min: {min(avgs):.1f}{RESET}")
        print("=" * 80)
    except Exception as e:
        print(f"{RED}Failed to display results: {e}{RESET}")

def main():
    students = []
    print(f"{BLUE}Welcome to the Student Grade Management System!{RESET}")
    
    while True:
        try:
            print(f"\n{CYAN}----- GRADE MANAGER MENU -----{RESET}")
            print("1. Add Student Data")
            print("2. Display All Results")
            print("3. Search for Student")
            print("4. Save Results to File")
            print("5. Exit")

            choice = input("Select an option (1-5): ").strip()

            if choice == '1':
                num = get_valid_number("How many students to add? ", 1, 50, True)
                for i in range(num):
                    while True:
                        name = input(f"Enter name for student {i+1}: ").strip()
                        if name: break
                        print(f"{RED}Name cannot be empty!{RESET}")
                    
                    m = get_valid_number("  Math Mark (0-100): ", 0, 100)
                    s = get_valid_number("  Science Mark (0-100): ", 0, 100)
                    e = get_valid_number("  English Mark (0-100): ", 0, 100)
                    
                    avg = (m + s + e) / 3
                    grade, comment = calculate_grade(avg)
                    students.append({'name': name, 'average': avg, 'grade': grade, 'comment': comment})
                    print(f"{GREEN}Student added successfully!{RESET}")

            elif choice == '2':
                display_result(students)

            elif choice == '3':
                query = input("Enter student name to search: ").lower().strip()
                found = [s for s in students if query in s['name'].lower()]
                display_result(found) if found else print(f"{YELLOW}No matches found.{RESET}")
            
            elif choice == '4':
                save_to_file(students)

            elif choice == '5':
                print(f"{BLUE}Goodbye!!!{RESET}")
                break
            else:
                print(f"{RED}Invalid choice. Please select 1-5.{RESET}")
                
        except KeyboardInterrupt:
            print(f"\n{RED}Program interrupted. Exiting...{RESET}")
            break
        except Exception as e:
            print(f"{RED}An unexpected error occurred: {e}{RESET}")

if __name__ == "__main__":
    main()
