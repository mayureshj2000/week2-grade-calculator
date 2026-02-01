# week2-grade-calculator
This Python script is a Student Grade Management System designed to handle academic data efficiently. It uses a menu-driven interface to collect student names and marks for multiple subjects, calculates averages, and assigns letter grades (A-F) with personalized feedback.

When I start, I define the colors using ANSI code. I’m not just printing text; I’m choosing a theme. When I see an 'A', I decide to shine in Green; for an 'F', I switch to Red. When I build results in table, I use precise alignment (:<20) to make sure every name and number sits perfectly in its column, like a professional spreadsheet.

**-> ** Validation
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
