import csv
import os
from collections import defaultdict
import openpyxl

def create_student_scores_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Subject", "Score"])
            writer.writerow(["Alice", "Math", 85])
            writer.writerow(["Bob", "Math", 90])
            writer.writerow(["Alice", "Science", 95])
            writer.writerow(["Bob", "Science", 80])
            writer.writerow(["Charlie", "Math", 70])
            writer.writerow(["Charlie", "Science", 75])
        print(f"Created {file_path} with sample data.")

def read_student_data(file_path):
    student_scores = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student_scores.append({
                    'Name': row['Name'],
                    'Subject': row['Subject'],
                    'Score': float(row['Score'])
                })
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return student_scores

def analyze_data(student_scores):
    student_totals = defaultdict(lambda: {'total_score': 0, 'count': 0})
    subject_totals = defaultdict(lambda: {'total_score': 0, 'count': 0})

    for entry in student_scores:
        name = entry['Name']
        subject = entry['Subject']
        score = entry['Score']

        student_totals[name]['total_score'] += score
        student_totals[name]['count'] += 1

        subject_totals[subject]['total_score'] += score
        subject_totals[subject]['count'] += 1

    student_averages = {name: totals['total_score'] / totals['count'] for name, totals in student_totals.items()}
    subject_averages = {subject: totals['total_score'] / totals['count'] for subject, totals in subject_totals.items()}

    return student_averages, subject_averages

def write_results_to_excel(student_averages, subject_averages, output_file):
    workbook = openpyxl.Workbook()
    
    student_sheet = workbook.active
    student_sheet.title = "Student Averages"
    student_sheet.append(["Name", "Average Score"])  

    for name, avg_score in student_averages.items():
        student_sheet.append([name, round(avg_score, 2)])  

    subject_sheet = workbook.create_sheet(title="Subject Averages")
    subject_sheet.append(["Subject", "Average Score"])  

    for subject, avg_score in subject_averages.items():
        subject_sheet.append([subject, round(avg_score, 2)])  

    workbook.save(output_file)
    print(f"Results saved to {output_file}")

def main():
    input_file = 'student_scores.csv'
    output_file = 'results.xlsx'

    create_student_scores_file(input_file)  
    student_scores = read_student_data(input_file)

    if student_averages:
        student_averages, subject_averages = analyze_data(student_scores)
        write_results_to_excel(student_averages, subject_averages, output_file)

if __name__ == '__main__':
    main()