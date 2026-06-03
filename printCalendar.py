def print_calendar(start_day, total_days):
    # 0: Mon, 1: Tue, 2: Wed, 3: Thu, 4: Fri, 5: Sat, 6: Sun
    header = "Mon Tue Wed Thu Fri Sat Sun"
    print(header)

    # Step 1: Print the leading empty spaces
    # Each day in our format occupies 4 spaces (3 for number/space + 1 gap)
    for i in range(start_day):
        print("    ", end="")

    # Step 2: Print the actual days
    for day in range(1, total_days + 1):
        # Format the number to be 3 characters wide
        print(f"{day:3}", end=" ")

        # Step 3: Check if we need a new line
        # If (offset + current day) is a multiple of 7, the row is full
        if (start_day + day) % 7 == 0:
            print()
    print()

# print June: Starts on Thursday (3), has 30 days
print_calendar(3, 30)
