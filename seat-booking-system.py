class SeatBookingSystem:
    def __init__(self):
        """
        Initializes the seat booking system.
        Creates a dictionary to represent the seating layout of an aircraft, where seats are initialized as 'F' (free),
        and certain seats are designated as 'S' (storage) based on their position.
        """
        self.seats = {}
        seat_labels = ["A", "B", "C", "D", "E", "F"]
        for row in range(1, 7):
            for col in range(1, 81):
                # if row == 4:
                #     self.seats[f"{col}X"] = "X"  # Aisle seats
                if col >= 77 and col <= 78 and (row == 5 or row == 6):
                    self.seats[f"{col}{seat_labels[row-1]}"] = "S"  # Storage areas
                else:
                    self.seats[f"{col}{seat_labels[row-1]}"] = "F"  # Free seats

    def check_availability(self, seat_id):
        """
        Checks the availability of a specified seat.
        :param seat_id: A string representing the seat (e.g., "1A").
        :return: True if the seat is free ('F'), False otherwise.
        """
        return self.seats.get(seat_id) == "F"

    def book_seat(self, seat_id):
        """
        Attempts to book a seat if it is available.
        :param seat_id: A string representing the seat to be booked (e.g., "1A").
        :return: True if the booking was successful, False if the seat was already booked or unavailable.
        """
        if self.check_availability(seat_id):
            self.seats[seat_id] = "R"
            return True
        return False

    def free_seat(self, seat_id):
        """
        Frees a booked seat, making it available for future bookings.
        :param seat_id: A string representing the seat to be freed (e.g., "1A").
        :return: True if the seat was successfully freed, False if the seat was not previously booked.
        """
        if self.seats.get(seat_id) == "R":
            self.seats[seat_id] = "F"
            return True
        return False

    def show_booking_state(self):
        """
        Displays the current state of all seats within the aircraft layout.
        Rows are printed with seats labeled by their current status (Free, Reserved, or Storage).
        """
        for i in range(1, 81):
            row_output = []
            for label in ["A", "B", "C", "X", "D", "E", "F"]:
                if label == "X":
                    row_output.append("X")
                    continue
                seat_id = f"{i}{label}"
                if seat_id in self.seats:
                    # Combine the seat ID and its state for output
                    row_output.append(f"{seat_id}({self.seats[seat_id]})")
            print(" ".join(row_output))  # Print the whole row as a single line


def main():
    """
    Main function to run the seat booking system interface.
    Users can check seat availability, book seats, free seats, and view the current booking state.
    """
    system = SeatBookingSystem()
    while True:
        print("\nMenu:")
        print("1. Check availability of seat")
        print("2. Book a seat")
        print("3. Free a seat")
        print("4. Show booking state")
        print("5. Exit program")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            seat_id = input("Enter seat ID (e.g., 1A): ")
            print("Available" if system.check_availability(seat_id) else "Not available")
        elif choice == 2:
            seat_id = input("Enter seat ID to book (e.g., 1A): ")
            print("Booking successful" if system.book_seat(seat_id) else "Booking failed")
        elif choice == 3:
            seat_id = input("Enter seat ID to free (e.g., 1A): ")
            print("Freeing successful" if system.free_seat(seat_id) else "Freeing failed")
        elif choice == 4:
            system.show_booking_state()
        elif choice == 5:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
