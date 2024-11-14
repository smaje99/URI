package beecrowd

import (
	"bytes"
	"io"
	"os"
	"testing"
)

/*
Helper function to simulate the input/output process for a Beecrowd-like environment.
It uses a byte buffer to capture the output and compares it against the expected result.

Parameters:
- input: string representing the input data (formatted as it would be entered).
- expected: string representing the expected output (formatted as it would be printed).
*/
func testSquareMatrixII(t *testing.T, input, expected string) {
	// Redirect the standard output to a buffer to capture printed results
	originalStdout := os.Stdout
	var buf bytes.Buffer
	r, w, _ := os.Pipe()
	os.Stdout = w

	// Simulate standard input by manually scanning inputs
	originalStdin := os.Stdin
	pr, pw, _ := os.Pipe()
	os.Stdin = pr
	pw.Write([]byte(input))
	pw.Close()

	// Call the SquareMatrixII function (main function)
	SquareMatrixII()

	// Restore the original standard output and input
	w.Close()
	os.Stdout = originalStdout
	io.Copy(&buf, r)
	os.Stdin = originalStdin

	// Compare the captured output with the expected output
	if buf.String() != expected {
		t.Errorf(
			"For input\n%s\nexpected output:\n%s\nbut got:\n%s",
			input,
			expected,
			buf.String(),
		)
	}
}

/*
TestArraySelectionI tests the implementation of the Beecrowd exercise 1174.
It runs a series of inputs and checks if the output is as expected.
*/
func TestSquareMatrixII(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{
			input: `1
2
3
4
5
0
`,
			expected: `  1

  1   2
  2   1

  1   2   3
  2   1   2
  3   2   1

  1   2   3   4
  2   1   2   3
  3   2   1   2
  4   3   2   1

  1   2   3   4   5
  2   1   2   3   4
  3   2   1   2   3
  4   3   2   1   2
  5   4   3   2   1

`,
		},
		{
			input: `9
10
0
`,
			expected: `  1   2   3   4   5   6   7   8   9
  2   1   2   3   4   5   6   7   8
  3   2   1   2   3   4   5   6   7
  4   3   2   1   2   3   4   5   6
  5   4   3   2   1   2   3   4   5
  6   5   4   3   2   1   2   3   4
  7   6   5   4   3   2   1   2   3
  8   7   6   5   4   3   2   1   2
  9   8   7   6   5   4   3   2   1

  1   2   3   4   5   6   7   8   9  10
  2   1   2   3   4   5   6   7   8   9
  3   2   1   2   3   4   5   6   7   8
  4   3   2   1   2   3   4   5   6   7
  5   4   3   2   1   2   3   4   5   6
  6   5   4   3   2   1   2   3   4   5
  7   6   5   4   3   2   1   2   3   4
  8   7   6   5   4   3   2   1   2   3
  9   8   7   6   5   4   3   2   1   2
 10   9   8   7   6   5   4   3   2   1

`,
		},
	}

	// Iterate over the test cases
	for _, test := range tests {
		testSquareMatrixII(t, test.input, test.expected)
	}
}
