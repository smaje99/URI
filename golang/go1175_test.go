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
func testArrayChangeIOutput(t *testing.T, input, expected string) {
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

	// Call the ArrayChangeI function (main function)
	ArrayChangeI()

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
func TestArrayChangeI(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{
			input: `0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
`,
			expected: `N[0] = 19
N[1] = 18
N[2] = 17
N[3] = 16
N[4] = 15
N[5] = 14
N[6] = 13
N[7] = 12
N[8] = 11
N[9] = 10
N[10] = 9
N[11] = 8
N[12] = 7
N[13] = 6
N[14] = 5
N[15] = 4
N[16] = 3
N[17] = 2
N[18] = 1
N[19] = 0
`,
		},
	}

	// Iterate over the test cases
	for _, test := range tests {
		testArrayChangeIOutput(t, test.input, test.expected)
	}
}
