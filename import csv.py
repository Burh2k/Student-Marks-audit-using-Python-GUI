import csv

def evaluate_marks(marks_csv):
  # Initialize a dictionary to store the results
  results = {}

  # Open the CSV file and read the marks
  with open(marks_csv, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # Read the header row
    
    # Prompt the user to input the types of assessments
    types = input("Enter the types of assessments (comma-separated): ").split(',')
    
    # Find the indices of the columns that correspond to the types of assessments
    indices = {}
    for t in types:
      indices[t] = []
      i = 2  # Skip the first two columns (name and roll number)
      while True:
        try:
          index = header.index(t, i)
          indices[t].append(index)
          i = index + 1
        except ValueError:
          break
    
    # Prompt the user to input the weightages for each assessment
    weightages = {}
    for t in types:
      weightages[t] = []
      for i in range(len(indices[t])):
        weightage = input(f"Enter the weightage for {t} {i+1}: ")
        weightages[t].append(float(weightage))
    
    # Read the marks for each student
    for row in reader:
      student_id = row[1]  # Use the roll number as the student ID
      marks = {}
      for t in types:
        marks[t] = [float(row[i]) for i in indices[t]]

      # Calculate the weighted marks for each student
      weighted_marks = {}
      for t in types:
        weighted_marks[t] = []
        for i, mark in enumerate(marks[t]):
          weighted_marks[t].append(mark * weightages[t][i] / 100)

      # Calculate the final marks for each student
      final_marks = {}
      for t in types:
        if t == 'exam':
          final_marks[t] = sum([weighted_marks[x] for x in types if x == 'exam'])
        else:
          final_marks[t] = sum(weighted_marks[t])

      # Store the results for each student in the dictionary
      results[student_id] = final_marks
  
  # Prompt the user to input the name of the output CSV file
  output_csv = input("Enter the name of the output CSV file: ")
  
  # Write the results to the output CSV file
 
  with open(output_csv, 'w', newline='') as f:
    writer = csv.writer(f)
    
    # Write the header row
    header = ['Roll numbers', 'Names'] + types
    writer.writerow(header)
    
    # Write the results for each student
    for student_id, marks in results.items():
      row = [student_id, marks['Names']] + [marks[t] for t in types]
      writer.writerow(row)

# Example usage
marks_csv = 'test.csv'
results = evaluate_marks(marks_csv)
print(results)
