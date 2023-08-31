questions=[ ["1.Which of the following is an example of an operating system?", "Python", "Java", "Windows", "HTML", 3],
            ["2.Which programming language is known for its 'write once, run anywhere' feature?", "Python", "Java", "C++", "PHP", 2],
            ["3.What does 'SQL' stand for in the context of databases?", "Structured Question Language", "Simple Query Language", "Structured Query Language", "System Query Language", 3],
            ["4.Which data structure is used to implement a queue?", "Stack", "Array", "List", "Queue", 2],
            ["5.Which component of an operating system manages memory?", "Kernel", "Compiler", "Monitor", "Debugger", 1],
            ["6.What is the primary function of the 'scheduler' in an operating system?", "Memory management", "File management", "Process scheduling", "Disk management", 3],
            ["7.What is the term for converting an object into a stream of bytes?", "Serialization", "Deserialization", "Inheritance", "Polymorphism", 1],
            ["8.Which keyword in Java is used to create a new object?", "new", "object", "create", "class", 1],
            ["9.What does 'DBMS' stand for?", "Data Business Management System", "Database Management System", "Data and Business Management System", "Database and Business Management System", 2],
            ["10.In a relational database, what is a 'primary key'?", "A key used to open the database", "A key used to encrypt data", "A unique identifier for a record", "A key used for sorting records", 3],
            ["11.What is the time complexity of a binary search algorithm?", "O(1)", "O(log n)", "O(n)", "O(n log n)", 2],
            ["12.Which data structure uses the 'Last-In-First-Out' (LIFO) principle?", "Queue", "Array", "Linked List", "Stack", 4],
            ["13.Which part of the operating system handles communication between hardware and software?", "Kernel", "Shell", "GUI", "Driver", 1],
            ["14.What is the purpose of the 'final' keyword in Java?", "To declare a method as non-overridable", "To indicate a variable can only be assigned once", "To define the main method in a class", "To create a constant variable", 2],
            ["15.What is an 'ERD' in the context of a database?", "Event and Resource Diagram", "Entity and Relationship Diagram", "Entity and Resource Data", "Event and Relationship Data", 2],
            ["16.What is the worst-case time complexity of the bubble sort algorithm?", "O(1)", "O(log n)", "O(n)", "O(n^2)", 4],
            ["17.What is the time complexity of a linear search algorithm?", "O(1)", "O(log n)", "O(n)", "O(n^2)", 3]
    # Add more questions here
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,640000,1250000,2500000,5000000,7500000,10000000,75000000]
money = 0


for i in range(0,len(questions)):
  question=questions[i]
  print(f"\nquestion for rs. {levels[i]}")
  print(f"\nquestion {question[0]}")
  print(f"\n 1.{question[1]}             2.{question[2]}")
  print(f"\n 3.{question[3]}             4.{question[4]}")

  ans=int(input("enter the option for currect answer between (1-4) "))

  if ans==0:
    money=level[i-1]
    break

  elif ans==question[-1]:
    print(f"currot answer! you have won rs. {levels[i]}")

    if i==4:
      money=10000
    elif i==9:
      money=320000
    elif i==14:
      money=7500000
    elif i==14:
      money=75000000

  else:
    print("wrong answer")
    break
print(F"your take home money is rs. {money}")

 
