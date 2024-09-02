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
func testReplaceNullNegativeOutput(t *testing.T, input, expected string) {
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

	// Call the main function
	ArrayReplacementI()

	// Restore the original standard output and input
	w.Close()
	os.Stdout = originalStdout
	io.Copy(&buf, r)
	os.Stdin = originalStdin

	// Compare the captured output with the expected output
	if buf.String() != expected {
		t.Errorf("For input:\n%s\nexpected output:\n%s\nbut got:\n%s", input, expected, buf.String())
	}
}

/*
TestReplaceNullNegative tests the implementation of the Beecrowd exercise.
It runs a series of inputs and checks if the output is as expected.
*/
func TestReplaceNullNegative(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{
			input: `-5
0
12
-8
9
3
-1
6
-2
11
`,
			expected: `X[0] = 1
X[1] = 1
X[2] = 12
X[3] = 1
X[4] = 9
X[5] = 3
X[6] = 1
X[7] = 6
X[8] = 1
X[9] = 11
`,
		},
		{
			input: `-1
-45234
-22
-120
0
2
-200
1
9
22
`,
			expected: `X[0] = 1
X[1] = 1
X[2] = 1
X[3] = 1
X[4] = 1
X[5] = 2
X[6] = 1
X[7] = 1
X[8] = 9
X[9] = 22
`,
		},
	}

	// Iterate over the test cases
	for _, test := range tests {
		testReplaceNullNegativeOutput(t, test.input, test.expected)
	}
}
