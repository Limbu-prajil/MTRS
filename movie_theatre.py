import json

# Global variables
movies = []
halls = {}
reservations = {}

# Function to save data to a file
def save_data():
    data = {'movies': movies, 'halls': halls, 'reservations': reservations}
    with open('movie_theatre_data.json', 'w') as file:
        json.dump(data, file)

# Function to load data from a file
def load_data():
    try:
        with open('movie_theatre_data.json', 'r') as file:
            data = json.load(file)
            global movies, halls, reservations
            movies = data.get('movies', [])
            halls = data.get('halls', {})
            reservations = data.get('reservations', {})
    except FileNotFoundError:
        # File doesn't exist yet, initialize with empty data
        save_data()

# Function to display available movies
def display_movies():
    print("\nAvailable Movies:")
    for movie in movies:
        print(f"{movie['id']}. {movie['title']}")

# Function to display available screenings for a movie
def display_screenings(movie_id):
    print("\nAvailable Screenings:")
    if movie_id in halls:
        for time, hall_id in halls.get(movie_id, {}).items():
            print(f"{time} in Hall {hall_id}")
    else:
        print("No screenings available for this movie.")
        print("Halls:", halls)

# Function for customers to reserve a seat
def reserve_seat(customer_name, movie_id, time):
    hall_id = halls.get(movie_id, {}).get(time)
    if hall_id is not None:
        if reservations.get(hall_id) is None:
            reservations[hall_id] = {}
        if reservations[hall_id].get(time) is None:
            reservations[hall_id][time] = []
        reservations[hall_id][time].append(customer_name)
        save_data()
        print(f"\nReservation successful! {customer_name}, enjoy the movie at Hall {hall_id} on {time}.")
    else:
        print("\nInvalid movie ID or time.")

# Function for administrators to add a new movie
def add_movie(title):
    movie_id = len(movies) + 1
    movies.append({'id': movie_id, 'title': title})
    save_data()
    print(f"\nMovie '{title}' added with ID {movie_id}.")

# Function for administrators to add a new screening
def add_screening(movie_id, time, hall_id):
    if movie_id <= len(movies):
        if halls.get(movie_id) is None:
            halls[movie_id] = {}
        halls[movie_id][time] = hall_id
        save_data()
        print(f"\nScreening for Movie {movie_id} at {time} in Hall {hall_id} added.")
    else:
        print("\nInvalid movie ID.")

# Function for administrators to browse reservations
def browse_reservations():
    print("\nCurrent Reservations:")
    for hall_id, screenings in reservations.items():
        for time, customers in screenings.items():
            print(f"Hall {hall_id}, {time}: {', '.join(customers)}")

# Text-based user interface for customers
def customer_interface():
    load_data()
    display_movies()
    movie_id = input("\nEnter the ID of the movie you want to watch: ")
    display_screenings(movie_id)
    time = input("\nEnter the time you want to watch the movie: ")
    customer_name = input("\nEnter your name: ")
    reserve_seat(customer_name, movie_id, time)

# Text-based user interface for administrators
def admin_interface():
    load_data()
    while True:
        print("\nAdmin Menu:")
        print("1. Add Movie")
        print("2. Add Screening")
        print("3. Browse Reservations")
        print("4. Exit")
        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            title = input("\nEnter the title of the new movie: ")
            add_movie(title)
        elif choice == '2':
            movie_id = int(input("\nEnter the ID of the movie: "))
            time = input("\nEnter the time of the screening: ")
            hall_id = int(input("\nEnter the ID of the hall: "))
            add_screening(movie_id, time, hall_id)
        elif choice == '3':
            browse_reservations()
        elif choice == '4':
            save_data()
            print("\nExiting Admin Interface.")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    print("Welcome to the Movie Theatre Reservation System!")
    while True:
        print("\nMain Menu:")
        print("1. Customer Interface")
        print("2. Admin Interface")
        print("3. Exit")
        main_choice = input("\nEnter your choice (1-3): ")

        if main_choice == '1':
            customer_interface()
        elif main_choice == '2':
            admin_interface()
        elif main_choice == '3':
            print("\nExiting Movie Theatre Reservation System.")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 3.")
