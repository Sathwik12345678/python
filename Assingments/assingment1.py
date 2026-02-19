business_seats = [0] * 10
economy_seats = [0] * 20

business_booked = []
economy_booked = []

business_count = 0
economy_count = 0

balance = 5000

print("Select Airline")
print("1. Kingfisher Airlines")
print("2. Quatar Airways")
print("3. Emirates Airlines")
airline = int(input("Enter airline choice: "))

if airline == 1:
    airline_name = "Kingfisher Airlines"
elif airline == 2:
    airline_name = "Quatar Airways"
elif airline == 3:
    airline_name = "Emirates Airlines"
else:
    airline_name = "Unknown"

while True:

    # Reset values for each booking attempt
    seat_booked = False
    total_payment = 0

    if business_count == 10 and economy_count == 20:
        print("Flight is already booked, try another flight.")
        break

    print("\nSelect Class")
    print("1. Business Class")
    print("2. Economy Class")
    class_choice = int(input("Enter class choice: "))

    # ---------- BUSINESS CLASS ----------
    if class_choice == 1:

        if business_count == 10:
            print("Business class is already booked, try Economy class.")

        else:
            seat = int(input("Enter seat number (1 to 10): "))

            if seat < 1 or seat > 10:
                print("Invalid seat number.")

            elif business_seats[seat - 1] == 1:
                print("Seat already booked, choose another seat.")

            else:
                business_seats[seat - 1] = 1
                business_booked.append(seat)
                business_count += 1
                seat_booked = True

                if seat <= 5:
                    price = 600
                else:
                    price = 800

                total_payment = price
                print(f"Seat {seat} booked in Business Class for ${price}.")

    # ---------- ECONOMY CLASS ----------
    elif class_choice == 2:

        if economy_count == 20:
            print("Economy class is already booked, try Business class.")

        else:
            seat = int(input("Enter seat number (1 to 20): "))

            if seat < 1 or seat > 20:
                print("Invalid seat number.")

            elif economy_seats[seat - 1] == 1:
                print("Seat already booked, choose another seat.")

            else:
                economy_seats[seat - 1] = 1
                economy_booked.append(seat)
                economy_count += 1
                seat_booked = True

                if seat <= 10:
                    price = 450
                else:
                    price = 500

                total_payment = price
                print(f"Seat {seat} booked in Economy Class for ${price}.")

    else:
        print("Invalid class choice")
        continue

    # ---------- PAYMENT ----------
    if seat_booked:

        print("\nTotal amount to pay: $", total_payment)
        payment = int(input("Enter payment amount: "))

        if payment >= total_payment:

            balance -= total_payment

            print("\nPAYMENT SUCCESSFUL")
            print("Ticket Booked")
            print("Airline Name:", airline_name)

            if business_booked:
                print("Business Seat Number Booked:", business_booked)

            if economy_booked:
                print("Economy Seat Number Booked:", economy_booked)

            print("Remaining Balance: $", balance)

        else:
            print("Something went wrong, please try again")

    else:
        print("No new seat booked. Payment skipped.")

    # ---------- CONTINUE OR EXIT ----------
    print("\nWhat do you want to do next?")
    print("1. Book again")
    print("2. Exit")
    option = int(input("Enter choice: "))

    if option == 2:
        print("Thank you for using the Airline Booking System.")
        break
