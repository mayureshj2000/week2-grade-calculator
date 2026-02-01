# week2-grade-calculator
This Python script is a Student Grade Management System designed to handle academic data efficiently. It uses a menu-driven interface to collect student names and marks for multiple subjects, calculates averages, and assigns letter grades (A-F) with personalized feedback.

When I start, I define the colors using ANSI code. I’m not just printing text; I’m choosing a theme. When I see an 'A', I decide to shine in Green; for an 'F', I switch to Red. When I build results in table, I use precise alignment (:<20) to make sure every name and number sits perfectly in its column, like a professional spreadsheet.

**->** Validation
When asked to get a number, The gatekeeper activates. The try-except blocks are used to catch mistakes. If you accidentally type a letter where a mark should be, compiler don't crash—I just block the entry and ask you again. It won't let "bad data" break the math working behind the scenes.

**->** Dictionary
I keep all students data in a List of Dictionaries.

Every student is a "folder" (a dictionary) containing their name and scores.

I store these folders (the students list). This allows to Search (Option 3) instantly. I just run through my list, peek at each folder, and show you the one that matches the name you gave me.

**->** Saving
When we hit Option 4, I talk to your computer's hard drive. I’m flexible—I’ll use whatever filename you want. If you forget to add .txt, I do it for you. I use a "safety first" writing method (with open) to ensure that your data is locked in and the file is closed properly, even if something goes wrong.

**->** How to Execute Me
Save: Put the code in a file named calculator.py.

Start: In your terminal, type python calculator.py.

Feed: Press 1 to give me student data first.

View & Save: Press 2 to see my color-coded table, or 4 to save that data to your computer.

**Output**
Welcome to the Student Grade Management System!

----- GRADE MANAGER MENU -----
1. Add Student Data
2. Display All Results
3. Search for Student
4. Save Results to File
5. Exit
Select an option (1-5):
1
How many students to add?
3
Enter name for student 1:
Sonal
Math Mark (0-100):
98
Science Mark (0-100):
97
English Mark (0-100):
95
Student added successfully!
Enter name for student 2:
Mayuresh
Math Mark (0-100):
95
Science Mark (0-100):
87
English Mark (0-100):
85
Student added successfully!
Enter name for student 3:
Pooja
Math Mark (0-100):
90
Science Mark (0-100):
85
English Mark (0-100):
80
Student added successfully!

----- GRADE MANAGER MENU -----
1. Add Student Data
2. Display All Results
3. Search for Student
4. Save Results to File
5. Exit
Select an option (1-5):
2

================================================================================
Student              | Average    | Grade      | Comment
--------------------------------------------------------------------------------
Sonal                | 96.7       |     A      | Great Work!!!
Mayuresh             | 89.0       |     B      | Good Work!!!
Pooja                | 85.0       |     B      | Good Work!!!
--------------------------------------------------------------------------------
CLASS STATS | Avg: 90.2 | Max: 96.7 | Min: 85.0
================================================================================

----- GRADE MANAGER MENU -----
1. Add Student Data
2. Display All Results
3. Search for Student
4. Save Results to File
5. Exit
Select an option (1-5):
3
Enter student name to search:
Sonal

================================================================================
Student              | Average    | Grade      | Comment
--------------------------------------------------------------------------------
Sonal                | 96.7       |     A      | Great Work!!!
--------------------------------------------------------------------------------
CLASS STATS | Avg: 96.7 | Max: 96.7 | Min: 96.7
================================================================================

----- GRADE MANAGER MENU -----
1. Add Student Data
2. Display All Results
3. Search for Student
4. Save Results to File
5. Exit
Select an option (1-5):
4
Enter the filename to save as (e.g., results):
test_students

[System Message]: Student data saved to 'test_students.txt' 

----- GRADE MANAGER MENU -----
1. Add Student Data
2. Display All Results
3. Search for Student
4. Save Results to File
5. Exit
Select an option (1-5):
5
Goodbye!!!
