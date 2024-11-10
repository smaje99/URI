"""Beecrowd exercise 1117.
Repetition

See: https://judge.beecrowd.com/es/problems/view/1117
"""

valid_scores: list[float] = []
invalid_count = 0

while len(valid_scores) < 2:
    score = float(input())

    if 0 <= score <= 10:
        valid_scores.append(score)
    else:
        print("nota invalida")
        invalid_count += 1

average = sum(valid_scores) / len(valid_scores)
print(f"media = {average:.2f}")
