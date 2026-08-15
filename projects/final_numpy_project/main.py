# ================================================================================
#           STUDENT PERFORMANCE & DATA QUALITY ANALYZER
#      A Comprehensive NumPy Project (Sections 01–12)
#                     SOURCE CODE
# ================================================================================

# This Python script implements a complete student performance and data quality
# analyzer using NumPy. It generates synthetic data, cleans it, and performs
# statistical analysis, categorization, correlation, and identification of
# students needing attention.

# Run the script directly after installing NumPy:
#     pip install numpy
#     python student_analyzer.py

# ================================================================================
# CODE (student_analyzer.py)
# ================================================================================
# */

import numpy as np

# ============================================================================
# 1. DATA GENERATION
# ============================================================================

# Set random seed for reproducibility
np.random.seed(42)

NUM_STUDENTS = 100
SUBJECTS = ['Mathematics', 'Physics', 'Chemistry', 'English', 'Networking']

# Student IDs: 101 to 200, with intentional duplicates to test set operations
student_ids = np.arange(101, 101 + NUM_STUDENTS)
student_ids[5] = 103      # duplicate of ID 103
student_ids[12] = 108     # duplicate of ID 108

# Marks: 100 students × 5 subjects, scores 0–100
marks = np.random.randint(0, 101, size=(NUM_STUDENTS, len(SUBJECTS))).astype(float)

# Introduce missing values (NaN) in ~5% of entries
nan_mask = np.random.random(marks.shape) < 0.05
marks[nan_mask] = np.nan

# Attendance: percentage between 50% and 100%
attendance = np.random.uniform(50, 100, size=NUM_STUDENTS)

# ============================================================================
# 2. DATA QUALITY ANALYSIS
# ============================================================================

def data_quality_report(ids, marks, attendance):
    """Check for missing values and duplicate IDs."""
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

# ============================================================================
# 3. PERFORMANCE STATISTICS
# ============================================================================

# Average score per student (mean across subjects)
avg_scores = np.mean(cleaned_marks, axis=1)

print("\n---------- PERFORMANCE ----------")
print(f"Average Score: {np.mean(avg_scores):.2f}")
print(f"Highest Score: {np.max(avg_scores):.2f}")
print(f"Lowest Score:  {np.min(avg_scores):.2f}")
print(f"Median Score:  {np.median(avg_scores):.2f}")

# ============================================================================
# 4. PERFORMANCE LEVEL CLASSIFICATION
# ============================================================================

def classify_performance(scores):
    """Categorize scores into performance levels."""
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

# ============================================================================
# 5. SUBJECT ANALYSIS (best/weakest)
# ============================================================================

subject_means = np.nanmean(marks, axis=0)  # mean per subject (using original marks with NaN)
best_subj_idx = np.argmax(subject_means)
weakest_subj_idx = np.argmin(subject_means)

print("\n---------- SUBJECT ANALYSIS ----------")
print(f"Best Subject:    {SUBJECTS[best_subj_idx]} ({subject_means[best_subj_idx]:.2f})")
print(f"Weakest Subject: {SUBJECTS[weakest_subj_idx]} ({subject_means[weakest_subj_idx]:.2f})")

# ============================================================================
# 6. ATTENDANCE ANALYSIS
# ============================================================================

avg_attendance = np.mean(attendance)
print(f"\n---------- ATTENDANCE ----------")
print(f"Average Attendance: {avg_attendance:.1f}%")

# ============================================================================
# 7. CORRELATION ANALYSIS (Attendance vs Score)
# ============================================================================

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

# ============================================================================
# 8. STUDENTS REQUIRING ATTENTION
# ============================================================================

# Criteria: avg_score < 50 OR attendance < 70%
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

# ============================================================================
# 9. TOP PERFORMERS (optional bonus)
# ============================================================================

sorted_idx = np.argsort(avg_scores)[::-1]  # indices in descending order
print("\nTop 5 Students (ID, Avg Score):")
for i in range(min(5, NUM_STUDENTS)):
    idx = sorted_idx[i]
    print(f"  {i+1}. ID {int(student_ids[idx])}: {avg_scores[idx]:.1f}")

print("\n========== ANALYSIS COMPLETE ==========")

# ============================================================================
# END OF CODE
# ============================================================================