import pandas as pd

file_path = "jobss.csv"

data = pd.read_csv(file_path)

#  Fill the 'Unnamed: 1' column with unique IDs for each applicant
data['Unnamed: 1'] = range(1, len(data) + 1)

#  Rename the column to 'Applicant ID' for clarity
data.rename(columns={'Unnamed: 1': 'Applicant ID'}, inplace=True)

#  Display the updated dataframe
print(data.head())

# Save the updated DataFrame to a new CSV file
data.to_csv("updated_jobss.csv", index=False)

print("File saved as 'updated_jobss.csv'")


