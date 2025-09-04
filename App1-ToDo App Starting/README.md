# Old Version - 
## Milestone: replaced `match-case` with `if-else`
This code is now archived in separate branch -- main branch will use be improved further with functions.

## App #1 - ToDo list:
Starting with the basics (I know,again)! Yet another basics grid but this one's important, especially since it helps revise on some of the core data types & their methods in python:
  
    a. Lists operations
    
    b. File handling
    
    c. for, while loops ; try-except scenarios etc.

### Day 1-7: 
Started with simple list iterations using `while`, `for` & `if-else` loops.

Then, introducing File-handling with the  `with`, `open()`, `write()` funtions📄. Worked on Add& Show functionalities.

This will enable a more stable storage space since earlier tasks would last only for the current instance of the script.

Later on will move onto SQL or web-hosting, possibly a streamlit-to-SQL route 🛢️🔁🖥️.

### Day 8-15
Extended logic of file handling to edit & 'mark as done' operations.

**Adding new feature**: typing the ToDo task directly after typing the 'add' keyword.<br> 
_E.g. `>>Enter task: add Order book online`_
This will combine 2 steps -- one of typing the 'add' keyword step and that of adding the actual ToDo task. 

>📢**Altering conditional logic -- Switching to `if-else`** for implementing control flow of user input mentioned above.

Also, implemented use of the `continue` statement to skip certain code blocks based on logical flow & move to the start of the iteration i.e. to _`>>>Type add/ edit/ show/ done/ exit:`_

Using string methods such as `startswith()` to fix bugs for user actions that could contain confounding scenarios or user inputs.

The program will check if keywords are in the beginning of the input string;<br>
_For e.g. if user types text containing 'add' during edit sequence instead of entering a ToDo number._
_____

