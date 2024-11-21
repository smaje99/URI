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
func testArray123(t *testing.T, input, expected string) {
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

	// Call the Array123 function (main function)
	Array123()

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
func TestArray123(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{
			input: "3\n",
			expected: `132
323
231
`,
		},
		{
			input: `9
6
5
6
3
`,
			expected: `133333332
313333323
331333233
333132333
333323333
333231333
332333133
323333313
233333331
133332
313323
331233
332133
323313
233331
13332
31323
33233
32313
23331
133332
313323
331233
332133
323313
233331
132
323
231
`,
		},
	}

	// Iterate over the test cases
	for _, test := range tests {
		testArray123(t, test.input, test.expected)
	}
}
