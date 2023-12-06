def calculate_ways_to_win(time_limit, distance_record):
    # Function to calculate the number of ways to win the race
    ways_to_win = 0
    for button_press_time in range(time_limit + 1):
        # Calculate the speed after button is released
        speed = button_press_time
        # Calculate the remaining time for the boat to move
        remaining_time = time_limit - button_press_time
        # Calculate the distance covered
        distance_covered = speed * remaining_time
        # Check if this distance is greater than the record
        if distance_covered > distance_record:
            ways_to_win += 1
    return ways_to_win

# Course details
courses = [
    (41, 214),    # (time_limit, distance_record)
    (96, 1789),
    (88, 1127),
    (94,1055)
]

# Calculate ways to win for each course and multiply them
total_ways = 1
for time_limit, distance_record in courses:
    ways = calculate_ways_to_win(time_limit, distance_record)
    total_ways *= ways

print(total_ways)
