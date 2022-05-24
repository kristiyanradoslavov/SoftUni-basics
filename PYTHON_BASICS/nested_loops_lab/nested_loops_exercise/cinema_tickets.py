current_input = input()

total_tickets_all = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0


while current_input != "Finish":
    movie_name = current_input
    available_seats = int(input())

    total_tickets_taken_per_movie = 0
    capacity = 0

    seats_input = input()

    while seats_input != "End":
        ticket_type = seats_input
        total_tickets_taken_per_movie += 1
        total_tickets_all += 1
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kids_tickets += 1

        capacity = total_tickets_taken_per_movie / available_seats * 100

        if capacity == 100:
            print(f"{movie_name} - {capacity:.2f}% full.")
            break
        seats_input = input()

    if seats_input == "End":
        print(f"{movie_name} - {capacity:.2f}% full.")

    current_input = input()

student_percent = student_tickets / total_tickets_all * 100
standard_percent = standard_tickets / total_tickets_all * 100
kids_percent = kids_tickets / total_tickets_all * 100

if current_input == "Finish":
    print(f"Total tickets: {total_tickets_all}")
    print(f"{student_percent:.2f}% student tickets.")
    print(f"{standard_percent:.2f}% standard tickets.")
    print(f"{kids_percent:.2f}% kids tickets.")
