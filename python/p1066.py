"""Beecrowd exercise 1066.

See: https://judge.beecrowd.com/es/problems/view/1066
"""

# Reading input values in a more concise way
values = [int(input()) for _ in range(5)]

# Initialize counters for even, odd, positive, and negative numbers
even_count = odd_count = positive_count = negative_count = 0

# Iterate over the list and update the counters based on conditions
for value in values:
    if value % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    if value > 0:
        positive_count += 1
    elif value < 0:
        negative_count += 1

# Printing the results
print(f"{even_count} valor(es) par(es)")
print(f"{odd_count} valor(es) impar(es)")
print(f"{positive_count} valor(es) positivo(s)")
print(f"{negative_count} valor(es) negativo(s)")
