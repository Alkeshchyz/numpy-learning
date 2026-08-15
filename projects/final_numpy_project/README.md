
================================================================================
          STUDENT PERFORMANCE & DATA QUALITY ANALYZER
     A Comprehensive NumPy Project (Sections 01–12)
================================================================================

OVERVIEW
--------
The Student Performance & Data Quality Analyzer is a comprehensive NumPy project
that combines concepts from all previous sections to analyze a realistic student
dataset. It demonstrates how to create, clean, manipulate, and analyze numerical
data using NumPy.

This project brings together:
  • Array creation and arithmetic
  • Indexing, slicing, and reshaping
  • Boolean and advanced indexing
  • Broadcasting
  • Custom functions
  • Missing value handling (NaN)
  • Sorting and searching
  • Array manipulation (append, delete, etc.)
  • Statistical analysis (mean, median, std, percentile, correlation)
  • Set operations (unique, union, etc.)

The program generates a synthetic dataset of 100 students with marks in 5
subjects, attendance records, and student IDs (including some duplicates and
missing values). It then performs data quality checks, computes performance
metrics, identifies top/bottom performers, analyzes subject strengths/weaknesses,
and evaluates the relationship between attendance and scores.

================================================================================
PROJECT OBJECTIVE
================================================================================
The objective is to apply all NumPy techniques learned across Sections 01–12 to
a single, practical data analysis task. The analyzer answers key questions:

  1. How clean is the data? (missing values, duplicates)
  2. What are the overall performance statistics? (mean, median, extremes)
  3. How are students distributed across performance levels?
  4. Which subject is the strongest and weakest?
  5. What is the average attendance?
  6. Is there a correlation between attendance and performance?
  7. Which students need attention?

================================================================================
DATASET (GENERATED)
================================================================================
We generate synthetic data for 100 students:

  • Student IDs: 101 to 200 (with a few duplicates to test set operations)
  • Marks: 5 subjects (Math, Physics, Chemistry, English, Networking)
    - Values randomly generated between 0 and 100.
    - About 5% missing values (NaN) inserted randomly.
  • Attendance: Percentage between 50% and 100%, generated as floats.

The dataset is stored in NumPy arrays.

================================================================================
PROJECT FEATURES
================================================================================
1. Data Quality Analysis
   - Detect and count missing (NaN) values.
   - Identify duplicate student IDs using set operations.
   - Clean missing values by replacing with subject-wise means.

2. Performance Statistics
   - Compute overall mean, median, maximum, minimum, and standard deviation.
   - Calculate average score per student (mean of their subjects).

3. Performance Level Classification
   - Categorize students into:
       Excellent (≥ 80)
       Good      (70 – 79)
       Average   (50 – 69)
       Poor      (< 50)
   - Count students in each category.

4. Subject Analysis
   - Compute mean score for each subject.
   - Identify the best (highest mean) and weakest (lowest mean) subject.

5. Attendance Analysis
   - Calculate average attendance across all students.
   - Optionally, count students with low attendance (< 70%).

6. Correlation Analysis
   - Compute Pearson correlation between attendance and average score.
   - Interpret the strength of the relationship.

7. Summary of Students Requiring Attention
   - Identify students with average score below 50 OR attendance below 70%.
   - Display their IDs and details.

================================================================================
NUMPY CONCEPTS DEMONSTRATED
================================================================================
+----------------------------+--------------------------------------------------+
| Concept / Function         | Usage                                            |
+----------------------------+--------------------------------------------------+
| np.array, np.arange        | Create arrays                                    |
| np.random                  | Generate synthetic data                          |
| np.isnan, np.nanmean       | Detect and handle missing values                 |
| np.unique, np.setdiff1d    | Duplicate detection and set operations           |
| np.mean, np.median, np.std | Basic statistics                                 |
| np.percentile              | Percentile analysis                              |
| np.max, np.min, np.argmax  | Extremes and their indices                       |
| np.where / Boolean indexing| Conditional operations                           |
| np.corrcoef                | Correlation between two variables                |
| np.sort, np.argsort        | Sorting and ranking                              |
| np.reshape, np.concatenate | Array manipulation                               |
| Broadcasting               | Applying operations across axes                  |
| Custom functions           | Reusable analysis code                           |
+----------------------------+--------------------------------------------------+

================================================================================
PROJECT STRUCTURE
================================================================================
student_performance_analyzer/
├── main.py          # Complete program
└── README.md        # This document

================================================================================
HOW TO RUN
================================================================================
1. Ensure NumPy is installed:
   pip install numpy

2. Run the program:
   python main.py

3. The program generates random data, performs all analyses, and prints a
   formatted report to the console.

================================================================================
CODE (main.py)
================================================================================
```python
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# -------------------- DATA GENERATION --------------------
NUM_STUDENTS = 100
SUBJECTS = ['Mathematics', 'Physics', 'Chemistry', 'English', 'Networking']

# Student IDs: 101 to 200, but introduce duplicates (simulate data entry errors)
student_ids = np.arange(101, 101 + NUM_STUDENTS)
# Insert duplicates: replace a few IDs with earlier ones
student_ids[5] = 103      # duplicate of ID 103
student_ids[12] = 108     # duplicate of ID 108

# Marks: 100 students x 5 subjects, scores between 0 and 100
marks = np.random.randint(0, 101, size=(NUM_STUDENTS, len(SUBJECTS))).astype(float)

# Introduce missing values (NaN) randomly in ~5% of entries
nan_mask = np.random.random(marks.shape) < 0.05
marks[nan_mask] = np.nan

# Attendance: percentage between 50% and 100%
attendance = np.random.uniform(50, 100, size=NUM_STUDENTS)

# -------------------- DATA QUALITY ANALYSIS --------------------
def data_quality_report(ids, marks, attendance):
    print("\n---------- DATA QUALITY ----------")

    # Missing values
    total_nan = np.isnan(marks).sum()
    print(f"Missing Values: {total_nan}")

    # Duplicate student IDs
    unique_ids, counts = np.unique(ids, return_counts=True)
    duplicates = unique_ids[counts > 1]
    print(f"Duplicate Student IDs: {len(duplicates)}")
    if len(duplicates) > 0:
        print(f"  Duplicate ID(s): {duplicates}")

    # Clean marks: replace NaN with subject-wise mean
    cleaned_marks = marks.copy()
    for subj_idx in range(cleaned_marks.shape[1]):
        col = cleaned_marks[:, subj_idx]
        col_mean = np.nanmean(col)
        col[np.isnan(col)] = col_mean
    return cleaned_marks

cleaned_marks = data_quality_report(student_ids, marks, attendance)

# -------------------- PERFORMANCE STATISTICS --------------------
# Compute average score per student (across subjects)
avg_scores = np.mean(cleaned_marks, axis=1)

print("\n---------- PERFORMANCE ----------")
print(f"Average Score: {np.mean(avg_scores):.2f}")
print(f"Highest Score: {np.max(avg_scores):.2f}")
print(f"Lowest Score:  {np.min(avg_scores):.2f}")
print(f"Median Score:  {np.median(avg_scores):.2f}")

# -------------------- PERFORMANCE LEVELS --------------------
def classify_performance(scores):
    conditions = [
        scores >= 80,
        (scores >= 70) & (scores < 80),
        (scores >= 50) & (scores < 70),
        scores < 50
    ]
    categories = ['Excellent', 'Good', 'Average', 'Poor']
    return np.select(conditions, categories)

levels = classify_performance(avg_scores)
unique, counts = np.unique(levels, return_counts=True)
print("\n---------- PERFORMANCE LEVEL ----------")
for level, count in zip(unique, counts):
    print(f"{level}: {count}")

# -------------------- SUBJECT ANALYSIS --------------------
subject_means = np.nanmean(marks, axis=0)  # mean per subject (original NaN still present)
best_subj_idx = np.argmax(subject_means)
weakest_subj_idx = np.argmin(subject_means)

print("\n---------- SUBJECT ANALYSIS ----------")
print(f"Best Subject:    {SUBJECTS[best_subj_idx]} ({subject_means[best_subj_idx]:.2f})")
print(f"Weakest Subject: {SUBJECTS[weakest_subj_idx]} ({subject_means[weakest_subj_idx]:.2f})")

# -------------------- ATTENDANCE ANALYSIS --------------------
avg_attendance = np.mean(attendance)
print(f"\n---------- ATTENDANCE ----------")
print(f"Average Attendance: {avg_attendance:.1f}%")

# -------------------- CORRELATION ANALYSIS --------------------
corr_matrix = np.corrcoef(attendance, avg_scores)
corr = corr_matrix[0, 1]
print(f"\n---------- CORRELATION ----------")
print(f"Attendance vs Score: {corr:.2f}")
if corr > 0.7:
    print("  (Strong positive relationship)")
elif corr > 0.4:
    print("  (Moderate positive relationship)")
elif corr > -0.4:
    print("  (Weak/no linear relationship)")
else:
    print("  (Negative relationship)")

# -------------------- STUDENTS REQUIRING ATTENTION --------------------
# Consider those with avg_score < 50 OR attendance < 70%
attention_mask = (avg_scores < 50) | (attendance < 70)
attention_ids = student_ids[attention_mask]
attention_scores = avg_scores[attention_mask]
attention_att = attendance[attention_mask]

print(f"\n---------- FINAL SUMMARY ----------")
print(f"Students analyzed: {NUM_STUDENTS}")
print(f"Students requiring attention: {len(attention_ids)}")
if len(attention_ids) > 0:
    print("\nDetails (ID, Avg Score, Attendance):")
    for i, (sid, score, att) in enumerate(zip(attention_ids, attention_scores, attention_att), 1):
        print(f"  {i}. ID {int(sid)}: Score {score:.1f}, Attendance {att:.1f}%")

# Optional: Display top 5 performers
sorted_idx = np.argsort(avg_scores)[::-1]
print("\nTop 5 Students (ID, Avg Score):")
for i in range(5):
    idx = sorted_idx[i]
    print(f"  {i+1}. ID {int(student_ids[idx])}: {avg_scores[idx]:.1f}")

print("\n========== ANALYSIS COMPLETE ==========")
================================================================================
EXPECTED OUTPUT (SAMPLE)
================================================================================
Since the data is randomly generated, actual numbers will differ. Below is an
example of the output format:

text
========== STUDENT PERFORMANCE ANALYZER ==========

Total Students: 100
Subjects: 5

---------- DATA QUALITY ----------
Missing Values: 7
Duplicate Student IDs: 2
  Duplicate ID(s): [103 108]

---------- PERFORMANCE ----------
Average Score: 72.45
Highest Score: 98.00
Lowest Score:  34.00
Median Score:  74.00

---------- PERFORMANCE LEVEL ----------
Excellent: 18
Good:       42
Average:    31
Poor:        9

---------- SUBJECT ANALYSIS ----------
Best Subject:    Mathematics (78.20)
Weakest Subject: Networking (66.50)

---------- ATTENDANCE ----------
Average Attendance: 84.7%

---------- CORRELATION ----------
Attendance vs Score: 0.81
  (Strong positive relationship)

---------- FINAL SUMMARY ----------
Students analyzed: 100
Students requiring attention: 14

Details (ID, Avg Score, Attendance):
  1. ID 105: Score 44.0, Attendance 62.5%
  2. ID 112: Score 47.2, Attendance 69.8%
  ...

Top 5 Students (ID, Avg Score):
  1. ID 145: 98.0
  2. ID 162: 96.5
  ...

========== ANALYSIS COMPLETE ==========
================================================================================
KEY TAKEAWAYS
================================================================================
Through this project, I practiced:

• Generating and manipulating synthetic datasets.
• Detecting and handling missing values with NumPy.
• Using set operations to find duplicates.
• Computing descriptive statistics and percentiles.
• Classifying data using boolean indexing and np.select.
• Identifying extremes and their indices.
• Performing correlation analysis to uncover relationships.
• Combining multiple NumPy operations into a cohesive analysis pipeline.
• Writing modular, reusable code with custom functions.
• Producing actionable insights from raw data.

================================================================================
FUTURE IMPROVEMENTS
================================================================================

Load real data from CSV files.

Add student names and demographic information.

Export results to a report file.

Visualize distributions and trends using Matplotlib.

Implement outlier detection (e.g., IQR method).

Allow interactive filtering and querying.

Compare performance across different classes or years.

================================================================================
STATUS
================================================================================
Section: Combined (Sections 01–12)
Project: Student Performance & Data Quality Analyzer
Status: ✅ Completed
Language: Python
Library: NumPy

================================================================================
End of Document
================================================================================

