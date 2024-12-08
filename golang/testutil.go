package beecrowd

import (
	"bytes"
	"io"
	"os"
	"testing"

	"github.com/andreyvit/diff"
)

// RunTest simulates the input/output environment for a function and validates the result.
// Params:
// - t: *testing.T instance for reporting errors.
// - fn: Function to test, typically your main function.
// - input: Input string to simulate stdin.
// - expected: Expected output string for comparison.
func RunTest(t *testing.T, fn func(), input, expected string) {
	// Redirect stdout to a buffer
	originalStdout := os.Stdout
	var buf bytes.Buffer
	r, w, _ := os.Pipe()
	os.Stdout = w

	// Redirect stdin to a pipe with the given input
	originalStdin := os.Stdin
	pr, pw, _ := os.Pipe()
	os.Stdin = pr
	pw.Write([]byte(input))
	pw.Close()

	// Execute the test function
	fn()

	// Restore original stdin and stdout
	w.Close()
	os.Stdout = originalStdout
	io.Copy(&buf, r)
	os.Stdin = originalStdin

	// Compare output with expected
	actual := buf.String()
	if actual != expected {
		t.Errorf(
			"\nInput:\n%s\nExpected:\n%s\nActual:\n%s\nDiff:\n%v",
			input, expected, actual, diff.LineDiff(expected, actual),
		)
	}
}
