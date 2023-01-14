import pandas as pd

results = []

while True:
    # Get student's name and quiz score
    name = input("Enter the student's name (or 'q' to quit): ")
    if name == 'q':
        break
    score = float(input("Enter the student's score: "))

    # Add student's name and score to the list
    results.append([name, score])

# Create a DataFrame from the results
results_df = pd.DataFrame(results, columns=["Name", "Score"])

# Save the DataFrame to a csv file
results_df.to_csv("quiz_results.csv", index=False)

