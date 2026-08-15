import numpy as np

# Students who joined the sports club.
sports = np.array([1, 2, 3, 4, 5, 6])

# Students who joined the music club.
music = np.array([4, 5, 6, 7, 8, 9])

# 1. Students who joined at least one club (Union)
at_least_one = np.union1d(sports, music)

# 2. Students who joined both clubs (Intersection)
both_clubs = np.intersect1d(sports, music)

# 3. Students who joined only sports (Difference: sports - music)
only_sports = np.setdiff1d(sports, music)

# 4. Students who joined only music (Difference: music - sports)
only_music = np.setdiff1d(music, sports)

# 5. Students who joined exactly one club (Symmetric Difference)
exactly_one = np.setxor1d(sports, music)

# Display results
print("1. Students who joined at least one club:")
print(at_least_one)

print("\n2. Students who joined both clubs:")
print(both_clubs)

print("\n3. Students who joined only sports:")
print(only_sports)

print("\n4. Students who joined only music:")
print(only_music)

print("\n5. Students who joined exactly one club:")
print(exactly_one)