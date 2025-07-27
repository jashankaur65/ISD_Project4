# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author

Jashan Kaur

## Assignment

Assignment 1: Bank Account and Client Management

Assignment 2: Abstraction, Inheritance and Polymorphism

Assignment 3: The Strategy Pattern is used to encapsulate the logic for calculating service charges into different strategy classes (Overdraft, Management Fee, and Minimum Balance). This allows for flexibility in applying different rules without modifying the core account classes.

Assignment 4: Programming Paradigms

## Encapsulation

Encapsulation in the BankAccount and Transaction classes is achieved by using private attributes and providing public methods like deposit() and withdraw() to interact with them. This ensures data is validated and protected from direct modification.

## Event-Driven Programming Paradigm

This application is structured using the Event-Driven Programming Paradigm to enhance user interaction. The following core components reflect this design:

- **Signal and Slot Mechanism**: The PySide6 library's signal and slot mechanism connects user actions to methods.
- **Dynamic Data Updates**: The application responds to user actions such as selecting a client or performing transactions, updating UI elements accordingly.
