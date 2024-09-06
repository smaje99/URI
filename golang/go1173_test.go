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
func testArrayFillIOutput(t *testing.T, input, expected string) {
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

	// Call the ArrayFillI function (main function)
	ArrayFillI()

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
TestArrayFillI tests the implementation of the Beecrowd exercise 1173.
It runs a series of inputs and checks if the output is as expected.
*/
func TestArrayFillI(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{
			input: "2\n",
			expected: `N[0] = 2
N[1] = 4
N[2] = 8
N[3] = 16
N[4] = 32
N[5] = 64
N[6] = 128
N[7] = 256
N[8] = 512
N[9] = 1024
`,
		},
		{
			input: "5\n",
			expected: `N[0] = 5
N[1] = 10
N[2] = 20
N[3] = 40
N[4] = 80
N[5] = 160
N[6] = 320
N[7] = 640
N[8] = 1280
N[9] = 2560
`,
		},
	}

	// Iterate over the test cases
	for _, test := range tests {
		testArrayFillIOutput(t, test.input, test.expected)
	}
}
