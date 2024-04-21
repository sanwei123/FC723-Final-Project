import random
import string

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
                if col >= 77 and col <= 78 and (row == 5 or row == 6):
                    self.seats[f"{col}{seat_labels[row-1]}"] = "S"  # Storage areas
                else:
                    self.seats[f"{col}{seat_labels[row-1]}"] = "F"  # Free seats
        self.booking_references = set()  # Set to track unique booking references
        self.booking_details = {}  # Dictionary to store booking details

    def generate_unique_reference(self):
        """
        Generate a unique booking reference with exactly eight alphanumeric characters.
        """
        while True:
            reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            if reference not in self.booking_references:
                self.booking_references.add(reference)
                return reference

    def check_availability(self, seat_id):
        """
        Checks the availability of a specified seat.
        :param seat_id: A string representing the seat (e.g., "1A").
        :return: True if the seat is free ('F'), False otherwise.
        """
        return self.seats.get(seat_id, 'X') == "F"  # Returns False for 'S', 'X', and any reference

    def book_seat(self, seat_id, passport_number, first_name, last_name):
        """
        Attempts to book a seat if it is available.
        :param seat_id: A string representing the seat to be booked (e.g., "1A").
        :return: True if the booking was successful, False if the seat was already booked or unavailable.
        """
        if self.check_availability(seat_id):
            reference = self.generate_unique_reference()
            self.seats[seat_id] = reference
            self.booking_details[reference] = {
                "passport_number": passport_number,
                "first_name": first_name,
                "last_name": last_name,
                "seat_id": seat_id
            }
            return f"Booking successful with reference {reference}"
        return "Booking failed"

    def free_seat(self, seat_id):
        """
        Frees a booked seat, making it available for future bookings.
        :param seat_id: A string representing the seat to be freed (e.g., "1A").
        :return: True if the seat was successfully freed, False if the seat was not previously booked.
        """
        if seat_id in self.seats and self.seats[seat_id] not in ["F", "S", "X"]:
            reference = self.seats[seat_id]
            del self.booking_details[reference]
            self.seats[seat_id] = "F"
            return "Freeing successful"
        return "Freeing failed"

    def show_booking_state(self):
        """
        Displays the current state of all seats within the aircraft layout.
        Rows are printed with seats labeled by their current status (Free, Reserved, or Storage).
        """
        for i in range(1, 81):
            row_output = []
            for label in ["A", "B", "C", "D", "E", "F"]:
                seat_id = f"{i}{label}"
                if seat_id in self.seats:
                    state = self.seats[seat_id]
                    if state in ["F", "S"]:
                        row_output.append(f"{seat_id}({state})")
                    else:
                        row_output.append(f"{seat_id}(Booked)")
            print(" ".join(row_output))

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
            passport_number = input("Enter passenger passport number: ")
            first_name = input("Enter passenger first name: ")
            last_name = input("Enter passenger last name: ")
            print(system.book_seat(seat_id, passport_number, first_name, last_name))
        elif choice == 3:
            seat_id = input("Enter seat ID to free (e.g., 1A): ")
            print(system.free_seat(seat_id))
        elif choice == 4:
            system.show_booking_state()
        elif choice == 5:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
