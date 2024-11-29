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
func testBobConduit(t *testing.T, input, expected string) {
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

	// Call the BobConduit function (main function)
	BobConduit()

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
func TestBobConduit(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{
			input: `3
1 1
2 8
8 2
`,
			expected: `2
10
10
`,
		},
		{
			input: `15
1 2
2 3
3 4
4 5
5 6
6 7
9 8
3 3
4 5
12 32
999 999
321 321
215 635
324 909
421 242
`,
			expected: `3
5
7
9
11
13
17
6
9
44
1998
642
850
1233
663
`,
		},
	}

	// Iterate over the test cases
	for _, test := range tests {
		testBobConduit(t, test.input, test.expected)
	}
}
