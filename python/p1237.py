"""Beecrowd exercise 1237.
Compare Substring.
LCS

See: https://judge.beecrowd.com/es/problems/view/1237
"""

from difflib import SequenceMatcher


def main():
    """Main function."""
    while True:
        try:
            pa = input()
            pb = input()

            # Find the longest common substring
            matcher = SequenceMatcher(None, pa, pb)
            match = matcher.find_longest_match(0, len(pa), 0, len(pb))

            print(match.size)
        except EOFError:
            break


if __name__ == "__main__":
    main()
