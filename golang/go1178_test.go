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
func testArrayFillIIIOutput(t *testing.T, input, expected string) {
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

	// Call the ArrayFillIII function (main function)
	ArrayFillIII()

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
func TestArrayFillIII(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{
			input: "200.000",
			expected: `N[0] = 200.0000
N[1] = 100.0000
N[2] = 50.0000
N[3] = 25.0000
N[4] = 12.5000
N[5] = 6.2500
N[6] = 3.1250
N[7] = 1.5625
N[8] = 0.7812
N[9] = 0.3906
N[10] = 0.1953
N[11] = 0.0977
N[12] = 0.0488
N[13] = 0.0244
N[14] = 0.0122
N[15] = 0.0061
N[16] = 0.0031
N[17] = 0.0015
N[18] = 0.0008
N[19] = 0.0004
N[20] = 0.0002
N[21] = 0.0001
N[22] = 0.0000
N[23] = 0.0000
N[24] = 0.0000
N[25] = 0.0000
N[26] = 0.0000
N[27] = 0.0000
N[28] = 0.0000
N[29] = 0.0000
N[30] = 0.0000
N[31] = 0.0000
N[32] = 0.0000
N[33] = 0.0000
N[34] = 0.0000
N[35] = 0.0000
N[36] = 0.0000
N[37] = 0.0000
N[38] = 0.0000
N[39] = 0.0000
N[40] = 0.0000
N[41] = 0.0000
N[42] = 0.0000
N[43] = 0.0000
N[44] = 0.0000
N[45] = 0.0000
N[46] = 0.0000
N[47] = 0.0000
N[48] = 0.0000
N[49] = 0.0000
N[50] = 0.0000
N[51] = 0.0000
N[52] = 0.0000
N[53] = 0.0000
N[54] = 0.0000
N[55] = 0.0000
N[56] = 0.0000
N[57] = 0.0000
N[58] = 0.0000
N[59] = 0.0000
N[60] = 0.0000
N[61] = 0.0000
N[62] = 0.0000
N[63] = 0.0000
N[64] = 0.0000
N[65] = 0.0000
N[66] = 0.0000
N[67] = 0.0000
N[68] = 0.0000
N[69] = 0.0000
N[70] = 0.0000
N[71] = 0.0000
N[72] = 0.0000
N[73] = 0.0000
N[74] = 0.0000
N[75] = 0.0000
N[76] = 0.0000
N[77] = 0.0000
N[78] = 0.0000
N[79] = 0.0000
N[80] = 0.0000
N[81] = 0.0000
N[82] = 0.0000
N[83] = 0.0000
N[84] = 0.0000
N[85] = 0.0000
N[86] = 0.0000
N[87] = 0.0000
N[88] = 0.0000
N[89] = 0.0000
N[90] = 0.0000
N[91] = 0.0000
N[92] = 0.0000
N[93] = 0.0000
N[94] = 0.0000
N[95] = 0.0000
N[96] = 0.0000
N[97] = 0.0000
N[98] = 0.0000
N[99] = 0.0000
`,
		},
	}

	// Iterate over the test cases
	for _, test := range tests {
		testArrayFillIIIOutput(t, test.input, test.expected)
	}
}
