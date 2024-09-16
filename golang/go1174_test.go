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
func testArraySelectionIOutput(t *testing.T, input, expected string) {
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

	// Call the ArraySelectionI function (main function)
	ArraySelectionI()

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
func TestArraySelectionI(t *testing.T) {
	// Define test cases
	tests := []struct {
		input    string
		expected string
	}{
		{
			input: `-91
-33
17
60
98
-24
-73
51
-70
44
65
-47
55
-56
2
-4
18
50
74
46
-87
18
8
-53
46
30
4
54
23
96
89
85
-48
-80
83
-26
-30
25
-50
-59
73
-88
-90
53
-3
-62
62
30
8
-79
-7
-2
-3
10
-30
-28
-88
-90
98
73
4
48
-96
-88
-3
64
-65
2
-95
50
67
60
53
-1
32
37
-48
-7
99
-6
32
50
-49
8
86
98
76
51
-79
29
-66
-70
-53
-69
33
67
56
-35
-7
83
`,
			expected: `A[0] = -91.0
A[1] = -33.0
A[5] = -24.0
A[6] = -73.0
A[8] = -70.0
A[11] = -47.0
A[13] = -56.0
A[14] = 2.0
A[15] = -4.0
A[20] = -87.0
A[22] = 8.0
A[23] = -53.0
A[26] = 4.0
A[32] = -48.0
A[33] = -80.0
A[35] = -26.0
A[36] = -30.0
A[38] = -50.0
A[39] = -59.0
A[41] = -88.0
A[42] = -90.0
A[44] = -3.0
A[45] = -62.0
A[48] = 8.0
A[49] = -79.0
A[50] = -7.0
A[51] = -2.0
A[52] = -3.0
A[53] = 10.0
A[54] = -30.0
A[55] = -28.0
A[56] = -88.0
A[57] = -90.0
A[60] = 4.0
A[62] = -96.0
A[63] = -88.0
A[64] = -3.0
A[66] = -65.0
A[67] = 2.0
A[68] = -95.0
A[73] = -1.0
A[76] = -48.0
A[77] = -7.0
A[79] = -6.0
A[82] = -49.0
A[83] = 8.0
A[88] = -79.0
A[90] = -66.0
A[91] = -70.0
A[92] = -53.0
A[93] = -69.0
A[97] = -35.0
A[98] = -7.0
`,
		},
	}

	// Iterate over the test cases
	for _, test := range tests {
		testArraySelectionIOutput(t, test.input, test.expected)
	}
}
