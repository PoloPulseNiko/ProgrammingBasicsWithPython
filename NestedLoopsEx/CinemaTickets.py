total_tickets = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        break

    seats = int(input())
    tickets_sold = 0

    while tickets_sold < seats:
        ticket_type = input()
        if ticket_type == "End":
            break

        tickets_sold += 1
        total_tickets += 1

        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kids_tickets += 1

    percentage_full = (tickets_sold / seats) * 100
    print(f"{movie_name} - {percentage_full:.2f}% full.")

print(f"Total tickets: {total_tickets}")
print(f"{(student_tickets / total_tickets) * 100:.2f}% student tickets.")
print(f"{(standard_tickets / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(kids_tickets / total_tickets) * 100:.2f}% kids tickets.")