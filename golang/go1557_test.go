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
func testSquareMatrixIII(t *testing.T, input, expected string) {
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

	// Call the SquareMatrixIII function (main function)
	SquareMatrixIII()

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
func TestSquareMatrixIII(t *testing.T) {
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
			expected: `1

1 2
2 4

 1  2  4
 2  4  8
 4  8 16

 1  2  4  8
 2  4  8 16
 4  8 16 32
 8 16 32 64

  1   2   4   8  16
  2   4   8  16  32
  4   8  16  32  64
  8  16  32  64 128
 16  32  64 128 256

`,
		},
		{
			input: `3
5
7
8
0
`,
			expected: ` 1  2  4
 2  4  8
 4  8 16

  1   2   4   8  16
  2   4   8  16  32
  4   8  16  32  64
  8  16  32  64 128
 16  32  64 128 256

   1    2    4    8   16   32   64
   2    4    8   16   32   64  128
   4    8   16   32   64  128  256
   8   16   32   64  128  256  512
  16   32   64  128  256  512 1024
  32   64  128  256  512 1024 2048
  64  128  256  512 1024 2048 4096

    1     2     4     8    16    32    64   128
    2     4     8    16    32    64   128   256
    4     8    16    32    64   128   256   512
    8    16    32    64   128   256   512  1024
   16    32    64   128   256   512  1024  2048
   32    64   128   256   512  1024  2048  4096
   64   128   256   512  1024  2048  4096  8192
  128   256   512  1024  2048  4096  8192 16384

`,
		},
	}

	// Iterate over the test cases
	for _, test := range tests {
		testSquareMatrixIII(t, test.input, test.expected)
	}
}
