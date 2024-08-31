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
func testPerfectNumberOutput(t *testing.T, input, expected string) {
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
	main()

	// Restore the original standard output and input
	w.Close()
	os.Stdout = originalStdout
	io.Copy(&buf, r)
	os.Stdin = originalStdin

	// Compare the captured output with the expected output
	if buf.String() != expected {
		t.Errorf("For input\n%s\nexpected output:\n%s\nbut got:\n%s", input, expected, buf.String())
	}
}

/*
TestBeeCrowd1164 tests the implementation of the Beecrowd exercise 1164.
It runs a series of inputs and checks if the output is as expected.
*/
func TestBeeCrowd1164(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{
			input:    "3\n6\n5\n28\n",
			expected: "6 eh perfeito\n5 nao eh perfeito\n28 eh perfeito\n",
		},
	}

	// Iterate over the test cases
	for _, test := range tests {
		testPerfectNumberOutput(t, test.input, test.expected)
	}
}
