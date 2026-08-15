import numpy as np


def add_values(data, values):
    return np.append(data, values)


def combine_arrays(first, second):
    return np.concatenate((first, second))


def remove_values(data, indices):
    return np.delete(data, indices)


def array_information(data):
    print("\nArray:")
    print(data)

    print("Dimensions:", np.ndim(data))
    print("Shape:", data.shape)
    print("Size:", data.size)


def show_unique_values(data):
    unique_values, counts = np.unique(
        data,
        return_counts=True
    )

    print("\nUnique values:")
    print(unique_values)

    print("Occurrences:")
    print(counts)


# Initial data
scores = np.array([78, 85, 92, 78, 88, 95, 85])

print("Original scores:")
print(scores)


# Add new scores
scores = add_values(scores, [72, 90])

print("\nAfter adding new scores:")
print(scores)


# Combine with another array
additional_scores = np.array([65, 80, 85])

scores = combine_arrays(scores, additional_scores)

print("\nAfter combining arrays:")
print(scores)


# Remove specific values using indices
scores = remove_values(scores, [2, 5])

print("\nAfter removing values:")
print(scores)


# Display array information
array_information(scores)


# Display unique values and frequencies
show_unique_values(scores)