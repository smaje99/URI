package beecrowd

import (
	"bytes"
	"io"
	"os"
	"testing"
	"github.com/andreyvit/diff"
)

/*
Helper function to simulate the input/output process for a Beecrowd-like environment.
It uses a byte buffer to capture the output and compares it against the expected result.

Parameters:
- input: string representing the input data (formatted as it would be entered).
- expected: string representing the expected output (formatted as it would be printed).
*/
func testTheRaceOfSlugs(t *testing.T, input, expected string) {
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

	// Call the TheRaceOfSlugs function (main function)
	TheRaceOfSlugs()

	// Restore the original standard output and input
	w.Close()
	os.Stdout = originalStdout
	io.Copy(&buf, r)
	os.Stdin = originalStdin

	// Compare the captured output with the expected output
	a := buf.String()
	e := expected
	if a != e {
		t.Errorf(
			"For input\n%s\nexpected output:\n%s\nbut got:\n%s\nDiff:\n%v",
			input,
			expected,
			buf.String(),
			diff.LineDiff(e, a),
		)
	}
}

/*
TestArraySelectionI tests the implementation of the Beecrowd exercise 1174.
It runs a series of inputs and checks if the output is as expected.
*/
func TestTheRaceOfSlugs(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{
			input: `10
10 10 10 10 15 18 20 15 11 10
10
1 5 2 9 5 5 8 4 4 3
10
19 9 1 4 5 8 6 11 9 7
`,
			expected: `3
1
2
`,
		},
		{
			input: `2
3 5
3
4 8 15
4
5 10 50 5
`,
			expected: `1
2
3
`,
		},
	}

	// Iterate over the test cases
	for _, test := range tests {
		testTheRaceOfSlugs(t, test.input, test.expected)
	}
}