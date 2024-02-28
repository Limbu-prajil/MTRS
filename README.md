Movie Theatre Reservation System Documentation

Overview
The Movie Theatre Reservation System is an application for managing reservations in a movie theatre. It allows customers to reserve seats for movies at different times and enables administrators
to add movies, schedule screenings, and browse reservations.

Features
1. Customer Interface: Customers can view available movies, select a movie, choose a screening time, and make reservations.
2. Admin Interface: Administrators can add new movies, schedule screenings, and browse existing reservations.
3. Data Persistence: All data, including movies, screenings, and reservations, are saved to a file (movie_theatre_data.json) for persistent storage.
4. Data Structures: The project uses lists and dictionaries to organize and manage data efficiently.

Functionality
1. Display Movies: Customers and administrators can view a list of available movies.
2. Display Screenings: Customers can see available screenings for a selected movie.
3. Make Reservation(reserve seat): Customers can reserve seats for a selected movie and screening time.
4. Add Movie: Administrators can add new movies to the system.
5. Add Screening: Administrators can schedule screenings for movies in different halls at specific times.
6. Browse Reservations: Administrators can view all current reservations made by customers.

Usage
1. Customer Interface:
  Select "Customer Interface" from the main menu.
  Choose a movie from the list of available movies.
  Select a screening time for the chosen movie.
  Enter your name to make a reservation.

2. Admin Interface:
  Select "Admin Interface" from the main menu.
  Choose from options to add a new movie, schedule a screening, or browse reservations.
  Follow the prompts to perform the selected action.

3. Exiting the System:
  Select "Exit" from the main menu to exit the application.

Files
1. movie_theatre.py: The main Python script containing the Movie Theatre Reservation System implementation.
2. movie_theatre_data.json: JSON file storing all data related to movies, halls, and reservations.

Requirements
1. Python 3.x
2. Visual Studio Code (or any other text editor)
3. Terminal (or command prompt)

Running the Project
1. Open the terminal and navigate to the directory containing movie_theatre.py.
2. Run the command python movie_theatre.py to start the application.
3. Follow the on-screen prompts to interact with the system.

Notes
1. Ensure that movie_theatre_data.json is present in the same directory as movie_theatre.py for data persistence.
2. The application provides separate interfaces for customers and administrators to perform their respective tasks.
3. Import the json module if it is relevant for the implementation of the reservation system.
