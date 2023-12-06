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

# Calculate ways to win for each course and multiply them
# Updated course details for the single long race
time_limit_long_race = 41968894
distance_record_long_race = 214178911271055

# Calculate ways to win for the long race
ways_to_win_long_race = calculate_ways_to_win(time_limit_long_race, distance_record_long_race)
print(ways_to_win_long_race)
