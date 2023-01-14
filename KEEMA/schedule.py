import pandas as pd

# Create an empty list to store the schedule
schedule = []

# Get the schedule from the user
while True:
    event = input("Enter the event (or 'q' to quit): ")
    if event == 'q':
        break
    time = input("Enter the time: ")
    schedule.append([event, time])

# Create a DataFrame from the schedule
schedule_df = pd.DataFrame(schedule, columns=["Event", "Time"])

# Print the schedule
print(schedule_df)


