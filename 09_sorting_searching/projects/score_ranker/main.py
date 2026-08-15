import numpy as np


def rank_scores(scores):
    return np.argsort(scores)[::-1]


def show_top_scores(scores, count=3):
    ranking = rank_scores(scores)

    print(f"\nTop {count} scores:")

    for position in range(count):
        index = ranking[position]
        print(f"{position + 1}. Score: {scores[index]} (Index: {index})")


scores = np.array([78, 45, 92, 67, 88, 34, 95, 73, 81, 59])

print("Original scores:")
print(scores)

print("\nHighest score:")
print(np.max(scores))

print("\nHighest score index:")
print(np.argmax(scores))

print("\nLowest score:")
print(np.min(scores))

print("\nLowest score index:")
print(np.argmin(scores))

print("\nScores in descending order:")
print(np.sort(scores)[::-1])

show_top_scores(scores)


# Example of correcting invalid scores
scores_with_invalid = np.array([78, -10, 92, 105, 88])

print("\nScores with invalid values:")
print(scores_with_invalid)

cleaned_scores = np.clip(scores_with_invalid, 0, 100)

print("\nScores after clipping:")
print(cleaned_scores)


# Example of updating specific scores
updated_scores = scores.copy()

np.put(updated_scores, [1, 5], [50, 40])

print("\nUpdated scores:")
print(updated_scores)