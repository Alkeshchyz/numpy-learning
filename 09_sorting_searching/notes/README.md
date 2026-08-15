================================================================================
                           SCORE RANKER
              NumPy Project – Section 09 (Sorting & Searching)
================================================================================

OVERVIEW
--------
Score Ranker is a practical NumPy project that analyzes student scores,
ranks them, identifies the highest and lowest scores, and handles invalid
or updated values. It demonstrates how sorting and searching operations can
be applied to real-world data analysis.

================================================================================
PROJECT OBJECTIVE
================================================================================

The purpose of this project is to apply the concepts learned in Section 09 —
Sorting & Searching to a practical score-analysis program.

The project demonstrates how NumPy can be used to:
  • Sort scores
  • Find ranking positions
  • Find the highest and lowest scores
  • Find the indices of extreme values
  • Display the top-performing students
  • Correct invalid scores
  • Update specific array elements

================================================================================
DATASET
================================================================================

The project uses the following student scores:

    import numpy as np

    scores = np.array([78, 45, 92, 67, 88, 34, 95, 73, 81, 59])

There are 10 scores in the dataset.

================================================================================
1. SORTING SCORES
================================================================================

The project uses np.sort(scores) to arrange scores in ascending order.

For descending order:
    np.sort(scores)[::-1]

The [::-1] slice reverses the sorted array.

Example:
    Ascending:   [34 45 59 67 73 78 81 88 92 95]
    Descending:  [95 92 88 81 78 73 67 59 45 34]

================================================================================
2. RANKING SCORES WITH np.argsort()
================================================================================

The project uses np.argsort(scores) to obtain the indices that would sort
the scores in ascending order.

To rank from highest to lowest:
    np.argsort(scores)[::-1]

This is useful because it preserves the connection between each score and
its original position (index).

Example:
    np.argsort(scores)         → [5, 1, 9, 3, 7, 0, 8, 4, 2, 6]
    np.argsort(scores)[::-1]   → [6, 2, 4, 8, 0, 7, 3, 9, 1, 5]

Interpretation:
    Index 6 has the highest score (95)
    Index 2 has the second highest score (92)
    Index 4 has the third highest score (88)
    and so on.

================================================================================
3. FINDING THE HIGHEST SCORE
================================================================================

The project uses np.max(scores) to find the highest score.

For the dataset:
    Highest score: 95

The position of the highest score is found using np.argmax(scores):
    Index: 6

================================================================================
4. FINDING THE LOWEST SCORE
================================================================================

The project uses np.min(scores) to find the lowest score.

For the dataset:
    Lowest score: 34

Its index is found using np.argmin(scores):
    Index: 5

================================================================================
5. DISPLAYING THE TOP SCORES
================================================================================

A custom function is used to create a ranking based on descending scores:

    def rank_scores(scores):
        return np.argsort(scores)[::-1]

Another function displays the top-performing scores:

    def show_top_scores(scores, count=3):
        ranked = rank_scores(scores)
        for i in range(count):
            idx = ranked[i]
            print(f"{i+1}. Score: {scores[idx]} (Index: {idx})")

Example output for top 3 scores:
    1. Score: 95 (Index: 6)
    2. Score: 92 (Index: 2)
    3. Score: 88 (Index: 4)

================================================================================
6. CORRECTING INVALID SCORES WITH np.clip()
================================================================================

The project demonstrates handling invalid scores:

    scores_with_invalid = np.array([78, -10, 92, 105, 88])

Some values are outside the valid score range of 0–100.

The project uses:
    np.clip(scores_with_invalid, 0, 100)

Values below 0 become 0, while values above 100 become 100.

Example:
    Before:  [ 78 -10  92 105  88]
    After:   [78   0  92 100  88]

================================================================================
7. UPDATING SCORES WITH np.put()
================================================================================

The project also demonstrates updating specific elements.

First, a copy is created:
    updated_scores = scores.copy()

Then:
    np.put(updated_scores, [1, 5], [50, 40])

This updates:
    Index 1 → 50
    Index 5 → 40

Example:
    Original:  [78 45 92 67 88 34 95 73 81 59]
    Updated:   [78 50 92 67 88 40 95 73 81 59]

================================================================================
CONCEPTS DEMONSTRATED
================================================================================

+---------------------+--------------------------------------------------------+
| NumPy Concept       | Purpose                                                |
+---------------------+--------------------------------------------------------+
| np.sort()           | Sort scores in ascending order                         |
| np.argsort()        | Get sorting/ranking indices                            |
| np.max()            | Find the highest value                                 |
| np.min()            | Find the lowest value                                  |
| np.argmax()         | Find the index of the highest value                    |
| np.argmin()         | Find the index of the lowest value                     |
| np.clip()           | Restrict values to a valid range                       |
| np.put()            | Update specific array elements                         |
| Array slicing       | Reverse sorted arrays ([::-1])                         |
| Custom functions    | Create reusable ranking logic                          |
+---------------------+--------------------------------------------------------+

================================================================================
PROJECT STRUCTURE
================================================================================

    score_ranker/
    ├── main.py
    └── README.md

  main.py    – Contains the complete score-ranking and analysis program.
  README.md  – Contains documentation explaining the project and NumPy
               concepts used.

================================================================================
HOW TO RUN
================================================================================

1. Make sure NumPy is installed:

    pip install numpy

2. Run the program from the project directory:

    python main.py

================================================================================
EXPECTED OUTPUT
================================================================================

Original scores:
[78 45 92 67 88 34 95 73 81 59]

Highest score:
95

Highest score index:
6

Lowest score:
34

Lowest score index:
5

Scores in descending order:
[95 92 88 81 78 73 67 59 45 34]

Ranking indices (highest to lowest):
[6 2 4 8 0 7 3 9 1 5]

Top 3 scores:
1. Score: 95 (Index: 6)
2. Score: 92 (Index: 2)
3. Score: 88 (Index: 4)

Scores with invalid values:
[ 78 -10  92 105  88]

Scores after clipping (0-100 range):
[ 78   0  92 100  88]

Updated scores (after np.put):
[78 50 92 67 88 40 95 73 81 59]

================================================================================
KEY TAKEAWAYS
================================================================================

This project helped me understand how to:

  • Sort numerical data using np.sort()
  • Create rankings using indices with np.argsort()
  • Find maximum and minimum values
  • Locate values inside an array using argmax/argmin
  • Extract top-performing scores
  • Handle invalid numerical values using np.clip()
  • Update specific array elements using np.put()
  • Combine multiple NumPy operations into one practical program

================================================================================
FUTURE IMPROVEMENTS
================================================================================

Possible improvements include:

  • Store student names alongside scores
  • Display student names in the ranking
  • Calculate grades automatically (A, B, C, etc.)
  • Calculate class average and statistics
  • Read scores from a CSV file
  • Allow users to enter scores interactively
  • Create a complete student ranking system
  • Add data visualization (bar charts, histograms)
  • Export ranking results to a file

================================================================================
QUICK REFERENCE
================================================================================

+---------------------+--------------------------------------------------------+
| Function / Concept  | Description                                            |
+---------------------+--------------------------------------------------------+
| np.sort(arr)        | Returns sorted array (ascending)                       |
| np.sort(arr)[::-1]  | Returns sorted array (descending)                      |
| np.argsort(arr)     | Returns indices that would sort the array              |
| np.argsort(arr)[::-1]| Returns indices for descending ranking                |
| np.max(arr)         | Returns the maximum value                              |
| np.min(arr)         | Returns the minimum value                              |
| np.argmax(arr)      | Returns the index of the maximum value                 |
| np.argmin(arr)      | Returns the index of the minimum value                 |
| np.clip(arr, min, max)| Clips values to the specified range                  |
| np.put(arr, indices, values)| Updates elements at specific indices            |
| arr.copy()          | Creates a copy of the array                            |
+---------------------+--------------------------------------------------------+

================================================================================
STATUS
================================================================================

  Status       : ✅ Completed
  Section      : 09 — Sorting & Searching
  Project      : Score Ranker
  Language     : Python
  Library      : NumPy

================================================================================
End of Document
================================================================================